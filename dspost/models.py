from django.db import models

from dsuser.models import Dsuser

class Tag(models.Model):
    name = models.CharField(max_length=30)
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name="작성 시간")

    class Meta:
        db_table = 'dstag'
        verbose_name = '태그'
        verbose_name_plural = '태그들'
class Dspost(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    author = models.ForeignKey(Dsuser,on_delete=models.CASCADE,verbose_name="작성자")
    img_url = models.URLField(verbose_name="이미지 URL")
    contents = models.TextField(verbose_name="글 내용")
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name="작성 시간")
    tags = models.ManyToManyField(Tag,verbose_name='태그')

    class Meta:
        db_table = 'dspost'
        verbose_name = '게시글'
        verbose_name_plural = '게시글들'

