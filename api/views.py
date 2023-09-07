from django.http import JsonResponse
from .models import Detection
from .serializers import DetectionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(http_method_names=["GET"])
def detection_list(request, format=None):
    if request.method == "GET":
        detections = Detection.objects.all()
        serializer = DetectionSerializer(detections, many=True)
        return Response({"detections": serializer.data})


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def detection_detail(request, id, format=None):
    pass
