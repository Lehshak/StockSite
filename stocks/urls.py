
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static

urlpatterns = [path("", views.IndexView.as_view(), name="index"),
                  path("<int:pk>/", views.DetailView.as_view(), name="detail"),
                  path("compare/<int:pk1>/<int:pk2>/", views.CompareView.as_view(), name="compare"),
                  path("get-stock-ids/", views.get_stock_ids, name="get_stock_ids"),
                  path('expected/', views.ExpectedGrowthView.as_view(), name='expected'),
               ]
