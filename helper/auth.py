from passlib.context import CryptContext

class AuthHandler():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")    

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)