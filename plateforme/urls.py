
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("avis/", include("avis.urls")),
    path("events/", include("events.urls")),
    path("notifications/", include("notifications.urls")),
]
    