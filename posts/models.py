from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/',max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=20) 
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()

    def __str__(self):
        return self.title