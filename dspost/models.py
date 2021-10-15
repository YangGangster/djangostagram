from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목"),
    author = models.ForeignKey('dsuser.Dsuser',on_delete=models.CASCADE,verbose_name="작성자")
    img_url = models.URLField(verbose_name="이미지 URL"),
    contents = models.TextField(verbose_name="글 내용")
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name="작성 시간")
    # tag = models.ManyToManyField('tag.Tag',verbose_name='태그')

    class Meta:
        db_table = 'dspost'
        verbose_name = '게시글'
        verbose_name_plural = '게시글들'