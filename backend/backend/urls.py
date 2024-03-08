from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user_api.views import SongView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("api", SongView, basename='Songview')  # Change "api/" to "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', SongView.as_view({'get': 'list'}), name='root'),  # Provide the actions argument
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
