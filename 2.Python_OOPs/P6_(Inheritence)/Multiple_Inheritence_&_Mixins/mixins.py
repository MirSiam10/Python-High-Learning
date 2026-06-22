class JSONSerializableMixin:
    """Adds JSON conversion to ANY class that uses it."""
    def to_dict(self):
        return self.__dict__

class LoggableMixin:
    """Adds logging to ANY class that uses it."""
    def log(self, action):
        print(f"[LOG] {self.__class__.__name__}: {action}")


class User(JSONSerializableMixin, LoggableMixin):
    def __init__(self, name, email):
        self.name  = name
        self.email = email

u = User("Ashin", "ashin@example.com")
print(u.to_dict())     # {'name': 'Ashin', 'email': 'ashin@example.com'}
u.log("User created")  # [LOG] User: User created