from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserImage
from .serializers import UserImageSerializer
from .utils import recognize_face
from django.core.files.base import ContentFile
import base64

@api_view(['POST'])
def upload_image(request):
    serializer = UserImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def face_recognition(request):
    if 'image' not in request.data:
        return Response({'error': 'Image not provided'}, status=status.HTTP_400_BAD_REQUEST)

    format, imgstr = request.data['image'].split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

    recognized_name = recognize_face(data)
    if recognized_name:
        return Response({'message': f'Face recognized as {recognized_name}'})
    else:
        return Response({'message': 'Face not recognized'}, status=status.HTTP_404_NOT_FOUND)

