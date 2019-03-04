from django.contrib import admin
from django.urls import path, include

from polls.api_urls import question_router


api_urlpatterns = [
    path('questions/', include(question_router.urls)),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/', include(api_urlpatterns)),
]
