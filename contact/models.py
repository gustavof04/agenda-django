from django.db import models
from django.utils import timezone

# Criar os fields da model Contact
# id (primary key - cria automático pelo django)
# first_name (string - CharField 50char), last_name (string - CharField 50char), phone (string - Charfield 50char)
# email (email - EmailField 254char), created_date (date - DateTimeField(default=timezone.now)), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)