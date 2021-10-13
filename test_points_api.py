#test
import unittest
import points_api
import xmlrunner
import os
import inspect
from point_manager import PointManager
from sqlalchemy import create_engine
from base import Base

class TestPointApi(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///test_points.sqlite')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        points_api.point_mgr = PointManager('test_points.sqlite')
        
        points_api.app.testing = True
        self.app = points_api.app.test_client()

        self.logPoint()
    
    def tearDown(self):
        os.remove('test_points.sqlite')
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))
    
    def test_points_all(self):
        rv = self.app.get('/points/all')
        self.assertEqual(rv.status, '200 OK')

if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='api-test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
