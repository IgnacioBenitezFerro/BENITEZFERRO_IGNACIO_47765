from django import forms
from .models import Market, Buyer, Seller, Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class MarketForm(forms.ModelForm):
    
    class Meta:
        
        model = Market
        fields = '__all__'
        

class BuyerForm(forms.ModelForm):
    
    class Meta:
        
        model = Buyer
        fields = '__all__'

class SellerForm(forms.ModelForm):
    
    class Meta:
        
        model = Seller
        fields = '__all__'
        
class UserRegister(UserCreationForm):
        
        email = forms.EmailField()
        username = forms.CharField()
        password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
        password2 = forms.CharField(label="Password check", widget=forms.PasswordInput)

        class Meta:
            
            model = User
            fields = ["username", "email", 
                      "password1", "password2"]
            
class UserEditForm(UserCreationForm):
    
    username = forms.CharField(label = "Change Username")
    email = forms.EmailField(label = "Change E-mail")
    password1 = forms.CharField(label= "Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label= "Password Check", widget = forms.PasswordInput)    
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2"]    
        
class AvatarEditForm(forms.ModelForm):
    
    class Meta:
        
        model = Avatar
        fields = ['imagen']
