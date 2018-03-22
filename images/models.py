from django.db import models
from django.contrib.auth.models import User #유저정보 임폴트
# Create your models here.
class Image(models.Model): #사진모델생성
    file = models.FileField(max_length=50) #사진파일
    location = models.CharField(max_length=50) #위치
    caption = models.TextField() #캡션
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #생성자 :외래키-유저ID
    updated_at = models.DateTimeField(auto_now=True) #수정일
    created_at = models.DateTimeField(auto_now_add=True) #생성일
    def __str__(self):
        return f'{self.location} - {self.caption}' #위치, 캡션 

class Comment(models.Model):
    message = models.TextField() #메세지(댓글내용)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #생성자 : 외래키-유저id 
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True) #댓글다는 사진.:외래키-이미지
    updated_at = models.DateTimeField(auto_now=True) #수정일
    created_at = models.DateTimeField(auto_now_add=True)#생성일
    def __str__(self):
        return f'{self.message}'

class Like(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #생성자
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True) #좋아요한사진
    created_at = models.DateTimeField(auto_now_add=True)  #
    
