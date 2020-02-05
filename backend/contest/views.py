import jwt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Contest, Video
from .serializers import ContestSerializer, VideoSerializer
from django.core.mail import send_mail


# Create your views here.

# Contest
class ContestListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        contest = Contest.objects.all().filter(user__id=request.user.id)
        serializer = ContestSerializer(contest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token_decoded = jwt.decode(token, None, None)
        request.data["user"] = token_decoded["user_id"]
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContestDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Contest.objects.get(pk=pk)
        except Contest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contest = self.get_object(pk)
        serializer = ContestSerializer(contest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contest = self.get_object(pk)
        serializer = ContestSerializer(contest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contest = self.get_object(pk)
        contest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Video
class VideoListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateVideoStatus(ListCreateAPIView):
    def post(self, request):
        video = Video.objects.get(id=request.data["id"])
        video.status = "Completed";
        video.save()


class SendEmail(ListCreateAPIView):
    def post(self, request):
        #video = Video.objects.get(id=request.data["id"])
        #contest = video.contest
        send_mail('SmartTools - Video Cargado para conscurso',
                  'El video subido para el concurso '+ #+ contest.name +
                  ' ha sido cargado con exito. Puede ingresar a verlo en https://0.0.0.0:8080/',# + contest.name,
                  'c.cordobac@uniandes.edu.co',
                  ['cata.cordoba8@gmail.com'],
                  fail_silently=False)
