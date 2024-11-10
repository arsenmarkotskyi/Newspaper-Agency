from pydoc_data.topics import topics
import re

from django import forms

from newspaper.models import Newspaper, Topic, Redactor


class NewspaperForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Published Date",
    )

    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Topics"
    )
    publishers = forms.ModelMultipleChoiceField(
        queryset= Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Publishers",
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topics", "publishers"]


class RedactorForm(forms.ModelForm):

    class Meta:
        model = Redactor
        fields = ["password", "username", "first_name", "last_name", "email", "years_of_experience"]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            validate_password(password)
        return password



def validate_password(value):
    if len(value) < 8:
        raise forms.ValidationError("Password must be at least 8 characters")
    if not re.search(r"[a-zA-Z]", value):
        raise forms.ValidationError("Password must contain at least one letter (uppercase or lowercase).")
    if not re.search(r"\d", value):
        raise forms.ValidationError("Password must contain at least one digit.")


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
