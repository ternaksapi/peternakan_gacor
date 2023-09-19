from django.shortcuts import render
from main.forms import ItemsForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Items
from django.core import serializers

# Create your views here.
def show_main(request):
    items = Items.objects.all()
    context = {
        'products' : items
    }
    return render(request, "main.html", context)

def create_items(request):
    form = ItemsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form' : form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")