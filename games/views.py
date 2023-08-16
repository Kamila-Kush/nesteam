from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Genre, Game, Studio
from .serializers import GameSerializer, StudioSerializer, GenreSerializer

def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializer(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

# def studio_list(request):
#     studio_lst = Studio.objects.all()
#     serializer = StudioSerializer(studio_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

# class CreateGameAPIView(CreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

class GamesView(ListCreateAPIView):
    queryset= Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializer(data=data)
        if serializer.is_valis():
            return Response("все ок")
        else:
            errors = serializer.error_messages
            response_data = {
                "message" : "Данные не валидны",
                "errors" : errors
            }
            return Response(
                data=response_data,
                status=400
            )