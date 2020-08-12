from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
import folium
from .models import Businesses,UserProfile,Posts
from .forms import ProfileForm,PostsForm
from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    the_user = UserProfile.objects.get(user=current_user)
    user_location = the_user.location

    posts = Posts.objects.filter(user__location__contains = user_location)

    return render(request, 'index.html',{'posts':posts,'the_user':the_user})

@login_required(login_url='/accounts/login/')
def neighborhoods(request,neighborhood):

    posts = Posts.objects.filter(user__location__contains=neighborhood)

    if neighborhood == 'cbd':
        user_location = Point(36.823634, -1.283784, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=1500)))
        map_page = folium.Map(location=[-1.283784,36.823634],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood == 'westlands':
        user_location = Point(36.809557, -1.267824, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.267824,36.809557],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood == 'makadara':
        user_location = Point(36.855793, -1.302774, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.302774,36.855793],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood =='kasarani':
        user_location = Point(36.897451, -1.223924, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.223924, 36.897451],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood =='pumwani':
        user_location = Point(36.846043, -1.283208, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.283208, 36.846043],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood =='kibera':
        user_location = Point(36.781516, -1.313696, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.313696, 36.781516],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood =='karen':
        user_location = Point(36.703910, -1.320081, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.320081, 36.703910],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif neighborhood =='dagoretti':
        user_location = Point(36.712655, -1.279289, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.279289, 36.712655],zoom_start=14,width=750, height=500)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()
        
    return render(request, 'neighborhood.html',{'posts':posts, 'my_map':my_map})

@login_required(login_url='/accounts/login/')
def send_email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_welcome_email(name, email)
    return redirect(new_profile)

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return HttpResponseRedirect(reverse('profile',args=[str(request.user.id)]))

    else:
        form = ProfileForm()

    return render(request, 'new_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile = UserProfile.objects.get(id = id)

    if profile.location == 'cbd':
        user_location = Point(36.823634, -1.283784, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=1500)))
        map_page = folium.Map(location=[-1.283784,36.823634],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location == 'westlands':
        user_location = Point(36.809557, -1.267824, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.267824,36.809557],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location == 'makadara':
        user_location = Point(36.855793, -1.302774, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.302774,36.855793],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location =='kasarani':
        user_location = Point(36.897451, -1.223924, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.223924, 36.897451],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location =='pumwani':
        user_location = Point(36.846043, -1.283208, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.283208, 36.846043],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location =='kibera':
        user_location = Point(36.781516, -1.313696, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.313696, 36.781516],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location =='karen':
        user_location = Point(36.703910, -1.320081, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.320081, 36.703910],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    elif profile.location =='dagoretti':
        user_location = Point(36.712655, -1.279289, srid=4326)
        businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=2000)))
        map_page = folium.Map(location=[-1.279289, 36.712655],zoom_start=14)
        for business in businesses:
            point = business.location
            lat = point.y
            lon = point.x
            folium.Marker([lat,lon],
                        popup=f'{business.name}',
                        tooltip=f'{business.name}',
                        icon=folium.Icon(icon=' glyphicon-briefcase', color='green')).add_to(map_page)
            my_map = map_page._repr_html_()

    return render(request, 'profile.html',{'profile':profile,'my_map':my_map})

@login_required(login_url='/accounts/login/')
def new_post(request,id):
    the_user = UserProfile.objects.get(id = id)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = the_user
            post.save()
        return redirect(index)

    else:
        form = PostsForm()

    return render(request, 'new_post.html',{'form':form})