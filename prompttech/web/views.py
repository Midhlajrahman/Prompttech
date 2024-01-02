from django.http import JsonResponse
from django.shortcuts import render

from .forms import ContactForm,EnquiryForm
from .models import News
from .models import Portfolio,PortfolioCategory
from .models import Team, Slider
from .models import Service
from .models import About
from .models import Testimonail
from django.shortcuts import render, get_object_or_404


def index(request):
    automation_services = Service.objects.filter(category='HOME_AUTOMATION')
    security_services = Service.objects.filter(category='SECURITY_SURVEILLANCE')
    testimonials = Testimonail.objects.all()
    sliders = Slider.objects.all()
    portfolios = Portfolio.objects.all()[0:10]
    newses = News.objects.all()[0:6]
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "true","title": "Successfully Submitted","message": "Message successfully updated",})
        else:
           return JsonResponse({"status": "false","title": "Form validation error"},status=400)
    else:
        form = EnquiryForm()
        
    context = {"is_index": True, "portfolios": portfolios, "newses": newses, "sliders": sliders, "automation_services": automation_services, "security_services": security_services,"testimonials":testimonials, "form": form}
    return render(request, 'web/index.html', context)


def about_us(request):
    automation_services = Service.objects.filter(category='HOME_AUTOMATION')
    security_services = Service.objects.filter(category='SECURITY_SURVEILLANCE')
    teams = Team.objects.all()
    newses = News.objects.all()[0:6]
    about=About.objects.last()
    testimonials = Testimonail.objects.all()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "true","title": "Successfully Submitted","message": "Message successfully updated",})
        else:
           return JsonResponse({"status": "false","title": "Form validation error"},status=400)
    else:
        form = EnquiryForm()
    context = {"is_about_us": True, "teams": teams, "newses": newses, "automation_services": automation_services, "security_services": security_services,"about":about,"testimonials":testimonials,"form": form}
    return render(request, 'web/about_us.html', context)


def services(request):
    automation_services = Service.objects.filter(category='HOME_AUTOMATION')
    security_services = Service.objects.filter(category='SECURITY_SURVEILLANCE')
    testimonials = Testimonail.objects.all()
    
    context = {
        "automation_services": automation_services,
        "security_services": security_services,
        "is_services": True,
        "testimonials":testimonials,
    }
    return render(request, 'web/services.html', context)

def service_details(request,slug):
    service = get_object_or_404(Service, slug=slug)
    automation_services = Service.objects.filter(category='HOME_AUTOMATION')
    security_services = Service.objects.filter(category='SECURITY_SURVEILLANCE')   
    automation_services = automation_services.exclude(slug=slug)
    security_services = security_services.exclude(slug=slug)

    context = {
        "selected_service": service,
        "automation_services": automation_services,
        "security_services": security_services,
    }
    return render(request,'web/service-details.html',context)


def projects(request):
    portfolios = Portfolio.objects.all()
    portfolio_cat = PortfolioCategory.objects.all()  # Retrieve all services
    context = {"is_portfolios": True, "portfolios": portfolios, "portfolio_cat": portfolio_cat}
    return render(request, 'web/projects.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "true","title": "Successfully Submitted","message": "Message successfully updated",})
        else:
           return JsonResponse({"status": "false","title": "Form validation error"},status=400)
    else:
        form = ContactForm()

    context = {"is_contact_us": True, "form": form}
    return render(request, 'web/contact_us.html', context)


def privacy_policy(request):
    context = {"is_privacy_policy": True}
    return render(request, 'web/privacy_policy.html', context)


def terms_of_use(request):
    context = {"is_terms_of_use": True}
    return render(request, 'web/terms_of_use.html', context)


def service_quote(request, slug):
    service = Service.objects.get(slug=slug)
    context = {"is_service_quote": True, "service": service}
    return render(request, 'web/service_quote.html', context)

