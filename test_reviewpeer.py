# test_reviewpeer.py
"""
Tests for ReviewPeer module.
"""

import unittest
from reviewpeer import ReviewPeer

class TestReviewPeer(unittest.TestCase):
    """Test cases for ReviewPeer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReviewPeer()
        self.assertIsInstance(instance, ReviewPeer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReviewPeer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
