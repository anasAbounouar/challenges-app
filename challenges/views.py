# views.py
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    "january": "Start a daily gratitude journal!",
    "february": "Practice a new hobby every weekend!",
    "march": "Read one book every week!",
    "april": "Go for a 5k walk every Sunday!",
    "may": "Try cooking one new recipe each week!",
    "june": "Do a digital detox every evening!",
    "july": "Drink at least 2 liters of water daily!",
    "august": "Practice meditation for 10 minutes daily!",
    "september": "Spend 15 minutes each day learning a new language!",
    "october": "Do a random act of kindness each day!",
    "november": "Write down three things you're grateful for every day!",
    "december": None,
}


def index(request):
  
    months = list(challenges.keys())
   

    return render(request, "challenges/index.html", {"months": months})

   
def monthly_challenge(request, month):
    text = ""

    try:

        challenge_text = challenges[month]
        # return  render(request, "challenges/challenge.html",{
        #    "text":challenge_text,'month':month
        # })
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        #  response_data = render_to_string('404.html')
        return Http404()


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months) or month < 1:
        return HttpResponseNotFound("month not supported")

    converted_month = months[month - 1]

    redirect_path = reverse(
        "month-challenge", args=[converted_month]
    )  # challenges/january

    return HttpResponseRedirect(redirect_path)
