from django.shortcuts import render
from django.views.generic import ListView, View
from .models import User
from django.http import JsonResponse

# Create your views here.

class CrudView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'app/crud.html'


class CreateCrudUser(View):
    def get(self, request):
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        hobbies = request.GET.get('hobbies', None)
        gender = request.GET.get('gender', None)

        obj = User.objects.create(
            name = name,
            email = email,
            hobbies = hobbies,
            gender = gender,
        )

        user = {'id':obj.id,'name':obj.name,'email':obj.email,'hobbies':obj.hobbies, 'gender':obj.gender}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        email = request.GET.get('email', None)
        hobbies = request.GET.get('hobbies', None)
        gender = request.GET.get('gender', None)

        obj = User.objects.get(id=id1)
        obj.name = name1
        obj.email = email
        obj.hobbies = hobbies
        obj.gender = gender
        obj.save()

        user = {'id': obj.id,'name': obj.name, 'email': obj.email,'hobbies': obj.hobbies, 'gender': obj.gender}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        User.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)