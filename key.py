#this is for a secure admin-only key used to access admin commands for bot.
import secrets
import string

def generate_key(length=4):
    characters = string.ascii_uppercase + string.digits  # A-Z + 0-9
    key = ''.join(secrets.choice(characters) for _ in range(length))
    
    return key

key = generate_key()
print("Checking if key is working, by testing: "+key)

