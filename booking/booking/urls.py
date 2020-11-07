from django.contrib import admin
from django.urls import path, include

from event import urls as eventURL
from user import urls as usersURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include(eventURL)),
    path('user/', include(usersURL)),
]
