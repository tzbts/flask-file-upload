from flask_file_upload._model_utils import _ModelUtils
from flask_file_upload.file_upload import FileUpload


class Test_FileUtils:

    def test_create_keys(self):
        result = {
            "my_video__file_name": None,
            "my_video__mime_type": None,
            "my_video__file_type": None,
        }

        file_upload = FileUpload()
        assert result == _ModelUtils.create_keys(file_upload.Model.keys, "my_video")
