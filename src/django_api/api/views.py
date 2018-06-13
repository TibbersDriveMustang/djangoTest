# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """
    Test API View.
    """
    def get(self, request, format=None):
        """
        Return a list of APIView features.
        """
        an_apiview = [
            'Use HTTP method as function (get, post, patch, put, delete)'
            'It is similiar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
