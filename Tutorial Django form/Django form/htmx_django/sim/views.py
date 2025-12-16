from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def example(request):
    form = ContactForm()
    return render(request, "example.html", {"form": form})


def sample_post(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        print(form.cleaned_data)  # debug output
        return HttpResponse(
            "<p style='color:green;'>Thank you! Your message has been sent ✅</p>"
        )

    return HttpResponse(
        "<p style='color:red;'>Please correct the errors and try again ❌</p>"
    )


