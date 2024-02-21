
from django.urls import path
from Support_app import views

#urls path for template html files
urlpatterns = [
    path("",views.indexLogin, name="indexLogin"),
    path("perform_login",views.perform_login, name="perform_login"),
    path("homepage",views.homepage,name='homepage'),
    path("perform_logout",views.perform_logout, name="perform_logout"),
    path("page",views.page,name="page" )
]