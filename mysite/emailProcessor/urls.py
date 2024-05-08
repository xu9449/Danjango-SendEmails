from django.urls import path
from . import views
from . import show_form_view

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_click/', views.handle_click, name='handle_click'),
    path("show-form/", show_form_view.show_form, name = 'show_form'),
    path("baobo/", views.baobo, name="baobo"),
]
