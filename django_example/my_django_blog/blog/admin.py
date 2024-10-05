from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post) # thêm model post vào admin, là khi vào admin quản lý thêm sửa xoá được post

