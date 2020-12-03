from django.db.models.aggregates import Count
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from rest_framework import status, permissions
from rest_framework.decorators import api_view, renderer_classes, \
    permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def index(request):
    data = {'test' : 123}
    if request.accepted_renderer.format == 'html':
        return Response(data, template_name='app/intro.html')
    return Response(data)

