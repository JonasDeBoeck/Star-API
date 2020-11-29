# api/urls.py

from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api import views

urlpatterns = [
    path('stars', views.StarsView.as_view()),
    path('stars/detailed', views.StarsDetailedView.as_view()),
    path('stars/<int:pk>', views.StarView.as_view()),
    path('stars/<int:pk>/detailed', views.StarDetailedView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('account/register', views.UserCreate.as_view()),
    path('api-token-auth', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
