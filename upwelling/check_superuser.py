from django.contrib.auth.models import User

superusers = User.objects.filter(is_superuser=True)

for superuser in superusers:
    print(superuser.username)
    print(superuser.email)
    print(superuser.first_name)
    print(superuser.last_name)