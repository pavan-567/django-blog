from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from Posts.models import Post

# @receiver(pre_save, sender= Post)
# def add_profile(sender, instance, created, *args, **kwargs) : 
#     # if created: 
#     #     user_profile = Profile(user= instance)
#     #     user_profile.save()
#     #     user_profile.follows.set([instance.profilemodel.id])
#     if created : 
#         pass 
#     print(f"Profile Signal -> Sender : {sender}, Instance : {instance}, Created : {created}")