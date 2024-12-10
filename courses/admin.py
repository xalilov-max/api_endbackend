from django.contrib import admin
from .models import Course, Lesson, Comment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['instructor', 'created_at']
    ordering = ['created_at']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['course', 'created_at']
    ordering = ['created_at']   

    # Custom queryset
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.all()  # Hamma darslarni qaytaradi  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ['lesson', 'user', 'created_at']  # Admin panelida ko'rsatiladigan ustunlar
    search_fields = ['content']  # Qidiruv uchun ishlatiladigan maydonlar
    list_filter = ['lesson', 'created_at']  # Filtrlar
    ordering = ['created_at']  # Tartiblash
