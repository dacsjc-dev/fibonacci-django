from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from django.http import HttpResponse

from .models import Fibonacci as FibonacciModel
from .serializers import FibonacciSerializer
from .fibonacci import Fibonacci

def index(request):
    return HttpResponse("Hello, world. You're at fibonacci tool.")

@api_view(['GET', 'POST'])
def fibonacci_list(request, format=None):
    try:
        if request.method == 'GET':
            fibonaccis = FibonacciModel.objects.all()
            serializer = FibonacciSerializer(fibonaccis, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            if (request.data['n']):
                result = Fibonacci().create_fibonacci(request.data['n'])
                resultStatus = status.HTTP_201_CREATED

                if result['status'] == "Invalid":
                    resultStatus = status.HTTP_400_BAD_REQUEST

                return Response(result, status=resultStatus)
    
            raise KeyError()
    except KeyError:
        result = dict()
        result['status'] = "Invalid"
        result['message'] = "Missing n value"
        return Response(result, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fibonacci_detail(request, id, format=None):
    try:
        fibonacci = FibonacciModel.objects.get(pk=id)
    except FibonacciModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = (fibonacci)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FibonacciSerializer(fibonacci, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fibonacci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)