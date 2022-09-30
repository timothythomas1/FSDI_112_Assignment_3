from django.db import models
from django.urls import reverse

# The Object–relational mapping (ORM) model for Django is database agnostic. We can reconfigure the database later on
# The relationship between Post and Model is that of child and parent
class Post(models.Model): # This class Post class extends the Model class with additional methods and attributes
    # Class attributes that happen to be objects
    title = models.CharField(max_length=256) # A column that will be created in the SQL
    subtitle = models.CharField(max_length=256) # A column that will be created in the SQL
    body = models.TextField() # A column that will be created in the SQL
    created_on = models.DateTimeField(auto_now_add=True) # A column that will be created in the SQL

    # This was created to modify the behavior of the str() in the admin panel after launching server. Converts the 'Posts object' to the title
    def __str__(self): 
        return self.title
    
    # This allows us to redirect ('reverse') to detail pages once we click 'Create' a new post
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

# Create a Migration, which is a python script to connect the database using:
# python3 manage.py makemigrations post

# To run the migration: 
# python3 manage.py migrate
















