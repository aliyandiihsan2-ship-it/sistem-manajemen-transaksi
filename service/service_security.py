from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("dummypassword")

class SecurityService:
    def verify_password(self,plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    def get_password_hash(self,password):
        return password_hash.hash(password)
