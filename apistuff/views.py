from rest_framework.views import APIView
from rest_framework.response import Response
from .processor import process

class Process(APIView):


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        resp = "Hi there"
        return Response(resp)
    
    def post(self, request):
        # resp = "posted"
        # print(request.data)
        resp = process(request.data)
        return Response(resp, headers={"Access-Control-Allow-Origin": "*"})
   
       