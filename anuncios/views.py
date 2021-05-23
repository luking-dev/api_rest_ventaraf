from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken import Token
from dotenv import load_dotenv
from api_rest_ventaraf.settings import BASE_DIR, LOAD_ENV

@api_view(['GET'])
def login(request):
    bd_user = os.environ['BD_USER']
    user = User.objects.get(username=bd_user)
    token = Token.objects.create(user=user)
