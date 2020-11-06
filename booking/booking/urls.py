from django.contrib import admin
from django.urls import path, include

from event import urls as eventURL
from user import urls as usersURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include(eventURL)),
    path('user/', include(usersURL)),
]
