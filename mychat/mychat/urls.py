from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from chat.views import chat_room

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name='home'),
    path('', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)