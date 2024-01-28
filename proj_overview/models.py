from django.db import models

# Create your models here.
# This is DB info for make single article
class ArticleInfo(models.Model):
    status = models.CharField(max_length=50)
    project_start_date=models.DateField(blank=True,null=True)
    project_finish_date=models.DateField(blank=True,null=True)
    title = models.CharField(max_length=50)
    article = models.TextField()
    img_path_1 = models.CharField(max_length=500,blank=True,null=True)
    title2 = models.CharField(max_length=50,blank=True,null=True)
    article2 = models.TextField()
