#from project import app, db
from project import create_app,db
app = create_app()
from flask_testing import TestCase



class BaseTestCase(TestCase):
    def create_app(self):
        #print("!!!!!testing base case")
        app.config.from_object('project.config.TestingConfig')
        return app
    
    def setUp(self):
        #print("!!!!!testing setup")
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        #print("!!!!!testing tear down")
        db.session.remove()
        db.drop_all()
    