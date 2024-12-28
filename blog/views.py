from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About, Facts, Offer, Products, Team, Service, Testimonial
from .forms import NewsletterForm, ContactForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.
class AboutUpdateView(UpdateView):
    model = About
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'AboutEdit.html'

class AboutDeleteView(DeleteView):
    model = About
    template_name = 'AboutDelete.html'
    success_url = reverse_lazy('index')

class AboutCreateView(CreateView):
    model =About
    template_name = 'AboutCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Aboutdetail(request, about):
    about = get_object_or_404(About, slug=about)
    context = {
        'about': about
    }
    return render(request, 'aboutDetailView', context=context)

def index(request):
    offer = Offer.objects.all()
    about = About.objects.all()
    facts = Facts.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    service = Service.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    products = Products.objects.all()
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "offer": offer,
        "about": about,
        "facts": facts,
        "team": team,
        "testimonial": testimonial,
        "service": service,
        "products": products,
        "contact": contact,
        "newsletter": newsletter
    }
    return render(request, 'index.html', context=context)
def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }

    return render(request, 'about.html', context=context)
def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)
def menu(request):
    products = Products.objects.all()
    context = {
        'products': products
    }

    return render(request, 'menu.html', context=context)
def service(request):
    service = Service.objects.all()
    context = {
        'service': service
    }

    return render(request, 'service.html', context=context)
def team(request):
    team = Team.objects.all()
    context = {
        'team': team
    }

    return render(request, 'team.html', context=context)
def testimonial(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }

    return render(request, 'testimonial.html', context=context)
def newsletter(request):
    newsletter =NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "newsletter": newsletter
    }
    return render(request, 'newsletter.html', context=context)
def teamdetail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'x': team
    }
    return render(request, 'teamdetail.html', context=context)

def testimonialdetail(request, id):
    testimonial = Testimonial.objects.get(id=id)
    context = {
        'x': testimonial
    }
    return render(request, 'testimonialdetail.html', context=context)

def offerdetail(request, id):
    offer= Offer.objects.get(id=id)
    context = {
        'x': offer
    }
    return render(request, 'offerdetail.html', context=context)

def servicedetail(request, id):
    service = Service.objects.get(id=id)
    context = {
        'x': service
    }
    return render(request, 'servicedetail.html', context=context)
def factsdetail(request, id):
    facts = Facts.objects.get(id=id)
    context = {
        'x': facts
    }
    return render(request, 'factsdetail.html', context=context)

def productsdetail(request, id):
    products = Products.objects.get(id=id)
    context = {
        'x': products
    }
    return render(request, 'productsdetail.html', context=context)
def aboutdetail(request, id):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'aboutdetail.html', context=context)