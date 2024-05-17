from django.urls import path
from musei.views import homepage, museoDetailView, autoreDetailView

app_name="musei"
urlpatterns = [
    path('', homepage, name='homepage'),
    path('musei/<int:pk>', museoDetailView, name="dettagli_museo"),
    path('autori/<int:pk>', autoreDetailView, name="dettagli_autore"),
]
