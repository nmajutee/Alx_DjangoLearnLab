"""
Management command to set up user groups and permissions.
This command creates the required groups (Editors, Viewers, Admins) and assigns
appropriate permissions to each group.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book


class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Setting up groups and permissions...')
        )

        # Get the Book content type
        book_content_type = ContentType.objects.get_for_model(Book)

        # Get or create custom permissions for Book model
        permissions = {}
        permission_codenames = ['can_view', 'can_create', 'can_edit', 'can_delete']

        for codename in permission_codenames:
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                name=f'Can {codename.split("_")[1]} book',
                content_type=book_content_type,
            )
            permissions[codename] = permission
            if created:
                self.stdout.write(f'Created permission: {permission.name}')
            else:
                self.stdout.write(f'Permission already exists: {permission.name}')

        # Create groups and assign permissions
        groups_config = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, permission_codenames in groups_config.items():
            group, created = Group.objects.get_or_create(name=group_name)

            if created:
                self.stdout.write(f'Created group: {group_name}')
            else:
                self.stdout.write(f'Group already exists: {group_name}')

            # Clear existing permissions and add new ones
            group.permissions.clear()

            for codename in permission_codenames:
                group.permissions.add(permissions[codename])
                self.stdout.write(f'  Added permission {codename} to {group_name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully set up groups and permissions!')
        )

        # Display summary
        self.stdout.write('\nSummary:')
        for group_name, permission_codenames in groups_config.items():
            group = Group.objects.get(name=group_name)
            self.stdout.write(f'  {group_name}: {len(permission_codenames)} permissions')
            for codename in permission_codenames:
                self.stdout.write(f'    - {codename}')