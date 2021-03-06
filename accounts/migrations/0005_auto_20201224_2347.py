# Generated by Django 3.0.7 on 2020-12-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201224_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aadhar',
            name='id',
        ),
        migrations.AlterField(
            model_name='aadhar',
            name='aadhar_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='bank',
            name='account_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='dob',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='jobexperience',
            name='yoe',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='percent',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='yop',
            field=models.CharField(max_length=4),
        ),
    ]
