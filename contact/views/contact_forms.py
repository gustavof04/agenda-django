from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from contact.models import Contact

# Create your views here.
def create(request):
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )