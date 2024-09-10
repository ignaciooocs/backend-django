from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('luckyApp/', include('luckyApp.urls')),
    path('paparazziApp/', include('paparazziApp.urls'))
]
