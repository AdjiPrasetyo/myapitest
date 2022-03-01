from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from car.models import Car

def index(request):
    if request.method == 'GET':
      cars = Car.objects.all()
      response = json.dumps([{'id': car.id, 'name': car.name, 'top_speed': car.top_speed} for car in cars])
    return HttpResponse(response, content_type="text/json")

def getCar(request, car_name):
    if request.method == 'GET':
      try:
        car = Car.objects.get(name=car_name)
        response = json.dumps({'id': car.id, 'name': car.name, 'top_speed': car.top_speed})
      except:
        response = json.dumps({'error': 'Car not found'})
    return HttpResponse(response, content_type="text/json")

def getCarId(request, car_id):
    if request.method == 'GET':
      try:
        car = Car.objects.get(id=car_id)
        response = json.dumps({'id': car.id, 'name': car.name, 'top_speed': car.top_speed})
      except:
        response = json.dumps({'error': 'Car not found'})
    return HttpResponse(response, content_type="text/json")

@csrf_exempt
def addCar(request):
    if request.method == 'POST':
      payload = json.loads(request.body)
      car_name = payload['name']
      top_speed = payload['top_speed']
      car = Car(name=car_name, top_speed=top_speed)
      try:
        car.save()
        response = json.dumps({ 'Succes': 'Car added' })
      except:
        response = json.dumps({ 'Error': 'Car not added' })
    else :
      response = json.dumps({ 'Error': 'Method not allowed' })
    return HttpResponse(response, content_type="text/json")

@csrf_exempt
def updateCar(request, car_id):
    if request.method == 'PUT':
      payload = json.loads(request.body)
      car_name = payload['name']
      top_speed = payload['top_speed']
      car = Car.objects.get(id=car_id)
      try:
        car.name = car_name
        car.top_speed = top_speed
        car.save()
        response = json.dumps({ 'Succes': 'Car updated' })
      except:
        response = json.dumps({ 'Error': 'Car not updated' })
    else :
      response = json.dumps({ 'Error': 'Method not allowed' })
    return HttpResponse(response, content_type="text/json")

def deleteCar(request, car_id):
    if request.method == 'DELETE':
      car = Car.objects.get(id=car_id)
      try:
        car.delete()
        response = json.dumps({ 'Succes': 'Car deleted' })
      except:
        response = json.dumps({ 'Error': 'Car not deleted' })
    else :
      response = json.dumps({ 'Error': 'Method not allowed' })
    return HttpResponse(response, content_type="text/json")