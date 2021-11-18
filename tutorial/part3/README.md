# Notes

- Class-based views allow us to create reusable resources by leveraging mixins.
  - Mixins offer common functionality (create, retrieve, update, and delete) for API views. They are special classes that are not intended to be instantiated. Their primary use is to provide optional features to a class or to expose a given feature for use in several separate classes.
    - For example, if we make `SnippetDetail` inherit from `mixins.RetrieveModelMixin`, `mixins.UpdateModelMixin`, and `mixins.DestroyModelMixin`, we can create `get`, `put`, and `delete` methods with `self.retrieve`, `self.update`, and `self.destroy` respectively, which are included in the mixins.
    - The arguments to these methods are identical: `self`, `request`, `*args`, and `**kwargs`.
  - The DRF includes a series of generic views that we can use to accomplish the same goal: `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView`.
