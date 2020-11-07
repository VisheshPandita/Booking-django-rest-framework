from django.urls import path
from .views import (
    GetAllEvents,
    PostEvent,
    GetEvent,
    BookForEvent
)

urlpatterns = [
    path('', GetAllEvents.as_view(), name='Events'),
    path('post/', PostEvent.as_view(), name='new event'),
    path('book/<slug>', BookForEvent.as_view(), name='book event'),
    path('<slug>/', GetEvent.as_view(), name='show event'),
]