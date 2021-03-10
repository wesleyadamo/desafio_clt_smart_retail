from django.urls import path

from hotel import views

urlpatterns = [
    path('cheapest/', views.CheapestHotel.as_view()),

]
