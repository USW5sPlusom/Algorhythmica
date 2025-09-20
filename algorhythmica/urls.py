from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("core.urls")),
    path('lo/', include("logika.urls")),
    path('al/', include("algorithms.urls")),
    path('admin/', admin.site.urls),
]
