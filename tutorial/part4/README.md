# Notes

- The relationship between snippets and authors is given through the `owner` field. This is a foreign key that maps to the `auth.User` model.

- To create new superusers:

```python
python manage.py createsuperuser
```

- Regular users:

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
new_user = User.objects.create_user("test", password = "supersecret1")
new_user.is_superuser = False
new_user.is_staff = False
new_user.save()
```
