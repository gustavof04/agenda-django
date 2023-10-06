from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # contact (crud)
    path('contact/<int:contact_id>/', views.contact, name='contact'), # read
    path('contact/create/', views.create, name='create'), # create
    path('contact/<int:contact_id>/update/', views.update, name='update'), # update
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # delete
]