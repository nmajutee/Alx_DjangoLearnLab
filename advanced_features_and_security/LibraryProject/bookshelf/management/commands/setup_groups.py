from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **options):
        book_content_type = ContentType.objects.get_for_model(Book)

        can_view = Permission.objects.get(codename='can_view', content_type=book_content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=book_content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=book_content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=book_content_type)

        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        viewers_group.permissions.add(can_view)

        editors_group, created = Group.objects.get_or_create(name='Editors')
        editors_group.permissions.add(can_view, can_create, can_edit)

        admins_group, created = Group.objects.get_or_create(name='Admins')
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

        print('Groups created successfully')