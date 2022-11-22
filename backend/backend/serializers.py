from rest_framework import serializers
from .models import Fibonacci as FibonacciModel

class FibonacciSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibonacciModel
        fields = ['id','input_value', 'fibonacci_value', 'status']