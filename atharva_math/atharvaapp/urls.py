from django.urls import path
from atharvaapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'atharvaapp'

urlpatterns = [
    path('',views.home_page,name='index'),
    path('about',views.about,name='about'),
    path('maths/summation',views.summation,name='summation'),
    path('maths/subtraction',views.substraction,name='subtraction'),
    path('maths/multiplication',views.multiplication,name='multiplication'),
    path('maths/division',views.division,name='division'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
