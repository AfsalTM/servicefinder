from django.urls import path
from webapp import views


urlpatterns = [
    path('home1', views.home_page, name='home1'),
path('',views.login_user,name='login_user'),
path('sign_user/',views.sign_user,name='sign_user'),
path('save_user/',views.save_user,name='save_user'),
path('user_login/',views.user_login,name='user_login'),
path('profile/', views.profile_page, name='profile'),
path('service_view/',views.service_view,name='service_view'),
path('profile_view/',views.profile_view,name='profile_view'),
path('logout/', views.logout_user, name='logout_user')


]
