from django.shortcuts import render,redirect 



def home(request):
    return render(request, "users/home.html")


    # Proteger la URL para que no accedas de frente con un If pero podemos hacerlo con un decorator en las urls
    # if request.user.is_authenticated:
    #     return render(request, "users/home.html")
    # else:
    #     return redirect('Login')



