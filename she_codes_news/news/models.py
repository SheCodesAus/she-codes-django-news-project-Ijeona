from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class NewsStory(models.Model):
    class Meta:
        ordering =['-pub_date'] 
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url_field = models.URLField(max_length=200, null=True)

    def get_absolute_url(self):
     return reverse('news:story',kwargs={'pk': self.pk})