from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
# User모델은 User admin을 같이 등록해줘야 함!
# UserAdmin 클래스는 User모델에 대해서 특별한 인터페이스 제공
admin.site.register(User, UserAdmin)