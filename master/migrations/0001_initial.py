# Generated by Django 3.1.4 on 2021-02-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField()),
                ('lname', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.IntegerField()),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('send_on', models.DateTimeField()),
            ],
        ),
    ]
