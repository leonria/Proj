# Generated by Django 3.2.dev20200521103454 on 2020-06-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HTech', '0006_auto_20200618_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twillo',
            old_name='CountryPhone',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='twillo',
            old_name='TwilloSid',
            new_name='account_sid',
        ),
        migrations.RenameField(
            model_name='twillo',
            old_name='TwilloKey',
            new_name='auth_token',
        ),
    ]
