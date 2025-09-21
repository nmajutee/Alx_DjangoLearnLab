# Django Permissions and Groups Setup

This project shows how to use custom permissions and groups in Django.

## What I Created

### 1. Custom Permissions
I added custom permissions to the Book model:
- can_view
- can_create
- can_edit
- can_delete

### 2. User Groups
Created 3 groups with different permissions:
- **Viewers**: Can only view books
- **Editors**: Can view, create, and edit books
- **Admins**: Can view, create, edit, and delete books

### 3. Protected Views
Created views that check permissions:
- book_list (requires can_view)
- book_create (requires can_create)
- book_edit (requires can_edit)
- book_delete (requires can_delete)

## How to Use

1. Run the setup command:
```bash
python manage.py setup_groups
```

2. Create users in Django admin

3. Assign users to groups

4. Test the permissions by logging in as different users

## Files Modified
- models.py: Added Book model with custom permissions
- views.py: Added permission-protected views
- admin.py: Registered Book model
- setup_groups.py: Management command to create groups