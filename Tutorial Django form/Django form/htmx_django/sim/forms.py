from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, label="Name")
    surname = forms.CharField(min_length=2, label="Surname")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(min_length=7, label="Phone Number")
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        label="Message"
    )

