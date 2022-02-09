import jwt
import my_custom_settings

from copang_app.models import Users

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