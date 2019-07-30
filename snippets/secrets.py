# Create a secret key using Python
import secrets

secret_key = secrets.token_hex(32)
print(secret_key)
