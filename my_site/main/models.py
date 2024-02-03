from django.db import models

# Create your models 
class Data(models.Model):
     name = models.CharField('Имя:',max_length=100),
     username = models.CharField('Фамилия:',max_length=100),
     age =  models.CharField('Возрасть:',max_length=100),
     jop =  models.CharField('Професия:',max_length=100),
     date = models.DateTimeField('Дата публикаций')
     def __str__(self):
         return self.name
     class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


     

  
