import sys
sys.path.insert(1, '../src/')

import unittest

from test_tag.test_comparison import test_comparison
from test_tag.test_unary import test_unary


if __name__ == '__main__':
    unittest.main()
