
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from  .serializers import *

@api_view(['GET'])
def home(request):

    person1 = {
        "name" : "shipon hossain",
        "age": 18,
        "is_married": "False"
    },
    person2 = {
        "name" : "ratul hossain",
        "age": 18,
        "is_married": "False"
    }
    person_list =[person1,person2]

    return Response(person_list)

@api_view(['GET'])
def Todo_list(request):
    todos = Todo.objects.all()

    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)

