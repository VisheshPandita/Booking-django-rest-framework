from django.urls import path
from .views import (
    GetAllEvents,
    PostEvent,
    GetEvent,
)

urlpatterns = [
    path('', GetAllEvents.as_view(), name='Events'),
    path('post/', PostEvent.as_view(), name='new event'),
    path('<slug>/', GetEvent.as_view(), name='show event'),
]