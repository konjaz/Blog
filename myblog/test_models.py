from django.test import TestCase
from .models import Post


class TestModels(TestCase):
    test_post = Post()

    def test_postinstance(self):
        assert isinstance(self.test_post, Post) is True

    def test_verbose_name(self):
        self.test_post.title = "test"
        self.assertEqual(str(self.test_post), "test")