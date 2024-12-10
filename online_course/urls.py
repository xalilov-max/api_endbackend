"""
URL configuration for online_course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from courses.views import (
    CourseViewSet,
    LessonViewSet,
    CommentViewSet,
    RatingViewSet,
)

# Swagger sozlamalari
schema_view = get_schema_view(
    openapi.Info(
        title="Online Kurs Platformasi API", 
        default_version='v1',  
        description="Online kurs platformasi uchun API, foydalanuvchilar uchun qulay hujjatlashtirilgan interfeys.",
        terms_of_service="https://www.google.com/policies/terms/",  
        contact=openapi.Contact(email="support@onlinekursplatforma.uz"),  
        license=openapi.License(name="MIT License"),  
    ),
    public=True,  
    permission_classes=(permissions.AllowAny,),  
)

# Routerni sozlash
v1_router = DefaultRouter()
v1_router.register(r'courses', CourseViewSet, basename='courses')  # Kurslar uchun viewset
v1_router.register(r'lessons', LessonViewSet, basename='lessons')  # Darslar uchun viewset
v1_router.register(r'comments', CommentViewSet, basename='comments')  # Izohlar uchun viewset
v1_router.register(r'ratings', RatingViewSet, basename='ratings')  # Reytinglar uchun viewset

# Asosiy urlpatterns
urlpatterns = [
    # Admin paneli URLi
    path('admin/', admin.site.urls),

    # Authentication API (Djoser) - foydalanuvchi autentifikatsiyasi
    path('api/auth/', include('djoser.urls')),  # Djoser URLs (Login, Registration)
    path('api/auth-token/', include('djoser.urls.authtoken')),  # Token based authentication

    # API versiyalari
    path('api/v1/', include(v1_router.urls)),  # v1 versiyasi uchun API URLi
    path('auth/', include("rest_framework.urls")),  # Django REST framework uchun authentikatsiya URLi

    # Swagger dokumentatsiyasi
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # MEDIA fayllarini xizmat qilish

# v2 versiyasi uchun yangi router
v2_router = DefaultRouter()
v2_router.register(r'new-courses', CourseViewSet, basename='new-courses')  # Yangi kurslar uchun viewset
urlpatterns += [
    path('api/v2/', include(v2_router.urls)),  # v2 versiya uchun API URLi
]
