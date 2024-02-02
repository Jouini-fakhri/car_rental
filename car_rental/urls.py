# urls.py
from django.urls import path
from .views import CustomLogoutView, home, login_view, signup, car_list, car_detail, car_new, car_edit, car_delete, success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('car_list/', car_list, name='car_list'),
    path('car/<int:pk>/', car_detail, name='car_detail'),
    path('car/new/', car_new, name='car_new'),
    path('car/<int:pk>/edit/', car_edit, name='car_edit'),
    path('car/<int:pk>/delete/', car_delete, name='car_delete'),
    path('success', success, name='success'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
