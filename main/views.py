from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm': '2406432633',
        'name': 'Dimas Abyan Diasta',
        'class': 'PBP C',
        'shop_name': '⚽ BolaBeliShop ⚽',
    }
    return render(request, "main.html", context)