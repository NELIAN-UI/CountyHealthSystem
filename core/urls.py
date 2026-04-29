from django.urls import path
from . import views
from .views import PatientLoginView

urlpatterns = [
    path('', views.entrance, name='entrance'),
    path('login/', PatientLoginView.as_view(), name='patient_login'),
    path('profile/', views.patient_profile, name='patient_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('register/', views.register_patient, name='register_patient'), # This matches the function we just added
    path('counties/', views.county_selection, name='county_selection'),
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('appointments/', views.book_appointment, name='book_appointment'),
]
