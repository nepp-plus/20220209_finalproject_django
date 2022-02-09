
from rest_framework.views import APIView
from rest_framework.response import Response

from copang_app.models import Users
from copang_app.serializers import UsersSerializer

from copang_app.api.utils import encode_token

class User(APIView):
    
    def get(self, request):
        
        print('헤더 출력 - ', request.headers['X-Http-Token'])
        
        return Response({
            'code': 200,
            'message': '임시 - 내 정보 조회',
        })
    
    def post(self, request):
        
        input_email = request.POST['email']
        input_pw = request.POST['password']
        
        print(f'이메일 - {input_email}, 비번 - {input_pw}')
        
        # 이메일만 가지고 사용자 검색.
        
        email_user = Users.objects.filter(email=input_email).first()
        
        if email_user:
            # 임시 - 비번은 암호화 되어있고, django에서는 아직 기능 구현 안됨.
            # 이메일 만 맞으면 성공.
            
            if email_user.is_same_password(input_pw):
                user_serialized = UsersSerializer(email_user)
                
                return Response({
                    'code': 200,
                    'message': '로그인 성공',
                    'data': {
                        'user': user_serialized.data,
                        'token': encode_token(email_user)
                    }
                })
            else:
                return Response({
                    'code': 400,
                    'message': '비밀번호가 틀립니다.'
                }, status=400)
        else:
            return Response({
                'code': 400,
                'message': '해당 이메일의 사용자는 존재하지 않습니다.'
            }, status=400)
        
        