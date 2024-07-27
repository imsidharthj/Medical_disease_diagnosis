from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.patient_data, name='patient_data'),
]
