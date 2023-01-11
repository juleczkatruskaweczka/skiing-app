from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
import  datetime
from datetime import timedelta,datetime
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError("Musisz podać adres email")
        if not username:
            raise ValueError("Musisz podać nazwę instruktora")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.is_admin = True
        user.is_free = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_free = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class user(AbstractBaseUser):
    username = models.CharField(max_length=32,unique=False)
    email = models.EmailField(max_length=264,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_free = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    def  __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
class event(models.Model):
    name = models.CharField(max_length=200)
    data = models.DateTimeField()
    dlugosc = models.IntegerField(null=True,blank=True)
    instruktor = models.ManyToManyField(user,null=True,blank=True)
    trwa = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)
    def date(self):
        return self.data.isoformat(" ")
    def koniec(self):
        koniec = self.data+timedelta(minutes=self.dlugosc or 0)
        now = datetime.now() + timedelta(hours=1)
        if now<koniec and now>self.data:
            self.trwa = True
            self.save()
            return 1
        else:
            self.trwa = False
            self.save()
            return 0


class Tracks(models.Model):
    name = models.CharField(max_length=100)
    LEVEL_OF_DIFFICULTY = [
        ('łatwą', 'Łatwy'),
        ('średnio-zaawansowaną', 'Średnio-zaawansowany'),
        ('trudną', 'Zaawansowany'),
    ]
    level = models.CharField(
        max_length=80,
        choices=LEVEL_OF_DIFFICULTY,
        default='łatwą',
    )
    length = models.CharField(max_length=100, default="1000 km")
    temperature = models.CharField(
        max_length=80,
        default='dla wszystkich',
        choices=[('dla wszystkich', 'Dla wszystkich'),
                 ('< 10 °C', '< 10 °C'),
                 ('< 0 °C', '< 0 °C'),
                 ('< -5 °C', '< -5 °C')],
    )
    weather = MultiSelectField(
        default='dla wszystkich',
        choices=[('słonecznie', 'Słonecznie'),
                 ('pochmurnie', 'Pochmurnie'),
                 ('zamieć', 'Zamieć')],
        max_length=80,
    )
    wind = models.CharField(
        default='dla wszystkich',
        max_length=80,
        choices=[('dla wszystkich', 'Dla wszystkich'),
                 ('< 50 km/h', '< 50 km/h'),
                 ('< 25 km/h', '< 25 km/h'),
                 ('< 5 km/h', '< 5 km/h')],
    )
    isopened = models.CharField(
        default='weather',
        max_length=80,
        choices=[('weather', 'Zalezna od pogody'),
                 ('Otwarta', 'Otwarta'),
                 ('Zamknięta', 'Zamknięta'), ]
    )

    def __str__(self):
        return self.name