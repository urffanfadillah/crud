from django.urls import path

from .views import Create, Update, Delete

app_name        = 'core'
urlpatterns     = [
    path('create/', Create.as_view(), name='create'),
    path('update/<int:id>/', Update.as_view(), name='update'),
    path('delete/<int:id>/', Delete.as_view(), name='delete'),
]