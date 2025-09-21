from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from bookshelf.models import Book
from datetime import date


User = get_user_model()


class Command(BaseCommand):
    """
    Management command to create test users and sample data for testing permissions.

    Creates:
    - 3 test users (viewer, editor, admin)
    - Assigns them to appropriate groups
    - Creates sample books for testing

    Usage: python manage.py create_test_users
    """
    help = 'Create test users with different permission levels and sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating test users and sample data...'))

        # Create test users
        test_users = [
            {'username': 'viewer_user', 'email': 'viewer@test.com', 'group': 'Viewers'},
            {'username': 'editor_user', 'email': 'editor@test.com', 'group': 'Editors'},
            {'username': 'admin_user', 'email': 'admin@test.com', 'group': 'Admins'},
        ]

        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['username'].split('_')[0].title(),
                }
            )

            if created:
                user.set_password('testpass123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
            else:
                self.stdout.write(f'User {user.username} already exists')

            # Assign to group
            try:
                group = Group.objects.get(name=user_data['group'])
                user.groups.add(group)
                self.stdout.write(f'Added {user.username} to {group.name} group')
            except Group.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Group {user_data["group"]} does not exist'))

        # Create sample books
        sample_books = [
            {
                'title': 'Django for Beginners',
                'author': 'William S. Vincent',
                'publication_date': date(2022, 1, 15),
                'isbn': '9781735467207',
                'pages': 356,
                'available': True
            },
            {
                'title': 'Two Scoops of Django 3.x',
                'author': 'Daniel Roy Greenfeld',
                'publication_date': date(2021, 6, 1),
                'isbn': '9780692915721',
                'pages': 532,
                'available': True
            },
            {
                'title': 'Django REST Framework Guide',
                'author': 'Tech Author',
                'publication_date': date(2023, 3, 10),
                'isbn': '9781234567890',
                'pages': 428,
                'available': False
            }
        ]

        for book_data in sample_books:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults=book_data
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created book: {book.title}'))
            else:
                self.stdout.write(f'Book {book.title} already exists')

        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.WARNING('TEST USERS CREATED:'))
        self.stdout.write('='*60)
        self.stdout.write('Username: viewer_user | Password: testpass123 | Group: Viewers')
        self.stdout.write('  - Can only VIEW books')
        self.stdout.write('')
        self.stdout.write('Username: editor_user | Password: testpass123 | Group: Editors')
        self.stdout.write('  - Can VIEW, CREATE, and EDIT books')
        self.stdout.write('')
        self.stdout.write('Username: admin_user | Password: testpass123 | Group: Admins')
        self.stdout.write('  - Can VIEW, CREATE, EDIT, and DELETE books')
        self.stdout.write('='*60)
        self.stdout.write('\nTest these users by:')
        self.stdout.write('1. Logging into Django Admin with each user')
        self.stdout.write('2. Visiting: /bookshelf/security-test/')
        self.stdout.write('3. Trying to access: /bookshelf/books/')
        self.stdout.write('4. Testing create/edit/delete operations')
        self.stdout.write('='*60)