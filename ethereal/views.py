from django.shortcuts import render, redirect

from .models import Testimonial, Contact, Ethereal, About, Work


def home(request):
    ethereal = Ethereal.objects.all().order_by('id')[:3]
    work = Work.objects.all().order_by('-id')[4:]
    testimonial = Testimonial.objects.all().order_by('id')[:3]
    about = About.objects.get(id=1)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )

        return redirect('home')
    
    context = {
        'ethereal': ethereal,
        'work': work,
        'testimonial': testimonial,
        'about': about,
    }

    return render(request, 'index.html', context)
