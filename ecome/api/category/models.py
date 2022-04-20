from django.db import models

class Category(models.Model):
    category_name = models.CharField( max_length=50,unique=True )
    description   = models.CharField( max_length=250 )
    created_at    = models.DateTimeField( auto_now_add=True )
    updated_at    = models.DateTimeField( auto_now=True )

    def __str__(self):
        return self.category_name
    
