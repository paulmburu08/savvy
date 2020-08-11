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
from .models import Businesses,UserProfile
from .forms import ProfileForm
from .email import send_welcome_email


# Create your views here.
def index(request):

    return render(request, 'index.html')

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

    profile = UserProfile.objects.get(user__id = id)
    # geolocator = Nominatim(user_agent="savvyapp")
    # location_name = profile.location
    # location = geolocator.geocode(location_name)

    # latitude = location.latitude
    # longitude = location.longitude

    # global user_location
    user_location = Point(36.762300, -1.298031, srid=4326)
    # user_location = fromstr('POINT(-73 40)')
    businesses = Businesses.objects.filter(location__distance_lte=(user_location, D(m=1000)))
    for business in businesses:
        point = business.location
        lat = point.y
        lon = point.x
        map_osm = folium.Map(location=[lat,lon])
    return render(request, 'profile.html',{'profile':profile,'businesses':businesses})

# class BusinessList(generic.ListView):
#     model = Businesses
#     context_object_name = 'businesses'
#     queryset = Businesses.objects.annotate(distance=Distance('location',
#     user_location)
#     ).order_by('distance')[0:6]
#     template_name = 'profile.html'