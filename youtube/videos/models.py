from django.db import models 
from django.contrib.auth.models import User 
# from .imagekit_client import get_streaming_url 


# Create your models here.

class Video(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='videos')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    file_id = models.CharField(max_length=100)
    thumbnail_file_id = models.CharField(max_length=100)
    video_url = models.URLField(max_length=100)
    thumbnail_url = models.URLField(max_length=100) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    streaming_url = models.URLField(max_length=200 , blank= True , null=True)

    class Meta:
        ordering = ['-created_at']

    # @property
    # def streaming_url(self):
    #     return get_streaming_url(self.video) 
    
    def __str__(self):
        return self.title 
    
class VideoLike(models.Model):
    LIKE = 1
    DISLIKE = -1


    LIKE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="user_likes")

    value = models.SmallIntegerField(choices=LIKE_CHOICES)

    class Meta:
        unique_together = ['user', 'video']

    def __str__(self):
        action = ''
        if self.value == self.LIKE: 
            action = 'liked'
        else:
            action = 'disliked'
        return f"{self.user.username} {action} {self.video.title}"







