from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField(default=' ')
    img=models.ImageField(upload_to='post_img/',default="post_img/default.jpg")
    created=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    