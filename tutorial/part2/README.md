# Notes

- The DRF provides two special objects out of the box:

  - The `Request` object makes parsing easier. The `request.data` property can handle arbitrary data and works for `POST`, `PUT` and `PATCH` operations.
  - The `Response` object takes unrendered content and uses [content negotiation](https://restfulapi.net/content-negotiation/) to determine the correct return type.

- It also provides a series of status codes for readability. Using an identifier (such as `HTTP_400_BAD_REQUEST`) from the `status` module is easier to understand than just `400`.
