# Notes

- The `get_all_lexers()` function from the `pygments.lexers` module returns an [iterator](https://stackoverflow.com/a/9884259/14712859) that yields tuples in the form `(name, aliases, filetypes, mimetypes)`. [Here's](https://stackoverflow.com/questions/3828352/what-is-a-mime-type) a good explanation on MIME types.

> In `LANGUAGE_CHOICES` (refer to the `Snippet` model), the tutorial uses indices to access items. I replaced that with a dictionary to indicate what we are extracting out of the tuples.

- Serializers convert snippet instances to/from representations such as JSON.

- `ModelSerializer` allows writing more concise serializer classes:
  - Determine the set of fields automatically
  - Put default implementations for the `create()` and `update()` methods in place without reinventing the wheel

- By convention, serializers are named after the model they are associated with (e.g. `Snippet` model --> `SnippetSerializer`)
  - The `class Meta` has two required attributes: `model` and `fields` (`__all__` or a list of fields)