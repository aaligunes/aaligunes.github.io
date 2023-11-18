import requests
from django.http import HttpResponse

class themoviedb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        
        
    def getpopulers(self,sayfa_numarasi):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=tr&page={sayfa_numarasi}")  
        movies = response.json()

        movie_data = []
        page = movies['page']
        for movie in movies['results']:
            movie_id = movie['id']
            title = movie['title']
            backdrop_path = "https://image.tmdb.org/t/p/w500"+movie['poster_path']  
            original_language = movie['original_language']
            overview = movie['overview']
            popularity = movie['popularity']
            
            
            movie_info = {
                'title': title,
                'overview': overview,
                'backdrop_path': backdrop_path,
                'original_language': original_language,
                'movie_id':movie_id,
                'popularity':popularity,
                'page':page,
            }
            
            movie_data.append(movie_info)
            
        return movie_data
    
    
    def up_coming(self):
        response = requests.get(f"{self.api_url}movie/upcoming?api_key={self.api_key}&language=tr&page=1")  
        movies = response.json()
        
        
        movie_data = []
        for movie in movies['results']:
            movie_id = movie['id']
            title = movie['title']
            backdrop_path = "https://image.tmdb.org/t/p/w500"+movie['poster_path']  
            original_language = movie['original_language']
            overview = movie['overview']
            popularity = movie['popularity']
            page = movies['page']
            
            movie_info = {
                'title': title,
                'overview': overview,
                'backdrop_path': backdrop_path,
                'original_language': original_language,
                'movie_id':movie_id,
                'popularity':popularity,
                'page':page,
            }
            movie_data.append(movie_info)
            
        return movie_data
        
    def listeler(request):
        api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        api_url = "https://api.themoviedb.org/3/genre/movie/"
        url = "https://api.themoviedb.org/3/genre/movie/list?api_key=d92a9b519f4d2edba5ae1b46806a07c6&language=tr"
        response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=d92a9b519f4d2edba5ae1b46806a07c6&language=tr")
        
        
        
        lists=response.json()
        
        list_data=[]
        for list in lists['genres']:
            list_id=list['id']
            list_name=list['name']
            
            list_info = {
                'list_id':list_id,
                'list_name':list_name
            }
            list_data.append(list_info)
        return list_data
    def liste_ayrinti(request,list_id):
        url = f"https://api.themoviedb.org/3/list/{list_id}?api_key=d92a9b519f4d2edba5ae1b46806a07c6&language=tr"
        response = requests.get(url)
        list_detay = response.json()
        
        list_detay_data = []
        
        for listdetay in list_detay['items']:
            title = listdetay['title']
            
            overview = listdetay['overview']
            if(listdetay['backdrop_path']):
                backdrop_path = "https://image.tmdb.org/t/p/w500"+listdetay['backdrop_path']
            else:
                backdrop_path = "https://image.tmdb.org/t/p/w500"
            
            
            film_id = listdetay['id']
            
            listdetay_info = {
                'title':title,
                'overview':overview,
                'backdrop_path':backdrop_path,
                'film_id':film_id
            }
            list_detay_data.append(listdetay_info)
        
        return list_detay_data
            
    def film_video(request,movie_id):
        api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        api_url = "https://api.themoviedb.org/3/movie/"
        response = requests.get(f"{api_url}{movie_id}/videos?api_key={api_key}&language=tr")
        response1 = requests.get(f"{api_url}{movie_id}/videos?api_key={api_key}&language=en")
        
        detaylar = response.json()
        detaylar1 = response1.json()
        movie_data = []
        key =""
        for detay in detaylar['results']:
            key = detay['key']
            
        if key == "":
            for detay in detaylar1['results']:
                key = detay['key']
            
        
        return key
        
        
    def film_detail(request,movie_id):
        api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        api_url = "https://api.themoviedb.org/3/movie/"
        response = requests.get(f"{api_url}{movie_id}?api_key={api_key}&language=tr")
        movie = response.json()
        movie_data = []
        movie_id = movie_id
        title = movie['title']
        overview = movie['overview']
        if(movie['poster_path']):
                backdrop_path = "https://image.tmdb.org/t/p/w500"+movie['poster_path']
        else:
                backdrop_path = "https://image.tmdb.org/t/p/w500"
        popularity = movie['popularity']   
        release_date = movie['release_date']
        revenue = movie['revenue']
        vote_average = movie['vote_average']
        budget = movie['budget']
        movie_info = {
            'title':title,
            'overview': overview,
            'backdrop_path': backdrop_path,
            'popularity':popularity,
            'release_date':release_date,
            'revenue':revenue,
            'vote_average':vote_average,
            'budget':budget,
            'movie_id':movie_id
            
            }
        return movie_info

        
        
        
    
    
    def search_movie(self,film_adi):
        api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        api_url = "https://api.themoviedb.org/3/"        
        url1 = requests.get(f"https://api.themoviedb.org/3/search/movie?query={film_adi}&api_key={api_key}&include_adult=false&language=tr&page=1")        
        response = url1.json()
        
        movie_data = []
        for movie in response['results']:
            movie_id = movie['id']
            title = movie['title']
            if(movie['poster_path']):
                backdrop_path = "https://image.tmdb.org/t/p/w500"+movie['poster_path']
            else:
                backdrop_path = "https://image.tmdb.org/t/p/w500"

            original_language = movie['original_language']
            overview = movie['overview']
            popularity = movie['popularity']
                       
            movie_info = {
                'title': title,
                'overview': overview,
                'backdrop_path':backdrop_path,
                'original_language': original_language,
                'id':movie_id,
                'popularity':popularity,              
            }
            movie_data.append(movie_info)           
        return movie_data
    
    
    
    def now_playing(self):
        api_key = "d92a9b519f4d2edba5ae1b46806a07c6"
        api_url = "https://api.themoviedb.org/3/"  
        
        response = requests.get(f"{self.api_url}movie/now_playing?api_key={self.api_key}&language=tr&page=1")  
        movies = response.json()
        
        movie_data = []
        for movie in movies['results']:
            movie_id = movie['id']
            title = movie['title']
            backdrop_path = "https://image.tmdb.org/t/p/w500"+movie['poster_path']  
            original_language = movie['original_language']
            overview = movie['overview']
            popularity = movie['popularity']
            page = movies['page']
            
            movie_info = {
                'title': title,
                'overview': overview,
                'backdrop_path': backdrop_path,
                'original_language': original_language,
                'movie_id':movie_id,
                'popularity':popularity,
                'page':page,
            }
            movie_data.append(movie_info)
            
        return movie_data
    
        
            
       
    
    





        
        
    
