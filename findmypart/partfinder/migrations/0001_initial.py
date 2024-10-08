# Generated by Django 3.2.16 on 2024-07-13 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_visible', models.BooleanField(default=True, help_text='Снимите галочку, что бы убрать из поиска', verbose_name='В зоне видимости')),
                ('producer_country_name', models.CharField(max_length=256, verbose_name='Страна производитель')),
            ],
            options={
                'verbose_name': 'марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_visible', models.BooleanField(default=True, help_text='Снимите галочку, что бы убрать из поиска', verbose_name='В зоне видимости')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mark', to='partfinder.mark', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_visible', models.BooleanField(default=True, help_text='Снимите галочку, что бы убрать из поиска', verbose_name='В зоне видимости')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('json_data', models.JSONField()),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='partfinder.mark', verbose_name='Марка')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='partfinder.model', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'запчасть',
                'verbose_name_plural': 'Запчасти',
            },
        ),
        migrations.AddConstraint(
            model_name='mark',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_mark'),
        ),
        migrations.AddConstraint(
            model_name='model',
            constraint=models.UniqueConstraint(fields=('mark_id', 'name'), name='unique_model_mark'),
        ),
    ]
