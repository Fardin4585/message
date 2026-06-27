from django.shortcuts import render, redirect
from .models import Message

# Create your views here.
def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        if name and text:
            Message.objects.create(name=name, text=text)

        return redirect('home')

    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'message/home.html', {'messages': messages})

