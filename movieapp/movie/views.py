from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from movie.api import themoviedb
from movie.openai import openaisor
from movie.models import yorumlar, favori_filmler
from django.contrib.auth.models import User
import random
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


def add_favorite(request, movie_id):
    if request.user.is_authenticated:
        kullanici_adi = request.user.username
        favori_ornegi = favori_filmler(favori_button=1, favoriye_eklenen_film_id=movie_id, favoriye_ekleyen_kullanici_adi=kullanici_adi)
        favori_ornegi.save()

    # Redirect to the film detail page after adding to favorites
    return redirect(reverse('film_detail', kwargs={'movie_id': movie_id}))

def remove_favorite(request, movie_id):
    if request.user.is_authenticated:
        kullanici_adi = request.user.username
        favori_filmler.objects.filter(favoriye_eklenen_film_id=movie_id, favoriye_ekleyen_kullanici_adi=kullanici_adi).delete()

    # Redirect to the film detail page after removing from favorites
    return redirect(reverse('film_detail', kwargs={'movie_id': movie_id}))




def home1(request):
    movie_api = themoviedb()
    sayfa_numaralari = range(1, 11)
    
    context = {
        "populer_movies":movie_api.getpopulers(1),
        "up_coming_movies": movie_api.up_coming(),
        "now_playing_movies": movie_api.now_playing(),
        'sayfa_numaralari': sayfa_numaralari,
        'listeler':movie_api.listeler()
        
        
    }
   # movie_titles = movie_api.deneme()
    return render(request, "movie/home.html", context)

def home(request,sayfa_numarasi):
    movie_api = themoviedb()
    sayfa_numaralari = range(1, 11)
    
    context = {
        "populer_movies":movie_api.getpopulers(sayfa_numarasi),
        "up_coming_movies": movie_api.up_coming(),
        "now_playing_movies": movie_api.now_playing(),
        'sayfa_numaralari': sayfa_numaralari,
        'listeler':movie_api.listeler()
        
        
    }
   # movie_titles = movie_api.deneme()
    return render(request, "movie/home.html", context)

def filmrobotu(request):
    openaisor_api = openaisor()
    movie_api = themoviedb() 
    rastgele_puan = random.randint(1,10)
    rastgele_resim = str(random.randint(1,8))
    resim = "static\movie/img/robot_resim_" + str(rastgele_resim) + ".jpg"
    #C:\Users\malig\Desktop\my-movie-site\movieapp\movie\static\movie\img\robot_resim_1.jpg
   
    
    
    if request.method == "POST":
        kategori1 = request.POST.get("kategori1")
        kategori2 = request.POST.get("kategori2")
        kategori3 = request.POST.get("kategori3")
        puan1 = request.POST.get("puan1")
        puan2 = request.POST.get("puan2")
        puan3 = request.POST.get("puan3")
        
        cevap = openaisor_api.soru(kategori1,kategori2,kategori3,puan1,puan2,puan3)
    else:
        kategori1 = ""
        kategori2 = ""
        kategori3 = ""
        puan1 = ""
        puan2 = ""
        puan3 = ""
        cevap = "Film Verileri Bekleniyor"
    
    film_info = movie_api.search_movie(cevap)
        
    
    context = {
        #"sorusor":openaisor_api.soru(kategori1,kategori2,puan1,puan2)
        "kategori1":kategori1,
        "kategori2":kategori2,
        "kategori3":kategori3,
        "puan1":puan1,
        "puan2":puan2,
        "puan3":puan3,
        "rastgele_puan":rastgele_puan,
        "rastgele_resim":resim,
        
        
        
        "cevap":cevap,
        "aranan_film":film_info,
        "now_playing_movies": movie_api.now_playing(),
        "up_coming_movies": movie_api.up_coming(),
        
        'listeler':movie_api.listeler()
        
        
    }
    
    return render(request, "movie/filmrobotu.html", context)

def film_detail(request,movie_id):
    movie_api = themoviedb()
    movie_idd = movie_id 
    if request.user.is_authenticated:
        kullanici_adi = request.user.username
    else:
        kullanici_adi = None 
        
    is_favori = favori_filmler.objects.filter(favoriye_eklenen_film_id=movie_id, favoriye_ekleyen_kullanici_adi=kullanici_adi).exists()
    
    
    if request.user.is_authenticated:
        if request.method == "POST":
            yorum_basligi = request.POST.get("yorum_basligi")
            yorum = request.POST.get("yorum")
            yorum_yapilan_film_id = movie_id
            yorum_yapan_kullanici_adi = kullanici_adi
            yorumlar_ornegi = yorumlar(yorum_basligi=yorum_basligi, yorum=yorum, yorum_yapilan_film_id=yorum_yapilan_film_id, yorum_yapan_kullanici_adi=yorum_yapan_kullanici_adi)
            
            if yorum == "":
                context1 = {
                    "yorumlar":yorumlar.objects.all(),      
                    "movie_id":movie_id,      
                    "film_detail":movie_api.film_detail(movie_id), 
                    'film_video':movie_api.film_video(movie_id),    
                    "up_coming_movies": movie_api.up_coming(), 
                    'listeler':movie_api.listeler(),
                    'kullanici_adi':kullanici_adi,
                    'favori_filmler':favori_filmler.objects.all(),
                    'is_favori':is_favori,
                    'error':"Boş Yorum Girmeyiniz"
                }
                return render(request, "movie/film-detail.html",context1)
                
            else:
                yorumlar_ornegi.save()
    
    
    
    
    
    if request.user.is_authenticated:
        if request.method == "POST1":
            favoriye_ekleyen_kullanici_adi = kullanici_adi
            favoriye_eklenen_film_id = movie_id
            favori_buton = 1
            favori_ornegi = favori_filmler(favori_button=favori_buton, favoriye_eklenen_film_id=favoriye_eklenen_film_id, favoriye_ekleyen_kullanici_adi=favoriye_ekleyen_kullanici_adi)
            favori_ornegi.save()
            
            
    
    
    context = {
        "yorumlar":yorumlar.objects.all(),      
        "movie_id":movie_id,      
        "film_detail":movie_api.film_detail(movie_id), 
        'film_video':movie_api.film_video(movie_id),    
        "up_coming_movies": movie_api.up_coming(), 
        'listeler':movie_api.listeler(),
        'kullanici_adi':kullanici_adi,
        'favori_filmler':favori_filmler.objects.all(),
        'is_favori':is_favori,
        
        
        
    }
    return render(request, "movie/film-detail.html",context)
def category_detail(request,list_id):
    movie_api = themoviedb()
    listeler = movie_api.listeler()
    kategori_ismi = ""
    for kategori_ismi_dongu in listeler:
        if list_id == kategori_ismi_dongu['list_id']:
            kategori_ismi = kategori_ismi_dongu['list_name']
            
    context = {
        "kategori_detay":movie_api.liste_ayrinti(list_id),
        'listeler':movie_api.listeler(),
        'kategori_ismi':kategori_ismi,
        "up_coming_movies": movie_api.up_coming(),
        
        
    }
    
    
    return render(request,"movie/category-details.html",context)













def deneme(request):
    return render(request, "movie/deneme.html")

def search_film(request):
    if request.method =='POST':
        film_adi = request.POST.get('film_adi','')
        
    movie_api = themoviedb() 
    film_info = movie_api.search_movie(film_adi)   
    
    context = {
        'aranan_film':film_info,
        'listeler':movie_api.listeler(),       
        
    }
    
    return render(request,"movie/search_film.html",context)
    

def account_detail(request):
    movie_api = themoviedb()
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")  
        eski_password = request.POST.get("eski_password")
        yeni_password = request.POST.get("yeni_password")
        yeni_password_tekrar = request.POST.get("yeni_repassword_tekrar")
        
        
        if yeni_password == yeni_password_tekrar:
            user_to_update = User.objects.get(username=username)
            if check_password(eski_password, user_to_update.password):
                user_to_update.first_name = firstname
                user_to_update.last_name = lastname
                user_to_update.set_password(yeni_password)  # Şifreyi güvenli bir şekilde güncellemek için set_password kullanın
                user_to_update.save()
            else:
                return render(request, "movie/account_detail.html", {"error": "Lütfen Bilgileri Doğru Giriniz. Eski şifreler uyuşmuyor"})
            
        else:
            return render(request, "movie/account_detail.html", {"error": "Lütfen Bilgileri Doğru Giriniz.yeni şifreler uyuşmuyor"})
            
    
    context = {
        
        'listeler':movie_api.listeler(),       
    }   
    return render(request, "movie/account_detail.html",context)

def account_favori_film(request):
    movie_api = themoviedb()
    favoriye_eklenen_filmler = favori_filmler.objects.all()
    movie_bilgiler = []
    listeler = movie_api.listeler()
       
    for favori_film in favoriye_eklenen_filmler:
        if request.user.username == favori_film.favoriye_ekleyen_kullanici_adi:
            film_detay = movie_api.film_detail(favori_film.favoriye_eklenen_film_id)
            title = film_detay['title']
            overview=film_detay['overview']
            backdrop_path=film_detay['backdrop_path']
            movie_id=film_detay['movie_id']
            movie_info = {
                'title':title,
                'overview':overview,
                'backdrop_path':backdrop_path,
                'movie_id':movie_id,
            }
            movie_bilgiler.append(movie_info)                                               
    context = {
        'aranan_filmler':movie_bilgiler,
        'favoriye_eklenen_filmler':favoriye_eklenen_filmler,
        'listeler':movie_api.listeler(),       
    }
    return render(request,"movie/account_favori_film.html",context)

def account_yorum_yapilan_filmler(request):
    movie_api = themoviedb()
    yorum_yapilan_filmler = yorumlar.objects.all()
    movie_bilgiler = []
    
    for yorum_yapilan_film in yorum_yapilan_filmler:
        if request.user.username == yorum_yapilan_film.yorum_yapan_kullanici_adi:
            film_detay = movie_api.film_detail(yorum_yapilan_film.yorum_yapilan_film_id)
            yapilan_yorum = yorum_yapilan_film.yorum
            title = film_detay['title']
            overview=film_detay['overview']
            backdrop_path=film_detay['backdrop_path']
            movie_id=film_detay['movie_id']
            movie_info = {
                'title':title,
                'overview':overview,
                'backdrop_path':backdrop_path,
                'movie_id':movie_id,
                'yorum':yapilan_yorum,
            }
            movie_bilgiler.append(movie_info) 
    context = {
        'aranan_filmler':movie_bilgiler,
        'yorum_yapilan_tum_filmler':yorum_yapilan_filmler,
        'listeler':movie_api.listeler(),       
        
        
    }
    return render(request,"movie/account_yorum_yapilan_filmler.html",context)

def sifre_degistir(request):
    movie_api = themoviedb()
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        yeni_sifre = request.POST.get("password")
        yeni_sifre_tekrar = request.POST.get("repassword")
        try:
            user_to_update = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return render(request, "movie/account_sifre_degistir.html", {"error": "Kullanıcı bulunamadı"})
        
        
        
        if user_to_update.email == email and yeni_sifre == yeni_sifre_tekrar :
            user_to_update.set_password(yeni_sifre)
            return render(request,"movie/account_sifre_degistir.html",{"error":"Şifre Değiştirildi Giriş Yapabilirsiniz."})
        else:
            return render(request,"movie/account_sifre_degistir.html",{"error":"Tekrar Deneyiniz"})
    
    context = {
        'listeler':movie_api.listeler(),  
         
        
    }   
    return render(request,"movie/account_sifre_degistir.html",context)