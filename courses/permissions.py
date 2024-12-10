from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Faqat kurs yoki darsning egasi ozgartirishlar kiritish huquqiga ega,
    boshqalar faqat oqish imkoniyatiga ega.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Foydalanuvchi faqat o‘zining kursi yoki darsini tahrirlashi mumkin
        return obj.owner == request.user
