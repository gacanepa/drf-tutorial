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

- [Reverse relations](https://www.django-rest-framework.org/api-guide/relations/#reverse-relations) are not included in the `ModelSerializer` class. We need to add them explicitly in the fields list (`snippets` in this example):

```python
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
```

which would translate to a serialization like the following:

```json
{
  "id": 1,
  "username": "test",
  "snippets": [1, 2]
}
```

- To modify how we create a snippet, we can override `perform_create`. This allows us to add extra fields or data before saving the object. Note that the owner is a property of the HTTP request.

  - If we wanted to manipulate the response, we can override the `create` method instead.

- To implement types of access control, we can use the default permissions from the REST framework or create [custom ones](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions).
  - The default checks are:
    - `IsAuthenticated`: Only authenticated users can access the API.
    - `IsAdminUser`: Only superusers can access the API.
    - `IsAuthenticatedOrReadOnly`: Only authenticated users can create new objects, but anyone can read existing ones.
  - Custom permissions override `BasePermission` and need to implement `has_permission` (view level) and `has_object_permission` (object level) methods (at least one of them). The latter is called if the former's checks have already passed.
