from django.contrib.auth.models import BaseUserManager


class CustomerManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        if not kwargs['phone_number']:
            raise ValueError("phone_number must be set")

        if not kwargs['first_name']:
            raise ValueError("first_name must be set")

        if not kwargs['last_name']:
            raise ValueError("last_name must be set")

        if not kwargs['username']:
            raise ValueError("username must be set")

        user = self.model(phone_number=kwargs['phone_number'], email=self.normalize_email(kwargs['email']) if kwargs['email'] else None,
                          first_name=kwargs['first_name'], last_name=kwargs['last_name'], username=kwargs['username'])
        user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(phone_number=kwargs['phone_number'], first_name=kwargs['first_name'], last_name=kwargs['last_name'],
                            username=kwargs['username'], password=kwargs['password'], email=kwargs['email'])
        user.is_admin = True
        user.save(using=self._db)
        return user