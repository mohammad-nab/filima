from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, GetCommentSerializer, AdminCommentSerializer, AdminCommentApproveSerializer
from content.models import Content
from conf.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class AdminListCommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = AdminCommentSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['content']
    ordering_fields = ['-created_at']
    lookup_field = 'slug'


class AdminApproveCommentView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, comment_uuid):
        comment = get_object_or_404(Comment, comment_uuid=comment_uuid)
        serializer = AdminCommentApproveSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SendCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, content):
        content = get_object_or_404(Content, slug=content)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            customer = request.user
            first_name = request.user.first_name
            last_name = request.user.last_name
            phone_number = request.user.phone_number
            serializer.save(customer=customer, first_name=first_name, last_name=last_name,
                            phone_number=phone_number, content=content, status_type="INITIAL")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCommentView(APIView):

    def get(self, request, content):
        content = get_object_or_404(Content, slug=content)

        comments = Comment.objects.filter(content=content)

        serializer = GetCommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
