from django.http import JsonResponse
from .models import Detection
from .serializers import DetectionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from detector_utils import detector_interface


@api_view(http_method_names=["GET", "POST"])
def detection_endpoints(request, format=None):
    if request.method == "GET":
        return detection_list(request, format)

    if request.method == "POST":
        return detection_detect(request, format)


def detection_list(request, format=None):
    detections = Detection.objects.all()
    serializer = DetectionSerializer(detections, many=True)
    return Response({"detections": serializer.data})


def detection_detect(request, format=None):
    data = request.data

    detector_ins = detector_interface.Detector()
    payload = detector_ins.detect_license_from_fs_location(
        fs_location=data["data"]["src_file"]
    )      
    #print(f'payload: {payload}')
    serializer = DetectionSerializer(data=payload.get("detection"))
    print(f'serializer: valid? {serializer.is_valid()}')
    print(serializer.errors)
    print(serializer.validated_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "error"}, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def detection_detail(request, id, format=None):
    pass
