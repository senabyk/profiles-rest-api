from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods ad function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview })
