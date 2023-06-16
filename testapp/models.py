from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
#import uuid

# (AbstractUser)

# Django me, AbstractUser ek pre-defined model class hai, jo Django ka django.contrib.auth app ke andar define kiya gaya hai.
# AbstractUser Django's default User model ko extend karne ke liye istemal hota hai.

# AbstractUser class AbstractBaseUser class aur PermissionsMixin class se inherit hoti hai. Isse, AbstractUser model ke 
# instances standard user-related fields aur functionalities hote hain, jaise ki username, password, email, first name,
# last name, etc.


class Phone(AbstractUser):
    #uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    phone_number = models.CharField(max_length=12, unique = True)
    number_varified = models.BooleanField(default = False)
    otp = models.CharField(max_length=6)
    
        
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self):
        return self.phone_number
    #def get_username(self):
     #   return self.phone_number
    
    


