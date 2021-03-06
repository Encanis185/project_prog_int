"""wkp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from users import views as users_views

from webapp.views import delete_profesor, inicio,buscar, profesor_profile, create_profesor, read_profesor,update_profesor, delete_profesor,search_profesor, AddCommentView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('buscar/', buscar, name="buscar"),path('buscar/', buscar, name="buscar"),
    

    path('register/', users_views.register, name="register"),
    path('profile/', users_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),

    path('search-profesor/profesor_profile/<id>/', profesor_profile, name='profesor_profile'),
    path('create-profesor/', create_profesor, name='create_profesor'),
    path('read-profesor/', read_profesor, name='read_profesor'),
    path('update-profesor/<id>/', update_profesor, name='update_profesor'),
    path('delete-profesor/<id>/',delete_profesor,name='delete_profesor'),

    path('search-profesor/', search_profesor, name='search_profesor'),
    #path('search-profesor/profesor_profile/<id>/comment', AddCommentView, name='profesor_comment'),

    #path(url(r"^comments/", include("pinax.comments.urls", namespace="pinax_comments"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
