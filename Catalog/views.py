from django.shortcuts import render

# Create your views here.

def home_view(request): # Home page
    return render(request,"index.html")

def user_view(request): # userlogin
    return render(request,"user.html")

def contact_view(request): # contact/about page
    return render(request,"contact.html")

def create_account_view(request): # create account, links to user application form. child of user login
    return render(request,"user_app.html")

def request_loan_view(request): # request loan. child of user login
    return render(request,"request.html")


def manager_view(request): # manager login
    return render(request,"manager.html")

def interest_view(request): # interest rates. child of manager login
    return render(request,"interest.html")

def create_manager_view(request): # create manager account . child of manager login
    return render(request,"manager_app.html")

def loan_view(request): # page to list of loan categories, each category will have functions. child of manager login
    return render(request,"loan.html") 