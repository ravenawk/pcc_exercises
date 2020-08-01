#!/usr/bin/env python3
from admin_privileges import Admin

the_admin = Admin("Bruce", "Wayne")
the_admin.privileges.set_privileges("can change user passwords")
the_admin.privileges.describe_privileges()