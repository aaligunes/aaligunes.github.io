# Generated by Django 4.2.5 on 2023-10-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_yorumlar_delete_yorum'),
    ]

    operations = [
        migrations.CreateModel(
            name='favori_filmler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favori_button', models.BooleanField(default=False)),
                ('favoriye_eklenen_film_id', models.IntegerField()),
                ('favoriye_ekleyen_kullanici_adi', models.TextField(max_length=100)),
            ],
        ),
    ]
