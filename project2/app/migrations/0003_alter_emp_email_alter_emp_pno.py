# Generated by Django 5.0.4 on 2024-04-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_emp_pno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='email',
            field=models.EmailField(max_length=300),
        ),
        migrations.AlterField(
            model_name='emp',
            name='pno',
            field=models.CharField(max_length=50),
        ),
    ]
