-- Enable row level security on default Django internal tables.
-- After enabling RLS, add policies for the roles that must still query these tables.

ALTER TABLE public.django_migrations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_user ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_group ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_permission ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_user_groups ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_user_user_permissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.django_content_type ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.auth_group_permissions ENABLE ROW LEVEL SECURITY;
