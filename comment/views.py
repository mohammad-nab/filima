from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from content.models import Content


class SendCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, content):
        serializer = CommentSerializer(data=request.data)
        content = Content.objects.get(slug=content)

        if serializer.is_valid():
            customer = request.user
            first_name = request.user.first_name
            last_name = request.user.last_name
            phone_number = request.user.phone_number
            serializer.save(customer=customer, first_name=first_name, last_name=last_name,
                            phone_number=phone_number, content=content)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
