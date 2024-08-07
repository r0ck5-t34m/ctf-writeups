# Passworldless

## Analyzing the Code

1. UUID Generation:
    - The UUID for any username is generated using uuid.uuid5(leet, username).
    - The leet UUID is fixed: 13371337-1337-1337-1337-133713371337.
    - The goal is to generate the same UUID that is generated for the username admin123.

2. Checking for Admin UUID:
    - The route /<uid> checks if the provided uid matches uuid.uuid5(leet, 'admin123').
    - If it matches, it returns the flag; otherwise, it returns a message that no flag is available.

## Steps to Retrieve the Flag

To get the flag, we need to generate the UUID for the username admin123 using the same logic as the application and then access the route with this UUID.

We can use a simple Python script to generate the UUID and then use it to access the /uuid route.

Here's the Python code to generate the UUID:

```python
import uuid

leet = uuid.UUID('13371337-1337-1337-1337-133713371337')
admin_uuid = uuid.uuid5(leet, 'admin123')
print(admin_uuid)```

Running this script will give us the UUID. Let’s say the UUID generated is UUID_GENERATED.

## Accessing the Flag

Once you have the UUID, you can access the /UUID_GENERATED route to get the flag. You can use a browser, curl, or any HTTP client to access the route. Here's how you can do it with curl:

```sh
curl http://localhost:1337/UUID_GENERATED```

