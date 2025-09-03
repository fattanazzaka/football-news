from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406423276',
        'name': 'Muhammad Fattan Azzaka',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
