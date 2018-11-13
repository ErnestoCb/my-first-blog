from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, run, nombre, fecNac, fono, region, comuna, tipo, password=None):

        if not email:
            raise ValueError('Debes ingresar un mail de usuario')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            run=run,
            nombre=nombre,
            fecNac=fecNac,
            fono=fono,
            region=region,
            comuna=comuna,
            tipo=tipo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, run, nombre, fecNac, fono, region, comuna, tipo, password=None):

        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            run=run,
            nombre=nombre,
            fecNac=fecNac,
            fono=fono,
            region=region,
            comuna=comuna,
            tipo=tipo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#modelo de usuario para la creacion
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField('Username', unique=True, max_length=40)
    fecNac = models.DateField()
    run = models.CharField(max_length=9)
    fono = models.CharField('Phone Number', max_length=9)
    nombre = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    FECNAC_FIELD = 'fecNac'
    RUN_FIELD = 'run'
    NOMBRE_FIELD = 'nombre'
    FONO_FIELD = 'fono'
    REGION_FIELD = 'region'
    COMUNA_FIELD = 'comuna'
    TIPO_FIELD = 'tipo'
    REQUIRED_FIELDS = ['email','fecNac','run','nombre','fono','region','comuna','tipo']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_actived(self):
        "Is the user activated?"
        #Simplest possible answe: Yes or No
        return self.is_active