# Generated by Django 3.2.11 on 2022-02-09 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_headman'),
        ('students', '0007_alter_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('students', models.ManyToManyField(related_name='lectures', to='students.Student')),
            ],
        ),
    ]
