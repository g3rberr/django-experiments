from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.get(pk=4)
        group, created = Group.objects.get_or_create(
            name = 'profile_manager',
        )
        permission_profile = Permission.objects.get(
            codename='view_profile'
        )
        permission_logentry = Permission.objects.get(
            codename='view_logentry',
        )

        # добавление разрешения в группу
        group.permissions.add(permission_profile)

        # присоединение пользователя к группе
        user.groups.add(group)

        # связать пользователя напрямую в разрешения
        