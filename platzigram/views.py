#platzigram views
#django
from django.http import HttpResponse, JsonResponse
#utilities
from datetime import datetime

def helloWorld(request):
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse("Hora actual is {now}".format(now = str(now)))

def sortedNumbers(request):
	""" Return a JSON response with sorted integers"""
	# pdb es un debuger de python
	# import pdb; pdb.set_trace()
	if len(request.GET):
		numbers = request.GET['numbers']
		numbers = numbers.split(",")
		numbers = list(map(int, numbers))
		numbers.sort()
		res = numbers
	else:
		res = "NO HAY NUMEROS!"
	return JsonResponse(res, safe=False)

def sayHi(request, name, age):
	""" Return a greeting. """
	if age < 12:
		message = "Sorry {}, eres menor de 12 años y no puedes entrar".format(name)
	else:
		message = "Bienvenido {}, acabas de entrar a Juaku!".format(name)
	return  HttpResponse(message)