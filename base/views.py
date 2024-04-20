from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
def blogPageView(request):
    template_name = 'pages/blog.html'
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(request=request, template_name=template_name, context=context)

def blogDetail(request,pk):
    template_name = 'pages/blog_detail.html'
    post = Post.objects.get(pk=pk)
    context = {'post' : post}
    return render(request=request, template_name=template_name, context=context)

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class PricingPageView(TemplateView):
    template_name = 'pages/pricing.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'

class ServiceDetailPageView(TemplateView):
    template_name = 'pages/service_detail.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class BlogDetailPageView(TemplateView):
    template_name = 'pages/blog_detail.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class YuridikPersonPageView(TemplateView):
    template_name = 'pages/yuridik_shaxslar.html'

class JismoniyPersonPageView(TemplateView):
    template_name = 'pages/jismoniy_shaxslar.html'