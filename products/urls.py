from django.urls import path
from . import views

urlpatterns = [
    # products
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(),
         name="product-detail"),
    # categories
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category-deatil'),
    # sub-categories
    path('sub-categories/', views.SubCategoryList.as_view(), name='sub_category-list'),
    path('sub-categories/<int:pk>/',
         views.SubCategoryDetailView.as_view(), name='sub_category-deatil'),
]
