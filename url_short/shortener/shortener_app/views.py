from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from .models import Urls
from .forms import SubmitUrlForm


def home_view(request,*args,**kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request,'shortener_app/home.html',{})


class HomeView(View):
    def get(self,request,*args,**kwargs):
        t_form = SubmitUrlForm()
        context = {"title": "URL Shortener","form":t_form}
        return render(request,"shortener_app/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {"title": "URL Shortener",'form': form}
        template = 'shortener_app/home.html'
        if form .is_valid():
            new_url = form.cleaned_data.get('url')
            obj,created = Urls.objects.get_or_create(url = new_url)
            context = {'object': obj, 'created':created}
            if created:
                template = 'shortener_app/success.html'
            else:
                template = 'shortener_app/already-exists.html'
        return render(request, template, context)

def redirect(request, short_url=None, *args, **kwargs):
    obj = get_object_or_404(Urls, short_url=short_url)
    return HttpResponseRedirect(obj.url)
