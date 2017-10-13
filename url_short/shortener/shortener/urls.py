
from django.conf.urls import url
from django.contrib import admin
from shortener_app.views import redirect,HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^hash/(?P<short_url>[\w-]+)$', redirect),
]
