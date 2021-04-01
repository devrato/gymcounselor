from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField


class Workout(models.Model):
    CATEGORY = [
        ('CARDIO', 'CARDIO'),
        ('YOGA', 'YOGA'),
    ]

    video_category = models.CharField(max_length=20, choices=CATEGORY)
    video_image = models.ImageField(upload_to='workout/images')
    video_title = models.CharField(max_length=255)
    video_desc = models.TextField()
    video_link = models.URLField(max_length = 200)
    upload_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.video_title)

    class Meta:
        db_table = 'table_videos'
        ordering = ['upload_datetime']

    # @property
    # def comment_count(self):
    #     return WorkoutComment.objects.filter(comment_blog_id=self.id).count()


# class WorkoutComment(models.Model):
#     comment_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
#     comment_user = models.EmailField()
#     comment = models.TextField(max_length=500)
#     comment_datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.comment)

#     class Meta:
#         db_table = 'table_video_comment'
