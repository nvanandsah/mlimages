import os
import shutil
from unittest import TestCase
from imageset.model import API
from imageset.imagenet import ImagenetAPI
import tests.env as env


class TestModel(TestCase):

    def test_label_dir(self):
        p = env.get_data_folder()
        api = ImagenetAPI(p, limit=3)
        api.gather("n01316949", include_subset=True)

        folder = "work_animal"
        path = api.file_api.to_abs(folder)
        api.label_dir(folder, 0, fname="test_label_fixed.txt")
        api.label_dir_auto(folder, fname="test_label_auto.txt")
        # todo have to do some check

        shutil.rmtree(path)

    def test_download(self):
        api = API(env.get_data_folder())
        f = "test.xml"
        api.download_dataset("http://www.image-net.org/api/xml/structure_released.xml", f)
        self.assertTrue(api.file_api.to_abs(f))
        os.remove(api.file_api.to_abs(f))
