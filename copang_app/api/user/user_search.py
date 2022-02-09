from rest_framework.views import APIView
from rest_framework.response import Response

from copang_app.models import Users
from copang_app.serializers import UsersSerializer

class UserSearch(APIView):
    def get(self, request):
        # keyword = request.GET['keyword']
        
        db_search_users = Users.objects.all()
        
        users_serialized = UsersSerializer(db_search_users, many=True)
        
        return Response({
            'users': users_serialized.data
        })