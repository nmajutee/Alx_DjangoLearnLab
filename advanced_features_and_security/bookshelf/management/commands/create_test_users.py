"""
Management command to create test users and assign them to groups.
This command creates test users for each group to demonstrate the permission system.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    help = 'Create test users and assign them to groups'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-existing',
            action='store_true',
            help='Skip creating users that already exist',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Creating test users and assigning them to groups...')
        )

        # Test users configuration
        test_users = [
            {
                'username': 'viewer_user',
                'email': 'viewer@example.com',
                'first_name': 'View',
                'last_name': 'User',
                'group': 'Viewers',
                'password': 'testpass123',
            },
            {
                'username': 'editor_user',
                'email': 'editor@example.com',
                'first_name': 'Edit',
                'last_name': 'User',
                'group': 'Editors',
                'password': 'testpass123',
            },
            {
                'username': 'admin_user',
                'email': 'admin@example.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'group': 'Admins',
                'password': 'testpass123',
            },
        ]

        # Get all groups
        groups = {}
        for group_name in ['Viewers', 'Editors', 'Admins']:
            try:
                groups[group_name] = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Group {group_name} does not exist. Run setup_groups command first.')
                )
                return

        # Create users and assign to groups
        for user_data in test_users:
            username = user_data['username']
            group_name = user_data['group']

            try:
                # Check if user already exists
                if User.objects.filter(username=username).exists():
                    if options['skip_existing']:
                        self.stdout.write(f'User {username} already exists, skipping...')
                        continue
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'User {username} already exists, updating...')
                        )
                        user = User.objects.get(username=username)
                else:
                    # Create new user
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name'],
                        password=user_data['password'],
                    )
                    self.stdout.write(f'Created user: {username}')

                # Clear existing groups and add to new group
                user.groups.clear()
                group = groups[group_name]
                user.groups.add(group)

                self.stdout.write(f'  Assigned {username} to {group_name} group')

            except IntegrityError as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating user {username}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully created test users!')
        )

        # Display summary
        self.stdout.write('\nTest Users Created:')
        for user_data in test_users:
            username = user_data['username']
            group_name = user_data['group']
            password = user_data['password']
            self.stdout.write(f'  Username: {username}')
            self.stdout.write(f'  Password: {password}')
            self.stdout.write(f'  Group: {group_name}')
            self.stdout.write('')