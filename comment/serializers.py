from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']


class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'first_name', 'last_name', 'created_at']
        read_only_fields = ['created_at']


class AdminCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = "__all__"


class AdminCommentApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "status_type"

