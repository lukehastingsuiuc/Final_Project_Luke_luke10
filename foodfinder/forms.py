from django import forms
from foodfinder.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restaurant', 'rating', 'content']

    def clean_title(self):
        return self.cleaned_data['title'].strip()