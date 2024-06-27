# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# from django.contrib.auth.models import User 
from .models import User  # Assuming your custom User model is named CustomUser

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.get_or_create(user=instance)

