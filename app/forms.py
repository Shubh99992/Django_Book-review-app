# Assuming you have a forms.py file in your Django app

from django import forms

class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    RATING_CHOICES = [
        (5, '★★★★★'),
        (4, '★★★★'),
        (3, '★★★'),
        (2, '★★'),
        (1, '★'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'rating-radio'}))
