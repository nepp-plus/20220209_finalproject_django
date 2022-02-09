
from rest_framework.views import APIView
from rest_framework.response import Response

class User(APIView):
    
    def post(self, request):
        
        input_email = request.POST['email']
        input_pw = request.POST['password']
        
        print(f'이메일 - {input_email}, 비번 - {input_pw}')
        
        return Response({
            'code': 200,
            'message': '임시- 로그인 기능'
        })