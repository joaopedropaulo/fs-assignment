from passlib.context import CryptContext

# Service for Security operations

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Gets a plain text password and compares it with a hashed password to verify if they match
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Hashes a plain text password
def get_password_hash(password):
    return pwd_context.hash(password)