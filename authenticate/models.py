from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group


ROLE_CHOICES = [
    ('superadmin', 'Superadmin'),
    ('admin', 'Admin'),
    ('developer', 'Developer'),
    ('marketer', 'Marketer'),
    ('legal', 'Legal'),
]

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')
    groups = models.ManyToManyField(Group, related_name='custom_users')
    
    
    class Meta:
        permissions = [ 
            ('xyz', 'xyz'),
        ]
    
    
    def __str__(self):
        return self.username
    
class Blog(models.Model):
    title = models.CharField(max_length = 20)
    desc = models.TextField(max_length = 100)
    
    
    class Meta:
        permissions = [
            ('Can_view', 'user Can view blog post'),
            ('Can_add', 'user can add blog post'),
            ('can_change', 'user can change blog post'),
            ('Can_delete', 'user Can delete Blog Posts'),
            ('xyz', 'xyz')
        ]
    
    def __str__(self):
        return self.title
    
    
class product(models.Model):
    product_name = models.CharField(max_length = 20)
    product_type = models.CharField(max_length = 20)
    product_desc =  models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.product_name
    
    
    
    




