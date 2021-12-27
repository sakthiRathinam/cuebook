from django.shortcuts import render
from django.db.models import F ,Value,CharField,Q
from django.contrib.auth.models import User , Group
from django.http import JsonResponse
from math import radians, cos, sin, asin, sqrt, atan2
from rest_framework import viewsets , permissions , serializers
from rest_framework.pagination import LimitOffsetPagination
from .models import *
from rest_framework import parsers
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import *
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files import File as DjangoFile
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser

# Create your views here.
