from django.urls import path
from home.views import BlogView

urlpatterns = [
    path('blog/' , BlogView.as_view()) ,
]