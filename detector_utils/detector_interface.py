import os

from PIL import Image

import detector_utils.base64_utils as base64_utils
import detector_utils.license_detector as license_detector


class Detector:
    detector = license_detector.license_detector()

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
        # Normalize the path to use the appropriate path separator for the current OS
        normalized_path = os.path.normpath(fs_location)

        # Split the path to get the filename
        filename = os.path.basename(normalized_path)

        detection["file_name"] = filename

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

    def extract_file_name(image_path):
        # Normalize the path to use the appropriate path separator for the current OS
        normalized_path = os.path.normpath(path_string)

        # Split the path to get the filename
        filename = os.path.basename(normalized_path)

        return filename
