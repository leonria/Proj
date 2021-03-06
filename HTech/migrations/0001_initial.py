# Generated by Django 3.2.dev20200521103454 on 2020-06-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(help_text='Enter the first name', max_length=100)),
                ('l_name', models.CharField(help_text='Enter the last name', max_length=100)),
                ('Country', models.CharField(help_text='Enter the country', max_length=100)),
                ('PhoneNumber', models.IntegerField(help_text='Enter the phone number')),
                ('Email', models.EmailField(help_text='Enter email address', max_length=100)),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'All Users',
            },
        ),
    ]
