from bank import Bank
import hashlib

class BankAccount:
    def __init__(self, username, password):
        if not username:
            raise ValueError("Username cannot be empty")
        if not password:
            raise ValueError("Password cannot be empty")
        self.username = username
        self.password_hash = self.hash_password(password)
        self.bank = Bank()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)