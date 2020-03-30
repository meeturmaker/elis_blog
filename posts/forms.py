from django.forms import ModelForm
from .models import Post

# Create the form class.


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content',
                  'image1', 'image2', 'image3', 'image4', 'publish_date', 'draft']


# Creating a form to add an article.

# Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)
