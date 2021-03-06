# Generated by Django 3.0.7 on 2020-12-24 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201224_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.RemoveField(
            model_name='aadhar',
            name='user',
        ),
        migrations.AddField(
            model_name='aadhar',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aadhar',
            name='aadhar_no',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='aadhar',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
