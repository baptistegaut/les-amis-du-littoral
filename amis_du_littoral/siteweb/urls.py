from django.urls import path
from . import views

urlpatterns = [
    path('bulletins/<str:numero>/', views.bulletin),
    path('', views.association),
    path('association/', views.association),
    path('bureau/', views.bureau),
    path('histoire/', views.histoire),
    path('preoccupations/', views.preoccupations),
    path('avenir/', views.avenir),
    path('participations/', views.participations),
    path('bulletins/', views.bulletins),
    path('contact/', views.contact),
    path('rejoindreladl/',views.rejoigneznous),
    path('documents/', views.documents),
    path('documents/lddl/',views.lddl),
    path('documents/abp/', views.abp)
]