from .models import User, UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def post_save_create_profile_reciever(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)

    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
            print("profile is not Axist")


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, "this user being save")
