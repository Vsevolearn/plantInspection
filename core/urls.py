from django.contrib import admin
from django.urls import path, re_path
from core import views


from .views import *

urlpatterns = [
    path('', views.library, name="library_base"),
    path('library-<page>', views.library_page, name="library_base_page"),
    path('user-<login>/library', views.library_pers, name="library_pers_page"),
    path('user-<login>/library-<page>', views.library_pers_page, name="library_pers_page"),
    
    path('exemplar-id<id>-page<page>', views.exemplar_page, name="exemplar_base_page"),
    path('user-<login>/exemplar-id<id>-page<page>', views.exemplar_pers_page, name="exemplar_pers_page"),

    path('sign_in', views.sign_in, name="sign_in"),
    path('register', views.register, name="register"),

    path('user-<login>/protocols', views.protocols, name="protocols"),
    path('user-<login>/protocols-delete-<id>', views.protocols_delete, name="protocols_delete"),
    


    path('user-<login>/protocol-<id>', views.protocol, name="protocol"),
    path('protocol_file', views.protocol_file, name="protocol_file"),
    path('user-<login>/protocol-<idp>/delete-<idt>', views.protocol_thr_delete, name="protocol_thr_delete"),
    path('protocol_alg', views.protocol_alg, name="protocol_alg"),

    
    
    path('user-<login>/personal', views.personal, name="personal"),

]