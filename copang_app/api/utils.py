import jwt
import my_custom_settings

from copang_app.models import Users
from functools import wraps

# 사용자 정보를 가지고 -> 토큰 생성하기.
def encode_token(user):
    
    return jwt.encode(
        {'id': user.id, 'email': user.email, 'password': user.password_hashed},
        my_custom_settings.JWT_SECRET_KEY, # 비밀키
        my_custom_settings.JWT_ALGORITHM, # 어떤 알고리즘
    )
    
def decode_token(token):
    # 암호화된 토큰 -> 복호화 : dict 가 나옴 (id, email, pw)
    # 복호화 실패? => 토큰이 잘못됨. 토큰에 맞는 사용자 없다.
    # 복호화 성공 -> id/email/pw이 틀렸다? 이미 만료된 토큰. -> 토큰에 맞는 사용자 없다.
    
    try:
        decoded_dict = jwt.decode(
            token,
            my_custom_settings.JWT_SECRET_KEY,
            algorithms= my_custom_settings.JWT_ALGORITHM
        )
        
        user = Users.objects\
            .filter(id = decoded_dict['id'])\
            .filter(email = decoded_dict['email'])\
            .filter(password_hashed = decoded_dict['password'])\
            .first()
            
        # 성공했다면, 실제 사용자. 없다면 None
        return user
        
    except jwt.exceptions.DecodeError:
        # 복호화 중에 문제 발생.
        # 토큰이 잘못됬다. => 사용자 없다고 return
        return None
    
    
# 데코레이터 - @추가함수 형태로, 본 함수 실행 전에 추가기능을 우선 수행하도록.
def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        
        print('토큰필요기능')
        print('변수 목록 - ', args)
        print('키워드가 붙은 변수 목록 - ', kwargs)
        
        print('리퀘스트 변수의 헤더의 토큰 - ', args[1].headers['X-Http-Token'])
        
        # 추가 행동을 하고 나면, 본 함수를 실행하게.
        return func(*args, **kwargs)
    
    # 위의 decorator에 적힌 내용을 실행하도록
    return decorator