# from django.contrib.auth.models import User
# from .models import Profile
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @receiver(post_save,sender=User)

# # Le premier récepteur de signal create_profile crée automatiquement un Profile pour chaque nouvel utilisateur créé.
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(staff=instance)

# # Le second récepteur de signal save_profile sauvegarde le Profile chaque fois que le User est sauvegardé, pour assurer que toutes les modifications sont reflétées dans le profil associé.
# @receiver(post_save,sender=User)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


# Connecte la fonction manage_profile au signal post_save du modèle User. Cela signifie que manage_profile sera appelée chaque fois qu'un objet User est sauvegardé.
@receiver(post_save, sender=User)
def manage_profile(sender, instance, created, **kwargs):
    if created:
        # Créer le profil lorsqu'un nouvel utilisateur est créé
        Profile.objects.create(staff=instance)
    else:
        # Sauvegarder le profil lorsqu'un utilisateur existant est mis à jour
        if hasattr(instance, 'profile'):
            instance.profile.save()
        else:
            # Créer un profil si celui-ci n'existe pas (par mesure de sécurité)
            Profile.objects.create(staff=instance)


   