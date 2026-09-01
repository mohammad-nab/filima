from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, views
from .models import Content, LikeDislike
from .serializers import ContentSerializer, LikeDiskSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from conf.pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status_type']
    search_fields = ['english_name', 'persian_name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save(update_fields=["is_deleted"])


class LikeDislikeView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeDiskSerializer

    def post(self, request, content):
        srz_data = LikeDiskSerializer(data=request.data)
        srz_data.is_valid(raise_exception=True)
        content_obj = get_object_or_404(Content, slug=content)

        reaction = srz_data.validated_data['reaction']
        like_dislike, created = LikeDislike.objects.update_or_create(content=content_obj,
                                                                     customer=request.user,
                                                                     defaults={
                                                                         'reaction': reaction,
                                                                     })
        response_serializer = LikeDiskSerializer(like_dislike)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)



