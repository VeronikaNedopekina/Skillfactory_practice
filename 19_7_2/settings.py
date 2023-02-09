import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
invalid_auth_key = os.getenv('valid_auth_key')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')
empty_email = os.getenv('empty_email')
empty_password = os.getenv('empty_password')
