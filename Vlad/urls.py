from django.urls import path
from .views import VladExelAPIView

urlpatterns = [
    path('exel-vlad/', VladExelAPIView.as_view(), name='vladexelview'),
]


