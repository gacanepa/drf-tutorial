from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root

# Key-value pairs where the key is the HTTP method and the value is the viewset action
snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})

snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

snippet_highlight = SnippetViewSet.as_view({"get": "highlight"})

user_list = UserViewSet.as_view({"get": "retrieve"})

user_detail = UserViewSet.as_view({"get": "retrieve"})

urlpatterns = format_suffix_patterns(
    [
        path("", api_root),
        path("snippets/", snippet_list, name="snippet-list"),
        path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>/", user_detail, name="user-detail"),
        path(
            "snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"
        ),
    ]
)

urlpatterns = format_suffix_patterns(urlpatterns)
