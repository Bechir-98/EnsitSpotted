from django.shortcuts import render, redirect
from .forms import SpottedMessageForm

def home(request):
    if request.method == 'POST':
        form = SpottedMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SpottedMessageForm()

    return render(request, 'core/home.html', {'form': form})
