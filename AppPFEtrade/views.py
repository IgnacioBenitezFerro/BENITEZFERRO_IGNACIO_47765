from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppPFEtrade.models import Market, Buyer, Seller, Avatar
from django.shortcuts import render, redirect
from AppPFEtrade.forms import UserRegister, User, UserEditForm
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='/APPFE/login/')
def market(request):
     
  avatar = Avatar.objects.filter(user=request.user.id).first()
  
  if avatar: #Usamos para verificar si existe una imagen, si no existe arroja una predeterminada para un valor nulo
    avatar_url = avatar.imagen.url
  else:
    avatar_url = None
     
  return render(request, "AppPFEtrade/market.html", {'url' : avatar_url}) #Pasamos como contexto la imagen al block del html padre (si entendi bien ;) )
   
@login_required(login_url='/APPFE/login/')
def buyer(request):
  
  avatar = Avatar.objects.filter(user=request.user.id).first()
  
  if avatar:
    avatar_url = avatar.imagen.url
  else:
    avatar_url = None
  
  return render(request, "AppPFEtrade/buyer.html", {'url': avatar_url} )

@login_required(login_url='/APPFE/login/')
def seller(request):
  
  avatar = Avatar.objects.filter(user=request.user.id).first()  
  
  if avatar:
    avatar_url = avatar.imagen.url
  else:
    avatar_url = None
  
  return render(request, "AppPFEtrade/seller.html", {'url': avatar_url} )
  

def inicio(request):
    
  avatar = Avatar.objects.filter(user=request.user.id).first()
  
  if avatar:
    avatar_url = avatar.imagen.url
  else:
    avatar_url = None
  
  return render(request, "AppPFEtrade/inicio.html",{'url': avatar_url} )
 

 
@login_required(login_url='/APPFE/login/')
def prueba(request):
    
    return render(request, "AppPFEtrade/padre.html")
 
#Añadir  

def marketForm(request):
    
    if request.method == "POST":
        
      market = Market(position=request.POST["pos"],
                      ticker=request.POST["tck"],
                      price=request.POST["pri"])
      
      market.save()
      
      return render(request, "AppPFEtrade/market.html")

    
    return render(request,"AppPFEtrade/marketform.html" )


def buyerForm(request):
    
    if request.method == "POST":
        
      market = Buyer(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/buyer.html")

    
    return render(request,"AppPFEtrade/buyerform.html" )


def sellerForm(request):
    
    if request.method == "POST":
        
      market = Seller(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/seller.html")

    
    return render(request,"AppPFEtrade/sellerform.html" )
  
  
def searchTicker(request):
  
  return render(request, "AppPFEtrade/market.html")
  
  
def matches(request): 
  
  if request.GET["ticker"]:
    
    ticker=request.GET["ticker"]
    markets = Market.objects.filter(ticker__iexact=ticker)
    
    return render(request, "AppPFEtrade/market.html", {"ticker" : ticker, "markets" : markets})
  
  else:
    
    res = "No fullfilled data!"
    
  return HttpResponse(res)

#Buscar / Mostrar

def searchSeller(request):
  
  ticker = Seller.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/sellerupdate.html", context)

def searchBuyer(request):
  
  ticker = Buyer.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/buyerupdate.html", context)

def searchMarket(request):
  
  ticker = Market.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/marketupdate.html", context)


#Eliminar

def deleteMarket(request, marketPosition):
  
  position = Market.objects.get(position=marketPosition)
  position.delete()
  
  positions = Market.objects.all()

  context = {"position" : positions}
  
  return render(request,"AppPFE/marketupdate.html", context)


def deleteBuyer(request, buyerTicker):
  
  ticker = Buyer.objects.get(mail=buyerTicker)
  ticker.delete()
  
  tickers = Buyer.objects.all()

  context = {"ticker" : tickers}
  
  return render(request,"AppPFE/buyerupdate.html", context)

def deleteSeller (request, sellerTicker):
  
  ticker = Seller.objects.get(mail=sellerTicker)
  ticker.delete()
  
  tickers = Seller.objects.all()

  context = {"ticker" : tickers}
  
  return render(request,"AppPFE/sellerupdate.html", context)


#Editar


from django.views.generic.edit import UpdateView
from .models import Market
from .forms import MarketForm, SellerForm, BuyerForm

class MarketUpdateView(LoginRequiredMixin, UpdateView):
  
    model = Market
    
    form_class = MarketForm
    
    template_name = 'AppPFEtrade/edit_market.html' 
    
    success_url = '/APPFE/market/'
    
    
class BuyerUpdateView(LoginRequiredMixin, UpdateView):
  
    model = Buyer
    
    form_class = BuyerForm
    
    template_name = 'AppPFEtrade/edit_buyer.html' 
    
    success_url = '/APPFE/buyer/'
    

class SellerUpdateView(LoginRequiredMixin, UpdateView):
  
    model = Seller
    
    form_class = SellerForm
    
    template_name = 'AppPFEtrade/edit_seller.html' 
    
    success_url = '/APPFE/seller/'

#lOGIN

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def LogIn(request):
  
  if request.method == "POST":
    
    form = AuthenticationForm(request, data = request.POST)
    
    if form.is_valid():
      
      usr = form.cleaned_data.get("username")
      psw = form.cleaned_data.get("password")
      
      user = authenticate(username = usr, password = psw)
      
      if user:
        
        login(request, user)
        
        return render(request, "AppPFEtrade/inicio.html", {"msg":f"Good to see you back {user}!"})
    
    else:
      
      return render(request, "AppPFEtrade/inicio.html", {"msg":"Invalid data!"})
  
  else:
    
    form = AuthenticationForm()
  
  return render(request,"AppPFEtrade/login.html", {"formulary":form} )

#Register

def Register(request):
  
  if request.method == "POST":
    
    form = UserRegister(request.POST)
    
    if form.is_valid():
      
      usr = form.cleaned_data["username"]
      form.save()
      return render(request, "AppPFEtrade/inicio.html",{"msg":"User successfully created!"})
  
  else:
    
    form = UserRegister()
  
  return render(request,"AppPFEtrade/register.html", {"formulary":form})


#About Me

def AboutMe(request):
     
     return render(request, "AppPFEtrade/aboutme.html")


#Edit User

from AppPFEtrade.forms import AvatarEditForm


def editProfile(request):
  
    user = request.user
    
    avatar, created = Avatar.objects.get_or_create(user=user)  #Deberia crearnos un user nuevo en caso de que no exista, me parecio bastante interesante esta opcion.

    if request.method == "POST":
      
        user_form = UserEditForm(request.POST)
        
        avatar_form = AvatarEditForm(request.POST, request.FILES, instance=avatar)

        if user_form.is_valid() and avatar_form.is_valid():
          
            info = user_form.cleaned_data

            user.username = info["username"]
            user.email = info["email"]
            user.set_password(info["password1"])
            user.save()

            updated_avatar = avatar_form.save(commit=False)
            updated_avatar.user = user  
            updated_avatar.save()

            return redirect('Market') # Este es el name de mi URL, aprendi a usarlo recien ahora como un "Atajo"

    else:
        user_form = UserEditForm(initial={'email': user.email, 'username': user.username, 'password1': user.password})
        
        avatar_form = AvatarEditForm(instance=avatar)

    return render(request, "AppPFEtrade/editprofile.html", {"formulary": user_form, "avatar_form": avatar_form, "user": user})
