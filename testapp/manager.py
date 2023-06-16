# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
#     use_in_migrations = True
    
#     def create_user(self, phone_number, password = None, **extra_fields):
#         if phone_number:
#             user = self.model(phone_number = phone_number, **extra_fields)
#             user.set_password(password)
#             user.save(using=self._db)
#             #return user
    
#             #raise ValueError('phone number is required')
#         else:
#             raise ValueError('phone number is required')
             
#     def create_superuser(self, phone_number, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
         
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Super user must have is_staff true')
        
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser true.')
        
        
#         return self.create_user(phone_number, password, **extra_fields)

from django.contrib.auth.base_user import BaseUserManager

# (BaseUserManager)
# BaseUserManager Django ka ek built-in class hai, jo django.contrib.auth.models module me define hota hai. 
# Ye class Django ke authentication system ke liye base manager provide karta hai.
# Iska use user objects ke create, retrieve aur manipulate karne ke liye kiya jata hai.

# BaseUserManager class me kuch important methods hote hai, jaise:--> 1. create_user  2. create_superuser


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, phone_number, password = None, **extra_fields):
        if not phone_number:
            raise ValueError('phone number is required')
        
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(phone_number, password, **extra_fields)