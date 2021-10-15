from django.db import models


class Dsuser(models.Model):
    userId = models.CharField(max_length=200, verbose_name="아이디")
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=200, verbose_name="비밀번호")
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name="가입 시간")


    

