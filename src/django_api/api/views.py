# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):
    """
    Test API View.
    """
    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """
        Create a hello message with our name
        :param request:
        :return:
        """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """
            Handles updating an object
        :param request:
        :param pk:
        :return:
        """

        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """
            Patch request, only updates fields provided in the request
        :param request:
        :param pk:
        :return:
        """

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """
        Delete an object
        :param request:
        :param pk:
        :return:
        """

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """
        Test API ViewSet
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
            Return a hello message
        :param request:
        :return:
        """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """

        :param request:
        :return:
        """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        Handles getting an object by its ID
        :param request:
        :param pk:
        :return:
        """

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """
        Handles updating an object
        :param request:
        :param pk:
        :return:
        """

        return Response({'http_method': 'PUT'})

    def partical_update(self, request, pk=None):
        """
        Handles updating part of an object.
        :param request:
        :param pk:
        :return:
        """

        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """
        Handles removing an object
        :param request:
        :param pk:
        :return:
        """

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating, creating and updating profiles.
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )    ## Could assign multiple authentications
    permission_classes = (permissions.UpdateOwnProfile, )   ## Could assign multiple permissions
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """
    Checks email and password and return an auth token
    """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """
        Use the ObtainAuthToken APIView to validate and create a token
        :param request:
        :return:
        """
        return ObtainAuthToken().post(request)