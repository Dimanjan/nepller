# Generated by Django 3.2.13 on 2022-05-23 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TUsers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCtweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_text', models.CharField(max_length=140, null=True)),
                ('time', models.CharField(default='05/23/2022 10:26:52 AM', max_length=50)),
                ('comment', models.CharField(max_length=100, null=True)),
                ('like', models.ManyToManyField(related_name='liked_users', to='TUsers.TUser')),
                ('reply', models.ManyToManyField(related_name='_Tweets_tctweets_reply_+', to='Tweets.TCtweets')),
                ('retweet', models.ManyToManyField(related_name='retweeted_users', to='TUsers.TUser')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TUsers.tuser')),
            ],
        ),
    ]
