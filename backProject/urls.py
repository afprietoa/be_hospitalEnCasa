"""backProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apiApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserRetrieveUpdateDeleteView.as_view()),
    path('medic/', views.MedicListCreateView.as_view()),
    path('medic/<int:pk>/', views.MedicRetrieveUpdateView.as_view()),
    path('nurse/', views.NurseListCreateView.as_view()),
    path('nurse/<int:pk>/', views.NurseRetrieveUpdateView.as_view()),
    path('auxiliar/', views.AuxiliarListCreateView.as_view()),
    path('auxiliar/<int:pk>/', views.AuxiliarRetrieveUpdateView.as_view()),
    path('patient/', views.PatientListCreateView.as_view()),
    path('patient/<int:pk>/', views.PatientRetrieveUpdateView.as_view()),
    path('familiar/', views.FamiliarListCreateView.as_view()),
    path('familiar/<int:pk>/', views.FamiliarRetrieveUpdateView.as_view()),

    path('medicPatient/', views.createMedicPatient), 
    path('medicPatient/<int:pk>/', views.detailMedicPatient),
    path('patientFamiliar/', views.createPatientFamiliar), 
    path('patientFamiliar/<int:pk>/', views.detailPatientFamiliar),

    path('clinicHistory/', views.ClinicHistoryCreateView.as_view()), 
    path('clinicHistory/<int:pk>/', views.ClinicHistoryRetrieveUpdateDestroyView.as_view()),

    # path('vitalSigns/', views.createVitalSigns), 
    # path('vitalSigns/<int:pk>/', views.detailVitalSigns),
    # path('suggestions/', views.createSuggestions), 
    # path('suggestions/<int:pk>/', views.detailSuggestions),

]