# Generated by Django 3.0.5 on 2020-04-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_valine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valine',
            options={'verbose_name': 'valine评论设置', 'verbose_name_plural': 'valine评论设置'},
        ),
        migrations.AlterField(
            model_name='valine',
            name='avatar',
            field=models.CharField(default='', max_length=100, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='valine',
            name='pagesize',
            field=models.IntegerField(default='10', max_length=100, verbose_name='pageSize'),
        ),
        migrations.AlterField(
            model_name='valine',
            name='placeholder',
            field=models.CharField(max_length=100, verbose_name='placeholder'),
        ),
    ]
