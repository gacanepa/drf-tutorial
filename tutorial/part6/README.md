# Notes

- Viewsets are class-based views that combine the logic for list, detail,
  create, update, and destroy actions. They do not provide any method handlers such as `.get()` or `.post()`.

  - Reduce the amount of code we need to write to implement the required functionality.
  - Allow to create routable, custom actions using decorators, and other methods as well.
  - Ensure URL conventions are consistent across the API.
  - Are less explicit than building individual views (this might be the only downside of viewsets).

- Routers leverage viewsets to build URL confs automatically
  - Register the viewsets with a router.
  - The `DefaultRouter` class creates the API root view (we can dispense with the `api_root` method in our views).
