from rest_framework import serializers
from .models import Detection


class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = [
            "record_name",
            "time_stamp_creation",
            "pred_loc",
            "crop_loc",
            "processing_time_pred",
            "processing_time_ocr",
            "ocr_text_result",
            "pred_json_bin",
            "crop_json_bin",
        ]
