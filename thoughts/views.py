from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Thought
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

import requests
from django.core.cache import cache

def fetch_quote_for_mood(mood):
    """
    Fetch a quote. Optionally, you could pass mood to refine which quotes to fetch.
    For simplicity, we’ll fetch a generic quote and later you could map mood‑to‑category.
    """
    # Try cache
    quote = cache.get(f"quote_for_{mood}")
    if quote:
        return quote

    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            quote = {
                "text": data["q"],
                "author": data["a"]
            }
            # Cache for e.g. 6 hours
            cache.set(f"quote_for_{mood}", quote, 6 * 60 * 60)
            return quote
    except Exception as e:
        print("Error fetching quote:", e)

    # Fallback quote
    return {
        "text": "Keep going, you’re doing great!",
        "author": "Unknown"
    }


@login_required(login_url="login")
def dashboard(request):
    today = timezone.localdate()
    try:
        todays_thought = Thought.objects.get(user=request.user, date=today)
        mood = todays_thought.mood
    except Thought.DoesNotExist:
        todays_thought = None
        mood = None

    if mood:
        quote = fetch_quote_for_mood(mood)
    else:
        quote = None

    return render(request, 'thoughts/dashboard.html', {
        'todays_thought': todays_thought,
        'quote': quote
    })

@login_required(login_url="login")
def add_thought(request):
    today = timezone.localdate()

    # Check if the user already has a thought today
    if Thought.objects.filter(user=request.user, date=today).exists():
        messages.error(request, "You have already posted a thought today!")
        return redirect('dashboard')

    if request.method == "POST":
        text = request.POST.get("text")
        mood = request.POST.get("mood")
        tag = request.POST.get("tag")

        if not text.strip():
            messages.error(request, "Thought cannot be empty.")
            return render(request, "thoughts/add_thought.html")

        Thought.objects.create(
            user=request.user,
            text=text,
            mood=mood,
            tag=tag
        )
        messages.success(request, "Your thought has been posted!")
        return redirect('dashboard')


    return render(request, "thoughts/add_thought.html")