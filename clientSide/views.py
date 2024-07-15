from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import context
from  django.contrib.auth.models import User
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Véhicule,Dépot,Réservation

from  django.views.generic import ListView


def page_accueil(request):
    véhicule = Véhicule.objects.all()
    return render(request, 'rent4you/Page_accueil.html', context={'véhicule': véhicule})











def offre(request, pk):
    query_set = get_object_or_404(Véhicule, pk=pk)
    return render(request, 'rent4you/offre.html', context={'offre': query_set})


def signature(request):
    return render(request, 'rent4you/pdf.html', context={})



def search(request):
    query_set = Véhicule.objects.select_related('id_dépot').filter(disponibilité=True)
    if 'Lieu' in request.GET:
        Lieu = request.GET['Lieu']

        request.session['date1'] = request.GET['date1']
        request.session['time1'] = request.GET['time1']
        request.session['date2'] = request.GET['date2']
        request.session['time2'] = request.GET['time2']

        if Lieu:

            query_set = query_set.filter(id_dépot__adress_dpt= Lieu)
            nmbr = query_set.count()


    context = {
        'query_set': query_set,
        'nmbr' : nmbr,
        'Lieu' : Lieu,

        'values': request.GET
    }
    return render(request, 'rent4you/switch.html', context)


def filter_price(request,Lieu):
    query_set = Véhicule.objects.select_related('id_dépot').filter(disponibilité=True)



    if Lieu:
         query_set = query_set.filter(id_dépot__adress_dpt= Lieu)
    price = request.GET.get('price')
    if price:
        query_set = query_set.filter(prix_jour__lte=price)
    catégorie = request.GET.get('categorie')
    if catégorie:
        catégorie = catégorie.split(',')
        em=[]
        for e in catégorie:
            try:
                em.append(e)
            except Exception as e:
                pass
            print(em)
            query_set = query_set.filter(catégorie_véhicule__in=em).distinct()
    payload=[]
    for car in query_set:
        result = {}
        result['marque']=car.marque
        result['imageURL']=car.imageURL
        result['model']=car.model
        result['description']=car.description
        result['prix_jour']=car.prix_jour
        payload.append(result)


    context = {
        'query_set': query_set,

        'Lieu' : Lieu,

        'values': request.GET
    }
    return render(request, 'rent4you/cars.html', context)
    #return JsonResponse(payload, safe=False)






def register_form(request):
    if request.method == "POST":
        username = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['password']
        myuser = User.objects.create_user(email,email,password)

        myuser.last_name=last_name
        myuser.save()
        messages.success(request,"your account has been successffully created")
        redirect('accueil')

    return render(request, 'rent4you/Inscription.html', context={})


def login_locataire(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user =authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            request.session['lct'] = user.id
            first_name = user.first_name
            return render(request,'rent4you/Page_accueil.html',context={'first_name':first_name})
        else:
            messages.error(request,'error')
            return redirect('list')

def logouts(request):
    logout(request)


    messages.success(request, "logged out Successfully")
    return redirect('accueil')


def historique_réservation(request, id):
    query_set = Réservation.objects.select_related('id_véhicule').filter(pk=id)





    context={'query_set':query_set}
    return render(request,'rent4you/historique.html',context)


def profile(request,id):
    context={}
    return render(request,'rent4you/profile.html',context)


# Filter Data
def filter_data(request):

 return JsonResponse({'data':'ghh'})


def reservation(request, loc,véh, dd, df, prix):
    reservation = Réservation()
    reservation.id_locataire_id=loc
    reservation.id_véhicule_id=véh
    reservation.date_début=dd
    reservation.date_fin=df
    reservation.prix=prix
    reservation.save()


    return render(request, 'rent4you/Page_accueil.html', context={})


def reserv(request):
    return render(request,'rent4you/reservation.html',context={})




