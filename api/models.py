from django.db import models


class Detection(models.Model):
    # Reference value corresponding at the moment in which the system started the process
    record_name = models.CharField(max_length=200)
    # Date in which this record in particular was created
    time_stamp_creation = models.DateField(auto_created=True)
    # File system location of the license plate prediction
    pred_loc = models.CharField(max_length=500, null=True, blank=True)
    # File system location of the license plate prediction crop
    crop_loc = models.CharField(max_length=500, null=True, blank=True)
    # Time elapsed in the license plate prediction
    processing_time_pred = models.DecimalField(decimal_places=4, max_digits=5, null=True, blank=True)
    # Time elapsed in the license plate ocr process
    processing_time_ocr = models.DecimalField(decimal_places=4, max_digits=5,null=True, blank=True)
    # ocr result
    ocr_text_result = models.CharField(max_length=500, null=True, blank=True)
    # binary encode64 of the license plate prediction
    pred_json_bin = models.CharField(max_length=500, null=True, blank=True)
    # binary encode64 of the license plate prediction crop
    crop_json_bin = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return (
            f"{self.record_name} {self.time_stamp_creation} ocr:{self.ocr_text_result}"
        )
