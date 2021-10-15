# Generated by Django 3.2.5 on 2021-10-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dsuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=200, verbose_name='아이디')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=200, verbose_name='비밀번호')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='가입 시간')),
            ],
        ),
    ]