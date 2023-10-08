from django.urls import path 
from AppPFEtrade.views import * 
from django.contrib.auth.views import LogoutView




urlpatterns = [
    
    path("inicio/",inicio, name = "Inicio" ),
    path('market/', market, name = "Market"),
    path('buyer/', buyer, name = "Buyer"),
    path('seller/', seller , name = "Seller"),
    path('marketform/', marketForm, name = "mktform"),
    path('buyerform/', buyerForm, name = "byrform"),
    path('sellerform/', sellerForm, name = "slrform"),
    path('searcht/', searchTicker, name = "srchticker"),
    path("result/", matches, name="match"),
    path("sellerticker/", searchSeller, name="sellerfind"),
    path("buyerticker/", searchBuyer, name="buyerfind"),
    path("marketupdate/", searchMarket, name="marketfind"),
    path("delmarket/<marketPosition>/", deleteMarket, name="DeletePosition"),
    path("delbuyer/<buyerTicker>/", deleteBuyer, name="DeleteTicker"),
    path("delseller/<sellerTicker>/", deleteSeller, name="DeleteSTicker"),
    path('editmarket/<pk>', MarketUpdateView.as_view(), name="editmarket"),
    path('editbuyer/<pk>', BuyerUpdateView.as_view(), name="editbuyer"),
    path('editseller/<pk>', SellerUpdateView.as_view(), name="editseller"),
    path('login/', LogIn, name="log"),
    path('registeruser/', Register),
    path("logout/", LogoutView.as_view(template_name="AppPFEtrade/logout.html")),
    path("aboutme/", AboutMe),
    path("editprofile/", editProfile)
    
   
    
    
    
    
]