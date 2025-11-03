from typing import Iterable
from django.contrib.auth.decorators import login_required, user_passes_test


def _in_groups(user, roles: Iterable[str], allow_staff=True, allow_superuser=True) -> bool:
    if not user.is_authenticated:
        return False
    if allow_superuser and user.is_superuser:
        return True
    if allow_staff and user.is_staff:
        return True
    return user.groups.filter(name__in=list(roles)).exists()

def roles_required(*roles, allow_staff=True, allow_superuser=True, login_url="login"):
    """
    Permite acceso si el usuario pertenece a AL MENOS uno de los roles dados.
    Uso:
      @roles_required("Empresario")
      @roles_required("Modelo", "Moderador", allow_staff=False)
    """
    def predicate(u):
        return _in_groups(u, roles, allow_staff=allow_staff, allow_superuser=allow_superuser)
    def decorator(viewfunc):
        return login_required(user_passes_test(predicate, login_url=login_url))(viewfunc)
    return decorator
