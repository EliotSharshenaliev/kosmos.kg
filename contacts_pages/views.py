from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms

from contacts_pages.models import FeedbackMessage


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'stext-111 cl2 plh3 size-116 p-lr-28', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'stext-111 cl2 plh3 size-116 p-lr-28', 'placeholder': 'Ваш email адресс'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25', 'placeholder': 'Напишите что-нибудь...'}))


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            FeedbackMessage(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                msg=form.cleaned_data["message"]
            ).save()
            return redirect("product.html")

    else:
        form = FeedbackForm()

    return render(request, 'contact.html', {'form': form})
