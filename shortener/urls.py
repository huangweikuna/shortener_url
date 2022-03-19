from django.urls import path, re_path

from shortener import views

urlpatterns = [
    path('newurl', views.new_url),
    re_path(r'^(?P<code>[a-zA-Z0-9]{9})$', views.redirect),
]
