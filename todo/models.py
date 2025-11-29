from django.db import models
from django.utils.text import slugify




class Task (models.Model):
    task_name = models.CharField (max_length=100,blank=False,null=False)
    task_slug = models.SlugField(max_length=100,blank=True,null=True)


    def save (self,*args,**kwargs):
        import random
        self.task_slug = slugify (f'{self.task_name}-{random.randint(0,999999)}')
        super().save(*args,**kwargs)

    def __str__ (self):
        return self.task_name
    
