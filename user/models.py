from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # on_delete=models.CASCADE signifie que si un utilisateur (User) est supprimé, le profil (Profile) correspondant sera également supprimé.
    staff=models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(default='default.webp',upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-profile'
    


# Create your models here.
