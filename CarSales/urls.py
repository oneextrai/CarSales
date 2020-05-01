from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('classic/', include('Classic.urls')),
	path('all/', include('All.urls')),
	path('ourmission/', include('OurMission.urls')),
	path('about/', include('About.urls')),
	path('contact/', include('Contact.urls')),
    path('admin/', admin.site.urls),
    path('', include('Sales.urls'))
]