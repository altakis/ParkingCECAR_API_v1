from .license_detector import license_detector
from PIL import Image
from . import base64_utils


class Detector:
    detector = license_detector()

    def detect_license_from_fs_location(self, fs_location, options=None):
        # load data
        model_name = ""
        url_input = None
        image_input = None
        webcam_input = Image.open(fs_location)
        threshold = 0.5

        detection = self.detector.detect_objects(
            model_name, url_input, image_input, webcam_input, threshold
        )

        # save original file name
        detection["file_name"] = fs_location

        # Create base64 strings from detection
        pred_json_base64 = None
        crop_json_base64 = None
        if options:
            if options.get("pred_json_base64") == True:
                pred_json_base64 = base64_utils.encode(payload.get("pred_loc"))
            if options.get("crop_json_base64") == True:
                crop_json_base64 = base64_utils.encode(payload.get("crop_loc"))

        payload = {
            "detection": detection,
            "pred_json_base64": pred_json_base64,
            "crop_json_base64": crop_json_base64,
        }
        return payload
