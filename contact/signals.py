from django.db.models.signals import post_migrate
from django.dispatch import receiver
from contact.models import Category

@receiver(post_migrate)
def insert_categories(sender, **kwargs):
    if sender.name == "contact":
        if not Category.objects.filter(name="Família").exists():
            Category.objects.create(name="Família")
        if not Category.objects.filter(name="Amigos").exists():
            Category.objects.create(name="Amigos")
        if not Category.objects.filter(name="Conhecidos").exists():
            Category.objects.create(name="Conhecidos")
