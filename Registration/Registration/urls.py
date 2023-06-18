"""Registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Codeflix import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('payment/',views.paymentpage,name='payment'),
    path('course/',views.course,name='course'),
    path('contact/',views.contact,name='contact'),
    path('video/',views.video,name='video'),
    path('python/',views.python,name='python'),
    path('about/',views.about,name='about'),
    path('basic/',views.basic,name='basic'),
    path('search/',views.search,name='search'),
    path('base/',views.base,name='base'),
    path('Tutorial/',views.Tutorial,name='Tutorial'),
    path('subs/',views.subs,name='subs'),
    path('charge/',views.charge,name='charge'),
    path('case/',views.case,name='case'),
    path('pypage1/',views.pypage1,name='pypage1'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
