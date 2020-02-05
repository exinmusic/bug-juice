from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from reports.models import Project

# MODELS
# Profile - The Parent most model.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    avatar = models.URLField(max_length=250)

    def __str__(self):
        return self.user.username

# SIGNALS
# User created -> create Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kargs):
    if created:
        Profile.objects.create(user=instance)

# User saved -> save Profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kargs):
    instance.profile.save()

# Profile deleted -> delete User
@receiver(post_delete, sender=Profile)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: # if user is not specified
        instance.user.delete()