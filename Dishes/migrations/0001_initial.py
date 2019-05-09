# Generated by Django 2.2.1 on 2019-05-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dishId', models.AutoField(primary_key=True, serialize=False, verbose_name='菜品编号')),
                ('dishName', models.CharField(max_length=50, verbose_name='菜品名称')),
                ('dishPrice', models.FloatField(verbose_name='菜品价格')),
                ('dishType', models.CharField(max_length=30, null=True, verbose_name='菜品分类')),
                ('dishStock', models.IntegerField(default=999, verbose_name='菜品库存')),
                ('dishPicture', models.TextField(null=True, verbose_name='菜品图片')),
                ('dishDescription', models.TextField(null=True, verbose_name='菜品描述')),
                ('dishAddTime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='菜品添加时间')),
            ],
            options={
                'verbose_name': '菜品',
                'verbose_name_plural': '菜品',
            },
        ),
    ]
