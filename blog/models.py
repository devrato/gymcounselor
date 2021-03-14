from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField


class Blog(models.Model):
    CATEGORY = [
        ('SPORT', 'SPORT'),
        ('MUSIC', 'MUSIC'),
        ('FOOD', 'FOOD'),
        ('FITNESS', 'FITNESS')
    ]

    blog_category = models.CharField(max_length=20, choices=CATEGORY)
    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog_image = models.ImageField(upload_to='blog_images')
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField()
    blog_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.blog_title)

    class Meta:
        db_table = 'table_blog'
        ordering = ['blog_datetime']

    @property
    def comment_count(self):
        return BlogComment.objects.filter(comment_blog_id=self.id).count()


class BlogComment(models.Model):
    comment_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=500)
    comment_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)

    class Meta:
        db_table = 'table_blog_comment'
