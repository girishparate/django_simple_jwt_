from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hey there!'}
        return Response(content)


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hello.html'

    def get(self, request):
        return Response(data={})