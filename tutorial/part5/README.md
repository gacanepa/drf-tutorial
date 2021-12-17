# Notes

- Hyperlinking is a way to link to other resources in the API (besides primary keys).
  - It requires URL patterns to be named.
- The `reverse` function returns fully-qualified URLs.

  - It can use convenience names to identify URL patterns.

- Differences between `ModelSerializer` and `HyperlinkedModelSerializer`:
  - `HyperlinkedModelSerializer` does not include an `id` field.
  - `HyperlinkedModelSerializer` has a `url` field.
  - Hyperlinked relationships use `HyperlinkedRelatedField` instead of `PrimaryKeyRelatedField`.
