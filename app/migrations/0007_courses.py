# Generated by Django 4.1.7 on 2023-02-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_signup_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='courseimages')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]