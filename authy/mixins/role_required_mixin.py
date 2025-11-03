# mixin/mixins.py
from typing import Sequence
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    roles: Sequence[str] = ()
    allow_staff: bool = True
    allow_superuser: bool = True
    raise_exception = True  # 403 si está logueado pero no tiene permisos

    def test_func(self):
        u = self.request.user
        if not u.is_authenticated:
            return False
        if self.allow_superuser and u.is_superuser:
            return True
        if self.allow_staff and u.is_staff:
            return True
        if not self.roles:
            return True  # si no seteaste roles, no bloquea
        return u.groups.filter(name__in=self.roles).exists()
