from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Course, Lesson, Comment, Rating
from .serializers import CourseSerializer, LessonSerializer, CommentSerializer, RatingSerializer


# Paginatsiya klassi
class StandardPagination(PageNumberPagination):
    """
    Bu klass bir sahifada ko'rsatiladigan elementlar sonini belgilaydi.
    `page_size` - har bir sahifada ko'rsatiladigan elementlar sonini belgilaydi.
    `page_size_query_param` - foydalanuvchi sahifa o'lchamini so'rovda ko'rsatish imkonini beradi.
    `max_page_size` - maksimal sahifa o'lchamini belgilaydi.
    """
    page_size = 3  
    page_size_query_param = 'page_size'
    max_page_size = 50


# Kurslar uchun ModelViewSet
class CourseViewSet(viewsets.ModelViewSet):
    """
    Kurslar modelini ko'rsatish uchun ViewSet.
    Kurslarni yaratish, o'zgartirish, o'chirish va ko'rish imkoniyatlarini beradi.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Foydalanuvchi avtorizatsiya qilingan bo'lishi kerak
    pagination_class = StandardPagination  # Paginatsiya
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['instructor']  # Filtrlash mumkin bo'lgan maydonlar
    search_fields = ['title', 'description']  # Qidirish maydonlari
    ordering_fields = ['created_at', 'updated_at']  # Tartiblash mumkin bo'lgan maydonlar
    ordering = ['-created_at']  # Default tartiblash bo'yicha


class LessonViewSet(viewsets.ModelViewSet):
    """
    Darslar modelini ko'rsatish uchun ViewSet.
    Darslarni yaratish, o'zgartirish, o'chirish va ko'rish imkoniyatlarini beradi.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        # course maydonini o'rnatish
        course_id = self.request.data.get('course')
        
        # course_id mavjudligini tekshirish
        if not course_id:
            raise serializers.ValidationError({'course': 'Course ID is required'})  # course_id mavjud bo'lmasa, xato yuboriladi

        try:
            course = Course.objects.get(id=course_id)  # Kursni ID orqali olish
        except Course.DoesNotExist:
            raise serializers.ValidationError({'course': 'Course with this ID does not exist'})  # Kurs topilmasa, xato yuboriladi

        # course maydonini to'ldirib saqlash
        serializer.save(course=course)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Izohlar modelini ko'rsatish uchun ViewSet.
    Foydalanuvchilarga darslarga izoh qoldirish imkoniyatini beradi.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Foydalanuvchi avtorizatsiya qilingan bo'lishi kerak
    pagination_class = StandardPagination  # Paginatsiya
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['lesson', 'user']  # Filtrlash uchun maydonlar
    search_fields = ['content']  # Qidirish maydoni
    ordering_fields = ['created_at']  # Tartiblash mumkin bo'lgan maydonlar
    ordering = ['-created_at']  # Default tartiblash

    def perform_create(self, serializer):
        """
        Yangi izoh yaratishda foydalanuvchi ma'lumotlarini avtomatik ravishda qo'shadi.
        """
        serializer.save(user=self.request.user)


class RatingViewSet(viewsets.ModelViewSet):
    """
    Reytinglar modelini ko'rsatish uchun ViewSet.
    Foydalanuvchilarga darslarga reyting qo'shish imkoniyatini beradi.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]  
    pagination_class = StandardPagination  
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['lesson', 'user']  
    ordering_fields = ['pk']  

    def perform_create(self, serializer):
        """
        Yangi reyting yaratishda foydalanuvchi ma'lumotlarini avtomatik ravishda qo'shadi.
        """
        serializer.save(user=self.request.user)
