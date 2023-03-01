from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backtest import views

router = routers.DefaultRouter()
router.register('Parameter', views.ParameterView, 'Parameter')

urlpatterns = [
    path('backtest/', include('backtest.urls')),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    # 리액트 템플릿
    # re_path('.*', TemplateView.as_view(template_name='index.html'))
]
