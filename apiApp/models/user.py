from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# UserManager es una clase de django para realizar el proceso de autenticación
class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        
        user = self.create_user(
            username=username,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)  
    rol = models.CharField('Rol', max_length = 50)
    doc_type = models.CharField( 'Doc-Type', default='',max_length=50)
    doc_number = models.BigIntegerField(default=0, unique=True)
    first_name = models.CharField( 'First_Name', default='',max_length=50)
    last_name = models.CharField( 'Last_Name', default='', max_length=50)
    e_mail = models.EmailField('Email', max_length=100)
    cellphone = models.BigIntegerField(default=0)
    genre = models.CharField( 'Genre', default='',max_length=50)
    username = models.CharField('Username', max_length = 50, unique=True)
    password = models.CharField('Password', max_length = 256)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()

    USERNAME_FIELD = 'username'