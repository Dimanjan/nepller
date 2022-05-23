# Generated by Django 3.2.13 on 2022-05-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('modified_time', models.CharField(default='05/23/2022 10:26:52 AM', max_length=50)),
                ('blocked', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=10000, null=True)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='TUsers.TUser')),
            ],
        ),
    ]