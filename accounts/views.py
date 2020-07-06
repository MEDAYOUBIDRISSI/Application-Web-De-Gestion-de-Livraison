from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    liste = Client.objects.all()
    return render(request, "indexv2.html", {"liste": liste})
   # return render(request, 'dashboard.html')

def registerView(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})




###################


# def index(request):
#     liste = Client.objects.all()
#     return render(request, "indexv2.html", {"liste": liste})


def afficheclient(request,id):
    client1 = Client.objects.get(id= id)
    liste = Livraison.objects.filter(client= client1)
    return render(request, "afficheclient.html", {"liste" : liste,"client": client1})


def addclient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST or None)
        if form.is_valid():
            form.save()
            liste = Client.objects.all()
            return redirect('dashboard')
            #return render(request, 'indexv2.html', {"liste" : liste})
    else:
        return render(request, 'addClient.html')



def editeclient(request,id):
    if request.method == 'POST':
        client = Client.objects.get(id= id)
        form = ClientForm(request.POST or None)
        if form.is_valid():
            client.nome = form.cleaned_data['nome']
            client.prenom = form.cleaned_data['prenom']
            client.tel = form.cleaned_data['tel']
            client.adress = form.cleaned_data['adress']
            client.save()
            #liste = Client.objects.all()
            return redirect('dashboard')
            #return render(request, 'indexv2.html', {"liste" : liste})
    else:
        client = Client.objects.get(id= id)
        return render(request, 'editeClient.html',{"client": client})


def deleteclient(request, id):
    client = Client.objects.get(id= id)
    client.delete()
    #liste = Client.objects.all()
    return redirect("dashboard")
    #return render(request, 'indexv2.html', {"liste" : liste})
    # messages.success(request, ('client est supprimer'))



#Gestion Livraison


def leurlivraison(request,id):
    client1 = Client.objects.get(id= id)
    liste = Livraison.objects.filter(client= client1)
    return render(request, "leurlivraison.html", {"liste" : liste,"client": client1})



def addlivraison(request,id):
    client1 = Client.objects.get(id= id)
    if request.method == 'POST':
        form = LivarisonForm(request.POST or None)

        if form.is_valid():
            liv=Livraison()
            liv.libelle= form.cleaned_data['libelle']
            liv.date= form.cleaned_data['date']
            liv.client= client1
            liv.save()
            # form.save()
            liste = Livraison.objects.filter(client= client1)
            return render(request,"leurlivraison.html", {"liste" : liste,"client": client1})
    else:
        return render(request, 'addlivraison.html',{"client": client1}) 

def editelivraison(request,id,id_liv):
    client1 = Client.objects.get(id= id)
    liv = Livraison.objects.get(id= id_liv)
    if request.method == 'POST':
        form = LivarisonForm(request.POST or None)
        if form.is_valid():
            liv.libelle = form.cleaned_data['libelle']
            liv.date = form.cleaned_data['date']
            liv.save()
            liste = Livraison.objects.filter(client= client1)
            return render(request,"leurlivraison.html", {"liste" : liste,"client": client1})
    else:
        return render(request, 'editelivraison.html',{"client": client1,"livraison": liv})


def deletelivraison(request, id,id_liv):
    liv = Livraison.objects.get(id= id_liv)
    liv.delete()
    client1 = Client.objects.get(id= id)
    liste = Livraison.objects.filter(client= client1)
    # return redirect("index")
    return render(request,"leurlivraison.html", {"liste" : liste,"client": client1})


