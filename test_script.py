from accounts.models import CustomUser
user = CustomUser.objects.filter(id=2).first()
print(user.username)
