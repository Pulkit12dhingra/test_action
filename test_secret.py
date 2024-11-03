import os

# Read the secret from the environment
my_secret = os.getenv("TEST_SECRET")

# Use the secret in your code
print(f"The secret is: {my_secret}")
