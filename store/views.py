from django.shortcuts import Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .hashing import AESCipher
import datetime as dt
from .serializers import *
from .filters import *    
from .models import *  

@api_view(['GET', 'POST'])
def sign_up(request):
    if request.method == 'GET':
        data = UserClient.objects.all()
        serializer = UserClientSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def log_in(request, user, password):
    try:
        client = UserClient.objects.get(phone_number=user)
        if client.password == password:
            if request.method == 'GET':
                data = Product.objects.filter(is_active=True, product_adder=client).order_by('-id')
                serializer = ProductSerializer(data,context={'request': request}, many=True)
                return Response(serializer.data)
            elif request.method == 'POST':
                serializer = ProductSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)
    except UserClient.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def is_login(request, user, password):
    try:
        client = UserClient.objects.get(phone_number=user)
        if AESCipher('encrypt').decrypt(client.password) == password:
            if request.method == 'GET':
                data = UserClient.objects.get(phone_number=user)
                data.password = AESCipher('encrypt').decrypt(data.password)
                serializer = UserClientSerializer(data)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)
    except UserClient.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def login_detail(request, user, password, nm):
    try:
        client = UserClient.objects.get(phone_number=user)
        if client.password == password:
            try:
                item = Product.objects.get(id=nm)
            except Product.DoesNotExist:
                raise Http404('Not Found')
            if request.method == 'GET':
                serializer = ProductSerializer(item)
                return JsonResponse(serializer.data)
            elif request.method == 'PUT':
                data = JSONParser().parse(request)
                serializer = ProductSerializer(item, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                item.delete()
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse(status=status.HTTP_417_EXPECTATION_FAILED)
    except UserClient.DoesNotExist:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def forgot_passwords(request):
    if request.method == 'GET':
        data = ForgotPassword.objects.all().order_by('-id')
        serializer = ForgotPasswordSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def turkmen_telekechi_main_api(request):
    if request.method == 'GET':
        data = TurkmenTelekechi.objects.all()
        serializer = TurkmenTelekechiSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        for is_twenty_days_ago in Product.objects.all():
            if (dt.date.today() - is_twenty_days_ago.joined_date).days > 20:
                is_twenty_days_ago.delete()
        for password in UserClient.objects.all():
            if password.password_encrypted:
                pass
            else:
                password.password=AESCipher('encrypt').encrypt(password.password)
                password.password_encrypted = True
                password.save()
        data = Category.objects.all()
        serializer = CategorySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
        
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        data = Product.objects.filter(is_active=True).order_by('-id')
        serializer = ProductSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def product_detail(request, nm):
    try:
        item = Product.objects.get(id=nm)
    except Product.DoesNotExist:
        raise Http404('Not Found')
    if request.method == 'GET':
        serializer = ProductSerializer(item)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def new_product_api(request):
    if request.method == 'GET':
        newProducts = []
        for is_new_product in Product.objects.filter(is_active=True):
            if (dt.date.today() - is_new_product.joined_date).days <= 3:
                newProducts.append(is_new_product)
        serializer = ProductSerializer(newProducts[::-1], context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def search_products(request):
    queryset = Product.objects.filter(is_active=True)
    filterset = ProductSearch(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_products(request):
    queryset = Product.objects.filter(is_active=True)
    filterset = ProductFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
