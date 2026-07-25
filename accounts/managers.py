from django.contrib.auth.models import BaseUserManager


class CustomerManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, username,password, email= None):
        if not phone_number:
            raise ValueError("phone_number must be set")

        if not first_name:
            raise ValueError("first_name must be set")

        if not last_name:
            raise ValueError("last_name must be set")

        if not username:
            raise ValueError("username must be set")

        user = self.model(phone_number=phone_number, email=self.normalize_email(email) if email else None,
                          first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, username,password, email= None):
        user = self.create_user(phone_number=phone_number, first_name=first_name, last_name=last_name,
                            username=username, password=password, email=email)
        user.is_admin = True
        user.save(using=self._db)
        return user