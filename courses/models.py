from django.db import models
from accounts.models import CustomUser

class Course(models.Model):
    """
    Kurs modelini yaratish uchun foydalaniladi.
    Ushbu model kurs nomi, tavsifi, o'qituvchi va yaratish sanasini saqlaydi.
    """
    title = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    instructor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='courses', verbose_name="O'qituvchi", blank=True, null = True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        """
        Modelning Meta ma'lumotlari:
        - Verbose nomlar
        - Tashqi tartib (yaratilgan sana bo'yicha).
        """
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['created_at']

    def __str__(self):
        """
        Modelni matnli shaklda ifodalash: kurs nomi.
        """
        return self.title

class Lesson(models.Model):
    """
    Dars modelini yaratish uchun foydalaniladi.
    Ushbu model darsning kursi, nomi, video fayli, mazmuni va yaratish sanasini saqlaydi.
    """
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="Kurs"
    )
    title = models.CharField(max_length=255, verbose_name="Dars nomi")
    video = models.FileField(upload_to='lessons/videos/', verbose_name="Video fayl")
    content = models.TextField(verbose_name="Dars mazmuni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        """
        Modelning Meta ma'lumotlari:
        - Verbose nomlar
        - Tashqi tartib (yaratilgan sana bo'yicha).
        """
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
        ordering = ['created_at']

    def __str__(self):
        """
        Modelni matnli shaklda ifodalash: kurs nomi va dars nomi.
        """
        return f"{self.course.title} - {self.title}"

class Comment(models.Model):
    """
    Izoh modelini yaratish uchun foydalaniladi.
    Ushbu model darsga yozilgan izohni va izohni yozgan foydalanuvchining ma'lumotlarini saqlaydi.
    """
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='comments', verbose_name="Dars"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='comments', verbose_name="Foydalanuvchi"
    )
    content = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        """
        Modelning Meta ma'lumotlari:
        - Verbose nomlar
        - Tashqi tartib (yaratilgan sana bo'yicha).
        """
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['created_at']

    def __str__(self):
        """
        Modelni matnli shaklda ifodalash: foydalanuvchi nomi va dars nomi.
        """
        return f"Comment by {self.user.username} on {self.lesson.title}"

class Rating(models.Model):
    """
    Reyting modelini yaratish uchun foydalaniladi.
    Ushbu model darsga foydalanuvchi tomonidan berilgan reytingni saqlaydi.
    """
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='ratings', verbose_name="Dars"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi"
    )
    liked = models.CharField(
    choices=[('like', 'Like'), ('dislike', 'Dislike')], 
    max_length=10
)
    
    class Meta:
        """
        Modelning Meta ma'lumotlari:
        - Verbose nomlar
        - Tashqi tartib (dars bo'yicha).
        - Foydalanuvchi va darsning birgalikda unikal bo'lishini ta'minlaydi.
        """
        unique_together = ['lesson', 'user']
        verbose_name = "Reyting"
        verbose_name_plural = "Reytinglar"
        ordering = ['lesson']

    def __str__(self):
        """
        Modelni matnli shaklda ifodalash: foydalanuvchi nomi va qabul qilgan yoki olmagan reyting.
        """
        return f"{self.user.username} - {'Yoqdi' if self.liked else 'Yoqmadi'}"
