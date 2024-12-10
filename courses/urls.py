from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, CommentViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]


# /api/v1/courses/      # Kurslar ro'yxati va yaratish
# /api/v1/courses/{id}/  # Kursni ko'rish, yangilash va o'chirish
# /api/v1/lessons/      # Darslar ro'yxati va yaratish
# /api/v1/lessons/{id}/  # Darsni ko'rish, yangilash va o'chirish
# /api/v1/comments/     # Izohlar qo'shish
# /api/v1/comments/{id}/  # Izohni ko'rish, yangilash va o'chirish
# /api/v1/ratings/      # Reyting qo'shish
# /api/v1/ratings/{id}/  # Reytingni ko'rish, yangilash va o'chirish
