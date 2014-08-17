from django.shortcuts import render_to_response, redirect
from django.http.response import Http404
from film.models import Film, Film_comment
from django.core.exceptions import ObjectDoesNotExist
# from film.forms import
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from film.forms import FilmForm, Film_comment_Form
import datetime

# Create your views here.

def films(request, page_number=1):
    all_films = Film.objects.all()
    current_page_films = Paginator(all_films, 3)
    args = {}
    args['title'] = 'film'
    args['films'] = current_page_films.page(page_number)
    args['username'] = auth.get_user(request).username
    args['is_Superuser'] = auth.get_user(request).is_superuser
    return render_to_response("films.html", args)


def film(request, film_id):
    args = {}
    args['title'] = 'film'
    args['film'] = Film.objects.get(id=film_id)
    args['username'] = auth.get_user(request).username
    return render_to_response("film.html", args)


def filmUsers(request, film_id):
    args = {}
    args['title'] = 'film'
    args['film'] = Film.objects.get(id=film_id)
    args['username'] = auth.get_user(request).username
    return render_to_response("filmUsers.html", args)


def filmAdd(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['title'] = 'film'
    args['userTrue'] = auth.get_user(request).is_anonymous()

    if auth.get_user(request).is_anonymous() == False:
        if request.POST:
            form = FilmForm(request.POST)

            if form.is_valid():
                film_add = form.save(commit=False)
                film_add.film_date_public = datetime.datetime.today()
                film_add.film_user_id = auth.get_user(request).id

                youtube = request.POST.get('film_sided_id').find('youtube.com/')
                vimeo = request.POST.get('film_sided_id').find('vimeo.com/')
                if youtube == -1 and vimeo == -1:
                    youtube = request.POST.get('film_sided_id').find('youtu.be/')
                if youtube != -1:
                    film_add.film_sided_site = 2
                    home = request.POST.get('film_sided_id').find('=')
               	    end = request.POST.get('film_sided_id').find('&')
                    if end != -1:
                        youtube = request.POST.get('film_sided_id')[home+1:end]
                        film_add.film_sided_id = youtube
                    if end == -1:
                        youtube = request.POST.get('film_sided_id')[home+1:]
                        film_add.film_sided_id = youtube

                if vimeo != -1:
                    film_add.film_sided_site = 3
                    home = request.POST.get('film_sided_id').find('.com/')
                    vimeo = request.POST.get('film_sided_id')[home+5:]
                    film_add.film_sided_id = vimeo

                film_add.save()
                return redirect('/film/')
            else:
                args['error'] = "huina"
                args['username'] = 'huina'
                return render_to_response('error.html',args)
        else:
            film_form = FilmForm
            args['form'] = film_form
            return render_to_response('addFilm.html', args)

    args['error'] = 'add_User_none'
    return render_to_response('error.html', args)