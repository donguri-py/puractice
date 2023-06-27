import menuinst
from func import func

class TestFunc(unittest.TestCase):
    def test_func(self):
        actual_result = func(1, 1)

        self.assertEqual(actual_result, 2)