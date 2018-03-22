from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import JsonResponse
from django.utils import timezone
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list_api(request, *args, **kwargs):
    data = {
        "posts": Post.objects.count()
    }
    return JsonResponse(data)


class PostList(View):
    def get(self, request, *args, **kwargs):
        return render(request, '../templates/post_list.html')


class PostData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

        data = {
            "posts": [{"title": post.title,
                       "body": post.text,
                       "published_date": post.published_date} for i, post in enumerate(posts)]
        }
        return Response(data)
