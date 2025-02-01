import getpass

from django.core.management import BaseCommand

from users.models import User

#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         user = User.objects.create(email="admin@example.com")
#         # user = User.objects.create_user(email="admin@example.com", password="123456")
#         user.set_password("123")
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # username = input("Enter superuser username: ")
        email = input("Enter superuser email: ")

        psw1 = getpass.getpass("Enter password: ")
        psw2 = getpass.getpass("Confirm password: ")

        while psw1 != psw2 or not psw1:
            print("Passwords didn't match or empty!")
            psw1 = getpass.getpass("Enter password: ")
            psw2 = getpass.getpass("Confirm password: ")

        user = User.objects.create(
            # username=username,
            email=email,
            first_name="Admin",
            last_name="MyMailings",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(psw1)
        user.save()
