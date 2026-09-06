from django.shortcuts import render
from found_items import models as found_models
from lost_items import models as lost_models

def home(request):
    found_items = found_models.ReportFoundItem.objects.all()
    lost_items = lost_models.ReportLostItem.objects.all()
    return render(request, 'home.html', {
        'found_items': found_items,
        'lost_items': lost_items,
    })