from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status


class GetData(APIView):
    def get(self, request, type='users'):
        if type == 'users':
            response = requests.get('https://fakestoreapi.com/users')
            data = response.json()
            status_code= response.status_code
            
        elif type == 'products':
            response = requests.get('https://fakestoreapi.com/products')
            data = response.json()
            status_code= response.status_code

        else:
            data = {
                "message":"Invalid type given"
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(data,status_code)


