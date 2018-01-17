from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('^$',include('createticket.urls')),
    path('admin/', admin.site.urls),
    path('createticket', include('createticket.urls'))
]
