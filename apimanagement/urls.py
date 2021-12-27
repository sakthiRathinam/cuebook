from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('alert/', include('alertsystem.urls')),
    path('invoice/', include('invoicegenerator.urls')),
]
