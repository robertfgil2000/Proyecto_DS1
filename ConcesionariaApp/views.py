from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

def home(request):
    return render(request, "ConcesionariaApp/home.html")

def login(request):
    return render(request, "ConcesionariaApp/login.html")


#User

@csrf_exempt
def user_create(request):
    if request.method == 'POST': 
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email') 
        name = data.get('name')
        phone = data.get('phone') 
        password = data.get('password') 
        User.user_create(email,name,phone,password)
        return JsonResponse({'status': 'OK', 'user':{
            'email': email, 
            'name': name, 
            'phone': phone, 
            'password': password
        }}, status=200)
    else:
        return JsonResponse({'status': 'ERROR'}, status=405)


@csrf_exempt
def user_get_all(request):
    if request.method == 'GET':
        users = User.user_get_all()
        data = {'users': []}
        for user in users:
            data['users'].append({
                'id': user.user_id,
                'email': user.email, 
                'name': user.name, 
                'phone': user.phone, 
                'password': user.password,
            })
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'ERROR'}, status=405)


@csrf_exempt
def user_get(request, user_id):
    if request.method == 'GET':
        try:
            user = User.user_get(user_id)
            data = {
                'id': user.user_id,
                'email': user.email, 
                'name': user.name, 
                'phone': user.phone, 
                'password': user.password,
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return JsonResponse({'status': 'ERROR', 'message': 'dont exists'}, status=404)
    else:
        return JsonResponse({'status': 'ERROR'}, status=405)


@csrf_exempt
def user_delete(request, user_id): 
    if request.method == 'DELETE':
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return JsonResponse({'status': 'Ok, deleted'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ERROR', 'message': 'User dont exists'}, status=404)
    else:
        return JsonResponse({'status': 'ERROR'}, status=405)


@csrf_exempt
def user_modify(request, user_id):
    if request.method == 'PUT':
        try:
            user = User.objects.get(user_id=user_id)
            data = json.loads(request.body.decode('utf-8'))

            email = data.get('email', None) 
            name = data.get('name', None)
            phone = data.get('phone', None) 
            password = data.get('password', None) 

            user.user_modify(email, name, phone, password)
            return JsonResponse({'status': 'OK', 
                                 'user': {
                                        'id': user.user_id,
                                        'email': user.email, 
                                        'name': user.name, 
                                        'phone': user.phone, 
                                        'password': user.password,  
                                        }
                                })
        except User.DoesNotExist:
            return JsonResponse({'status': 'ERROR', 'message': 'User dont exists'}, status=404)    
    else:
        return JsonResponse({'status': 'ERROR'}, status=405)