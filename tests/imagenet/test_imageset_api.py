import os
import shutil
from unittest import TestCase
from imageset.imagenet import ImagenetAPI
import tests.env as env


class TestImagenetAPI(TestCase):

    def test_gather_wnid(self):
        p = env.get_data_folder()
        api = ImagenetAPI(p)
        api.gather("n11531193")

        path = env.get_path("wilding")
        self.assertTrue(os.path.isdir(path))
        shutil.rmtree(path)

    def test_gather_wnids(self):
        p = env.get_data_folder()
        api = ImagenetAPI(p, limit=3)
        api.gather("n09289331", include_subset=True)

        path = env.get_path("glacier")
        self.assertTrue(os.path.isdir(path))

        for f in ["alpine_glacier", "continental_glacier", "piedmont_glacier"]:
            path = env.get_path("glacier/" + f)
            self.assertTrue(os.path.isdir(path))

        shutil.rmtree(path)
