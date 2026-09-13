from django.shortcuts import render

# Create your views here.
def about_section(request):
    return render(request, 'about_section.html')