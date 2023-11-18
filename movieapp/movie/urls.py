from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home1),
    path("home/<int:sayfa_numarasi>",views.home,name="home"),
    path("filmrobotu", views.filmrobotu, name = "filmrobotu"),
    path("film_details/<int:movie_id>", views.film_detail, name="film_detail"),
    #path("movies", views.populer_movies)
    path("deneme", views.deneme,name="deneme"),
    path("search_film/", views.search_film, name = "search_film"),
    path("category_detail/<int:list_id>", views.category_detail, name="category_detail"),
    path('favori-ekle/<int:movie_id>/', views.add_favorite, name='add_favorite'),
    path('favori-cikar/<int:movie_id>/', views.remove_favorite, name='remove_favorite'),
    path("account_detail", views.account_detail,name="account_detail"),
    path("account_favori_film", views.account_favori_film,name="account_favori_film"),
    path("account_yorum_yapilan_filmler", views.account_yorum_yapilan_filmler,name="account_yorum_yapilan_filmler"),
    path("account_sifre_degistirme,",views.sifre_degistir,name = "sifre_degistir"),
    
    
    
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    