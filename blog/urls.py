from django.urls import path
from blog import views
# TODO: APP NAME 
app_name="blog"

urlpatterns = [
    path('list/',views.blog_view,name="blog_view"),
    path('new/<str:data>/',views.data_view,name='data_view')
]