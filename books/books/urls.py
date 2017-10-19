
from django.conf.urls import url
from django.contrib import admin
from books_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^new_book$', views.new_book, name='new_book'),
    url(r'^new_author$', views.new_author, name='new_author'),
    url(r'^new_category$', views.new_category, name='new_category'),
    url(r'^details/(?P<pk>[a-zA-Z]+)$', views.details, name='book_details'),
]