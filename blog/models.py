from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #models.Model indica q es modelo de django asi django sabe que debe guardarlo en la db
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)# foreingkeyrelacion con otro modelo
    title = models.CharField(max_length=200)#charfield definie un texto limitado
    text = models.TextField()#texto ilimitado
    created_date = models.DateTimeField(#fecha y hora
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title