from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.
from films.models import FilmBrief

def genres(request):
	pass
def category_movies(request):
	if request.method == 'GET':
		type = request.GET.get('category')
		data = []
		movies = FilmBrief.object.filter(category=type)
		for movie in movies:
			detail = movie.filmdetail_set.all()[0]
			info = [movie.id, detail.cover_url, movie.c_name, movie.release_time, detail.rating]
			data.append(info)
		return render()