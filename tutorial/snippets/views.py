from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new object
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
