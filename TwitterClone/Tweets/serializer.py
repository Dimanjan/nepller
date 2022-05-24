from rest_framework import serializers
from Tweets.models import TCTweet
from django import forms

class TCTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=TCTweet
        fields='__all__'

class TCValidator(forms.Form):
    username=forms.CharField(max_length=100)
    tweet_text = forms.CharField(max_length=140)

class ReplyValidator(forms.Form):
    username=forms.CharField(max_length=100)
    reply_text = forms.CharField(max_length=140)

class RetweetValidator(forms.Form):
    username=forms.CharField(max_length=100)