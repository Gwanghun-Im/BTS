from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'tour'

urlpatterns = [

    path('detail/',views.tour_detail, name = 'tour_detail'),
    path('detail/<int:spot_pk>/',views.tour_review, name = 'tour_review'),
    path('route/',views.route, name = 'tour_route'),
<<<<<<< HEAD
    path('routerandom/',views.route_random, name = 'tour_route_random'),
    path('city/',views.tour_city, name = 'tour_city')

]
=======
    path('city/',views.tour_city, name = 'tour_city'),
    path('test/',views.test, )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 2c9738092f25e9b01d7ed53f835564972a0cff7f
