from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from models import Note
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request, 'include.html')

@csrf_exempt
def api(request):
	if request.method == 'POST':
		Note.objects.create(label=request.POST.get('text'))

	data = serializers.serialize('json', Note.objects.all())
	return JsonResponse(json.loads(data), safe=False)

def kanban(request):
	return render(request, 'kanban.html')