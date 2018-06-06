from django.urls import path
from . import views


urlpatterns = [
    path('publish/', views.publish, name='Publish'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]