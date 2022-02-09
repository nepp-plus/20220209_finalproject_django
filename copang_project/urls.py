"""copang_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from copang_app.api.user import User, UserSearch

# swagger 정보 사항 세팅 -> schema_view 변수에 담아두기
schema_view = get_schema_view(
    openapi.Info(
        title='Copang API 명세',
        default_version='v1',
        description='빅데이터 파이썬 최종 프로젝트를 장고로 컨버팅 합니다.',
        terms_of_service="https://neppplus.com",
        contact=openapi.Contact(name='Tester', email='test@test.com'),
        license=openapi.License(name='Test License')
    ),
    public=True,
    permission_classes=(AllowAny,)
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', User.as_view(), name='user'),
    path('user/search', UserSearch.as_view(), name='user_search'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^api/docs$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
