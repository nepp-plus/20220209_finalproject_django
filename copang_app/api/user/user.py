
from rest_framework.views import APIView
from rest_framework.response import Response

class User(APIView):
    
    def post(self, request):
        return Response({
            'code': 200,
            'message': '임시- 로그인 기능'
        })