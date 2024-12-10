from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Lesson

@receiver(post_save, sender=Lesson)
def send_lesson_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Yangi Dars: {instance.title}"
        message = f"Dars mazmuni: {instance.content}\n\nDars videoni platformadan koring"
        recipient = instance.course.instructor.email  
        send_mail(subject, message, 'madrahimovq@gmail.com', [recipient])

