# PostgreSQL / PostgREST Security Hardening

This Django app can run on PostgreSQL via Supabase or a similar provider. When the `public` schema is exposed through PostgREST, default Django system tables can become visible and trigger security warnings.

## Problem

Default Django metadata and auth tables are created in the `public` schema:

- `public.django_migrations`
- `public.auth_user`
- `public.auth_group`
- `public.auth_permission`
- `public.auth_user_groups`
- `public.auth_user_user_permissions`
- `public.django_content_type`
- `public.auth_group_permissions`

If these tables are exposed to PostgREST without Row Level Security (RLS), scanners will flag them.

## Recommended fix

1. Restrict API exposure so PostgREST does not serve Django internal tables.
2. Enable RLS on internal tables if they must remain in `public`.
3. Use role-based policies for any query access that must remain available.

## Example remediation SQL

If the database is PostgreSQL, run the SQL in `postgres/enable_rls_internal_tables.sql`.

After enabling RLS, you should add explicit policies for the roles that need access. For example, if your application uses a service role, keep that role separate from `anon` or public API roles.

## How this works

The SQL applied does three things:

- Enables row level security on internal Django tables and app table.
- Adds explicit deny-all policies on sensitive tables for `anon` and `authenticated`, so no rows are exposed by default.
- Adds a minimal allow policy for `public.todos_todo` so authenticated users can read app data.

Because RLS is enabled, PostgreSQL blocks access to every row unless a policy allows it. The deny policies ensure the default state is "no access," and the allow policy for `todos_todo` opens only the specific operation you want.

## Best practice

- Do not expose `auth_*`, `django_*`, or other internal system tables through PostgREST.
- Expose only the application tables needed by the API.
- Prefer separate schemas or dedicated database roles for internal metadata.
