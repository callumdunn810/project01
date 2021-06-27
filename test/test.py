from flask import url_for
from flask_testing import TestCase
from app import app, db, Stock




class TestBase(TestCase):
    def create_app(self):

    
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Grg170dx@34.105.139.189:3306/projectdb"
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()

        sample1 = Stock(manufacturer="Test Film")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('/home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Film', response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('/home'),
            data = dict(name="Test Film 1"),
            follow_redirects=True
        )
        self.assertIn(b'Test Film 1',response.data)