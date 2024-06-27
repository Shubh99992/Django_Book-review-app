# Assuming you have a forms.py file in your Django app

from django import forms
from .models import Book, User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User as mainUser

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


class FavoriteBooksForm(forms.ModelForm):
    favorite_books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['favorite_books']

class RecentReadsForm(forms.ModelForm):
    recent_reads = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['recent_reads']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = mainUser

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            User.objects.get_or_create(user=user)  # Create CustomUser instance
        return user
