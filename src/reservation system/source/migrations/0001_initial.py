# Generated by Django 4.1.1 on 2022-10-30 20:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(max_length=80)),
                ('book_uid', models.UUIDField()),
                ('library_uid', models.UUIDField()),
                ('status', models.CharField(choices=[('RENTED', 'Rented'), ('RETURNED', 'Returned'), ('EXPIRED', 'Expired')], default='RENTED', max_length=20)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('till_date', models.DateField()),
            ],
        ),
    ]
