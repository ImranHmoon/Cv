from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
import pdfkit
import io


# Create your views here.
def base(request):
    if request.method =='POST':
        name = request.POST.get('name')
        job = request.POST.get('job')
        company = request.POST.get('company')
        university = request.POST.get('university')
        skills = request.POST.get('skills')
        degree = request.POST.get('degree')
        email= request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        phone_number = request.POST.get('phone_number')
        prof = Profile(name=name,company=company,skills=skills,university=university,degree=degree,email=email,job=job,address=address,gender=gender,religion=religion,phone_number=phone_number)
        prof.save()
    return render (request, 'base.html',locals())


def home(request):
    Prof = Profile.objects.all()
    return render (request, 'home.html',locals())


def download(request, id):
    user_prof = Profile.objects.get(id=id)
    template = loader.get_template("download.html")
    html = template.render({'user_prof': user_prof})
    option={
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options=option, configuration=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))
    response = HttpResponse(pdf, content_type='application/pdf')
    response['content-Disposition'] = 'attachment'
    return response




