from rest_framework import serializers
from Tweets.models import TCtweets
from django import forms

class TCtweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TCtweets
        fields='__all__'

class TCValidator(forms.Form):
    username=forms.CharField(max_length=100)
    tweet_text = forms.CharField(max_length=140)

class ReplyValidator(forms.Form):
    username=forms.CharField(max_length=100)
    reply_text = forms.CharField(max_length=140)

class RetweetValidator(forms.Form):
    username=forms.CharField(max_length=100)