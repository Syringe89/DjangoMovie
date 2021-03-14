from django import forms

from .models import *


class MovieAddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'text']


class MovieAddRatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(RatingStar.objects.all(), empty_label=None)

    class Meta:
        model = Rating
        fields = ['star']
