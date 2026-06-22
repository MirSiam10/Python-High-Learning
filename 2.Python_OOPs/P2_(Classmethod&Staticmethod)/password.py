class Password:

    def __init__(self, raw_password: str):

        if not self.is_valid_format(raw_password):
            raise ValueError("Password must be at least 8 characters and contain at least one digit")

        self.raw_password = raw_password
        self._hashed = self._hash(raw_password)

    def _hash(self, password: str):
        return password[::-1] + "***"
    
    def check_password(self, attempt: str):
        return self._hash(attempt) == self._hashed

    @staticmethod
    def is_valid_format(password: str):
        return len(password) >= 8 and any(char.isdigit() for char in password)
    
    @classmethod
    def generate_default(cls):
        return cls("Default1")


p = Password("Securepass1")
print(p.check_password("Securepass1"))   # True
print(p.check_password("Wrongpass2"))    # False

print(Password.is_valid_format("short"))  # False
print(Password.is_valid_format("Longpass9"))  # True

Default = Password.generate_default()
print(Default)
print(Default.check_password("Default1"))


