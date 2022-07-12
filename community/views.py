from django.shortcuts import render
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from community.serializers import ArticleSerializer

from community.models import Article as ArticleModel


class CommunityView(APIView):
    def get(self, request):
        article = ArticleModel.objects.all().order_by('-created_at')
        serialized_data = ArticleSerializer(article, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["user"] = request.user.id
        article_serializer = ArticleSerializer(data=request.data)
        
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer, status=status.HTTP_200_OK)
        return Response(article_serializer, status=status.HTTP_400_BAD_REQUEST)