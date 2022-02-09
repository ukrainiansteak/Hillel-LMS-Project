# Generated by Django 3.2.11 on 2022-02-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20220209_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('teachers', models.ManyToManyField(related_name='courses', to='teachers.Teacher')),
            ],
        ),
    ]
