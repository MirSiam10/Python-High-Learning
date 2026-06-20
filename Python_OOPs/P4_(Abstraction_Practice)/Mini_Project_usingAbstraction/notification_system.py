from abc import ABC , abstractmethod

class NotificationSystem(ABC):

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def get_channel_name(self):
        pass

    def log(self):
        return f"[{self.get_channel_name()} sent to {self.recipient} : {self.message}]"

class Emailnotification(NotificationSystem):

        def send(self):
             return f"Email sent to {self.recipient} with message : {self.message}"
        
        def get_channel_name(self):
             return "Email"
        
class SmsNotification(NotificationSystem):
     def send(self):
          return f"SMS sent to {self.recipient} with message : {self.message}"
     
     def get_channel_name(self):
          return "SMS"
     
class PushNotification(NotificationSystem):
     def send(self):
          return f"Push notification sent to {self.recipient} with message : {self.message}"
     
     def get_channel_name(self):
          return "Push"
     

#Create Object :
notifications = [

        Emailnotification("sam@gmail.com", "Welcome to our service!"),
        SmsNotification("01234323451", "Your OTP is 69"),
        PushNotification("user_101", "Welcome to Push")

            ]

for notification in notifications:
     print(notification.send())
     print(notification.log())
     print("-" * 50)

# Try instantiating abstract class directly
try:
    n = NotificationSystem("Someone", "Hello")
except TypeError as e:
    print("\nError:")
    print(e)