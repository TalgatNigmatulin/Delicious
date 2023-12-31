# Generated by Django 4.2.4 on 2023-08-31 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='post/%Y/%m/%d/', verbose_name='Изображение')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Цена')),
                ('orders', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Заказы')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Бургер  ',
                'verbose_name_plural': 'Бургеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.AddField(
            model_name='burgers',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.category', verbose_name='Категория'),
        ),
    ]
