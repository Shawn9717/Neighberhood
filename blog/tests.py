from django.test import TestCase
from .models import BlogPost,Comment
# Create your tests here.
import unittest

class BlogTest(unittest.TestCase):
    
    def setUp(self):
        self.new_category=Blog(blog = 'science')
        
    def test_cat(self):
        self.assertTrue(self.new_blog is not None) 