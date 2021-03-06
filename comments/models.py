from django.db import models
from posts.models import Post
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
  def filter_by_instance(self,instance):
    content_type = ContentType.objects.get_for_model(instance.__class__)
    obj_id = instance.id
    qs = super(CommentManager, self).filter(
        content_type=content_type, object_id=obj_id)
    return qs


# Create your models here.

class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
  instance = models.ForeignKey(Post,on_delete=models.CASCADE)
  parent = models.ForeignKey(
      "self", null=True, blank=True, on_delete=models.CASCADE)
  # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True)
  # object_id = models.PositiveIntegerField(null=True)
  # content_object = GenericForeignKey('content_type', 'object_id')
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = CommentManager()
  def __str__(self):
    return str(self.user.username)
  class Meta:
    ordering = ["-timestamp"]
  #replies
  def children(self):
    return Comment.objects.filter(parent=self)
  
  @property
  def is_parent(self):
    if self.parent is not None:
      return False
    return True
      
