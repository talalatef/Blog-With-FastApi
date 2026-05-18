import bcrypt

class Hash:
    @staticmethod
    def bcrypt(password: str):
        password_bytes = password[:72].encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt).decode("utf-8")

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        return bcrypt.checkpw(
            plain_password[:72].encode("utf-8"),
            hashed_password.encode("utf-8")
        )
