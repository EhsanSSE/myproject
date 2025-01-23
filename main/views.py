from django.shortcuts import render, redirect
from main.forms import ContactForm, NewslatersForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.name = "UNKNOWN"
            new_contact.save()
            messages.success(request, 'Your form has been successfully submitted!')
            return redirect('main:contact')
        else:
            messages.error(request, 'Please correct the errors in the form and try again.')


    form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def newslaters_view(request):
    if request.method == 'POST':
        form = NewslatersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been successfully submitted!')
            return redirect('main:index')
        else:
            messages.error(request, 'Please correct the errors in the form and try again.')
            return redirect('main:index')
    else:
        return redirect('main:index')
    

