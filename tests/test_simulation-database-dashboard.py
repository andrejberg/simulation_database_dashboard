import unittest

import simulation-database-dashboard


class Simulation-database-dashboardTestCase(unittest.TestCase):

    def setUp(self):
        self.app = simulation-database-dashboard.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to simulation-database-dashboard', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
