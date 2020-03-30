from django.contrib.contenttypes.models import ContentType
# from comments.models import Comment
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    username = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    
    image1 = models.ImageField(upload_to="images/",
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    image2 = models.ImageField(upload_to="images/",
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    image3 = models.ImageField(upload_to="images/",
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    image4 = models.ImageField(upload_to="images/",
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=False)
    
    

    
    def __str__(self):
      return self.title


    
    def get_absolute_url(self):
      return reverse('detail', kwargs={'slug': self.slug})



    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(
            instance.__class__,for_concrete_model=False)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    # if instance.content:
    #     html_string = instance.get_markdown()
    #     read_time_var = get_read_time(html_string)
    #     instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)

