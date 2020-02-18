import jwt
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView

from .models import Contest, Video
from .serializers import ContestSerializer, VideoSerializer
from django.core.mail import send_mail
from customer.models import User
from datetime import datetime

# Create your views here.

# Contest
class ContestListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token_decoded = jwt.decode(token, None, None)
        contest = Contest.objects.filter(user__id=token_decoded["user_id"])
        serializer = ContestSerializer(contest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        token_decoded = jwt.decode(token, None, None)
        data = request.data.dict()
        usr = User.objects.get(id=token_decoded["user_id"])
        data['user'] = usr
        data['begin_at'] = datetime.strptime(data['begin_at'], '%Y-%m-%d %H:%M:%S')
        data['end_at'] = datetime.strptime(data['end_at'], '%Y-%m-%d %H:%M:%S')
        new_content = Contest.objects.create(**data)
        return Response(ContestSerializer(new_content).data, status=status.HTTP_201_CREATED)


class ContestDetailByURLView(APIView):
    def get(self, request, url, format=None):
        url = request.build_absolute_uri()
        contest = Contest.objects.get(url=url)
        return Response(ContestSerializer(contest).data, status=status.HTTP_200_OK)


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
        data = request.data.dict()
        data['begin_at'] = datetime.strptime(data['begin_at'], '%Y-%m-%d %H:%M:%S')
        data['end_at'] = datetime.strptime(data['end_at'], '%Y-%m-%d %H:%M:%S')
        serializer = ContestSerializer(contest, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contest = self.get_object(pk)
        contest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Video
class VideoListCreateView(APIView):

    def get(self, request, pk, format=None):
        videos = Video.objects.filter(contest__id=pk)
        if request.user.is_anonymous:
            videos = videos.filter(status="Convertido")
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        data = request.data.dict()
        contest = Contest.objects.get(id=data['contest'])
        data['contest'] = contest
        video = Video.objects.create(**data)
        return Response(VideoSerializer(video).data, status=status.HTTP_201_CREATED)


class VideoDetailView(RetrieveUpdateDestroyAPIView):

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





