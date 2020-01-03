from django.urls import path
from uploadapp import views

urlpatterns = [
     path('files/', views.FileUploadView.as_view(), name= 'files_list'),
]