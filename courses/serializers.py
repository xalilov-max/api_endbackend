from rest_framework import serializers
from .models import Course, Lesson, Comment,Rating

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video', 'content', 'created_at', 'course']
    
    def validate_course(self, value):
        """
        Kurs mavjudligini tekshirish.
        """
        try:
            # Kursni tekshirish
            course = Course.objects.get(id=value.id)
        except Course.DoesNotExist:
            raise serializers.ValidationError("Bunday kurs mavjud emas.")
        return value

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # Kursdagi darslarni ko‘rsatish
    instructor = serializers.StringRelatedField()  # O‘qituvchi ismi

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'created_at', 'lessons']

class CommentSerializer(serializers.ModelSerializer):
    # Foydalanuvchi nomini ko'rsatish uchun
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'lesson', 'user', 'content', 'created_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'lesson', 'user', 'liked']
