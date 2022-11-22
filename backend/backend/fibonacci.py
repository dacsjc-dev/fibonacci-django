import time
import random
from .models import Fibonacci as FibonacciModel
from .serializers import FibonacciSerializer

class Fibonacci:
    def __init__(self):
        self.PROCESSING_MSG = "Processing your request..."

    def create_fibonacci(self, n):
        """
        :param n: int
        """
        nterm = int(n)
        result = dict()
        result['status'] = "pending"

        if nterm <= 0:
            result['status'] = "Invalid"
            result['message'] = "Please enter a positive integer"
            return result

        try:
            fibonacci = FibonacciModel.objects.filter(input_value=str(nterm)).first()
            serializer = FibonacciSerializer(fibonacci)

            result['status'] = serializer.data['status']

            if (result['status'] == "pending"):
                result['message'] = self.PROCESSING_MSG
                print('receive: ', serializer.data)
                self.process_fibonacci(id=serializer.data['id'])
            elif (result['status'] == "success"):
                result['nth'] = str(serializer.data['fibonacci_value'])
            elif (result['status'] == "" or serializer.data['input_value'] is None):
                print("Creating Data Inner")
                return self.create_fibonacci_pending(nterm)
            return result
        except FibonacciModel.DoesNotExist:
            print("Creating ")
            return self.create_fibonacci_pending()

    @classmethod
    def create_fibonacci_pending(self, nterm):
        result = dict()
        data = dict()

        result['status'] = "pending"

        data['input_value'] = str(nterm)
        data['status'] = "pending"
        
        print("Creating Data")
        serializer = FibonacciSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            result['message'] =  "Processing your request..."
            self.process_fibonacci(id=serializer.data['id'])
            return result
    
        result['status'] = "Error"
        result['message'] = "Failed to store request of fibonacci in database. Please try again."
        return result

    @classmethod
    def process_fibonacci(self, id):
        id = str(id)
        print("-----------------------------------")
        print("Processing Fibonacci...", id)
        fibonacci = FibonacciModel.objects.get(pk=id)
        print("Processing Fibonacci 2...")
    
        # Tagging Fibonacci Pending's into Processing
        serializedFibonacci = FibonacciSerializer(fibonacci).data

        # UPDATING INTO THE DATABASE
        data = dict()

        print("---id:", serializedFibonacci['id'], ' - input value: ', serializedFibonacci['input_value'])
        nterms = int(serializedFibonacci['input_value'])

        nth, n1, n2 = 0, 0, 1
        count = 0

        while count < nterms - 1:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

        print("---id:", serializedFibonacci['id'], ' - nth value: ', str(n1))
        data = dict()
        data['input_value'] = str(nterms)
        data['fibonacci_value'] = str(n1)
        data['status'] = "success"

        print("---id:", serializedFibonacci['id'], ' - Saving into database...')
        serializer = FibonacciSerializer(fibonacci, data=data)
        if serializer.is_valid():
            serializer.save()
            print("---id:", serializedFibonacci['id'], ' - Updated Successful!')

    def process_fibonacci_batch(self):
        print("-----------------------------------")
        print("Processing Fibonacci...")

        fibonacci = FibonacciModel.objects.filter(status="pending").order_by('-id')[:5]
        print("Processing Fibonacci 2...")
      
        # Tagging Fibonacci Pending's into Processing
        for each in fibonacci:
            serializedFibonacci = FibonacciSerializer(each).data

            # UPDATING INTO THE DATABASE
            data = dict()

            data['input_value'] = str(serializedFibonacci['input_value'])
            data['status'] = "processing"

            serializer = FibonacciSerializer(each, data)
            if serializer.is_valid():
                serializer.save()

        for each in fibonacci:
            serializedFibonacci = FibonacciSerializer(each).data

            print("---id:", serializedFibonacci['id'], ' - input value: ', serializedFibonacci['input_value'])
            nterms = int(serializedFibonacci['input_value'])

            nth, n1, n2 = 0, 0, 1
            count = 0

            while count < nterms - 1:
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1

                # Adding a delay for sync
                #time.sleep(timeDelay)
            print("---id:", serializedFibonacci['id'], ' - nth value: ', str(n1))

            # UPDATING INTO THE DATABASE
            data = dict()
            data['input_value'] = str(nterms)
            data['fibonacci_value'] = str(n1)
            data['status'] = "success"

            print("---id:", serializedFibonacci['id'], ' - Saving into database...')
            serializer = FibonacciSerializer(each, data=data)
            if serializer.is_valid():
                serializer.save()
                print("---id:", serializedFibonacci['id'], ' - Updated Successful!')