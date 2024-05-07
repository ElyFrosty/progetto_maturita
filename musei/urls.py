from django.urls import path
from musei.views import homepage

app_name="musei"
urlpatterns = [
    path('/homepage', homepage, name='homepage')
]
