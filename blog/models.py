from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_ext(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.png','.jpg','.jpeg']
    if not ext.lower() in valid_ext:
        raise ValidationError('unvalid ext')

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=False,blank=False, validators=[validate_file_ext])
    descripion = models.CharField(max_length=512, null=False,blank=False)

class article(models.Model):
    title = models.CharField(max_length=512,null=False,blank=False)
    cover = models.FileField(upload_to='files/articles_covers/',null=False,blank=False, validators=[validate_file_ext])
    content = RichTextField()
    creat_at = models.DateTimeField(default=datetime.now)
    categury = models.ForeignKey('Categury', on_delete=models.CASCADE)
    author = models.OneToOneField(userprofile,on_delete=models.CASCADE)

class Categury (models.Model):
    title = models.CharField(max_length=128,blank=False,null=False)
    cover = models.FileField(upload_to='files/categury_covers/',blank=False,null=False, validators=[validate_file_ext])

    def __str__(self):
        return self.title

