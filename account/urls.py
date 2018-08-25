
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

app_name="account"

urlpatterns =[
    url(r'^signup',views.signupView,name='signup'),
    url(r'^login',views.loginView,name='login'),
    url(r'^logout',views.logoutView,name='logout'),
    url(r'^profile',views.profileView,name='profile'),
    url(r'^edit',views.editView,name='edit'),

]
