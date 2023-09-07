# Generated by Django 4.2.4 on 2023-09-01 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_burgers_category_delete_food_burgers_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='burgers',
            options={'verbose_name': 'Бургер', 'verbose_name_plural': 'Бургеры'},
        ),
        migrations.AlterField(
            model_name='burgers',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='post/%Y/%m/%d/', verbose_name='Изображение')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Рейтинг')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='Цена')),
                ('orders', models.PositiveSmallIntegerField(default=0, verbose_name='Заказов')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
            },
        ),
    ]