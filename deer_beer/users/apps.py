import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "deer_beer.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import deer_beer.users.signals  # noqa: F401
