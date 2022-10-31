from django.contrib import admin
from .models import User,ImageVerification


# Register your models here.
# configure you admin dashboard
class UserAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','email','phonenumber')
    search_fields=('firstname','lastname','email','phonenumber')
admin.site.register(User,UserAdmin)


# class UploadImageTestAdmin(admin.ModelAdmin):
#     list_display=('patient','image')
#     search_fields=('patient','image')
# admin.site.register(UploadImageTest,UploadImageTestAdmin)

class ImageVerificationAdmin(admin.ModelAdmin):
    list_display=('patient','blister_image_url','timestamp')
    search_fields=('patient','blister_image_url','timestamp')
admin.site.register(ImageVerification, ImageVerificationAdmin)
