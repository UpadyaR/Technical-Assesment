from django.shortcuts import render
from website.models import Ganison_dataset_1

# Create your views here.
def table_view(request):
    data = Ganison_dataset_1.objects.all()
    return render(request, 'table_view.html', {'data': data})