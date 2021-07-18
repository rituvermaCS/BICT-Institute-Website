from django.urls import path
from institute import views
urlpatterns = [
     path('',views.index, name='index'),
     path('about/',views.about, name='about'),
     path('course/',views.course, name='course'),
     path('gallery/',views.gallery, name='gallery'),
     path('onlineregistration/',views.onlineregistration, name='onlineregistration'),
     path('checkresult/',views.checkresult, name='checkresult'),
     path('checkstatus/',views.checkstatus, name='checkstatus'),
     path('managementteam/',views.managementteam, name='managementteam'),
     path('branchlist/',views.branchlist, name='branchlist'),
     path('selectedstudent/',views.selectedstudent, name='selectedstudent'),
     path('contact/',views.contact, name='contact'),
     path('listt/',views.listt, name='listt')
]