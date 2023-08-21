from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q


from .models import Genre, Game, Studio
from .serializers import GameSerializer, StudioSerializer, GenreSerializer

# def games_list(request):
#     game_lst = Game.objects.all()
#     serializer = GameSerializer(game_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)

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
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
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


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:  #для ввода поиска через строку: http://127.0.0.1:8000/game-search/?key_word=
            key_word = request.GET['key_word']
        elif 'key_word' in request.data: #для ввода поиска через форму (фронтенд)
            key_word = request.data['key_word']
        else: #защита от дурака
            return Response('no data', status=400)

        games = Game.objects.filter(
            Q(name__icontains=key_word) |
            Q(genre__name__icontains=key_word) |
            Q(studio__name__icontains=key_word)
        )

        serializer = GameSerializer(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)