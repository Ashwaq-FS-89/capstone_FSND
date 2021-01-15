import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor , Movies

ASS_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjNGY2NTAxYTc1NTAwMDc2MDRhZGMyIiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDc0MzgyMCwiZXhwIjoxNjEwODMwMjIwLCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.CGk-N3aLtvLvuHCYP-mdF_Pvsh7VBbPkln1y-LXulQAl1MetJxHOXCn2BFBWEr5T60OuKf6v9W5M4iJR4gL66H352Ndm-DEiylIJl6VcEQypOSbFJSTwSL_WE0skuoCvr7x1weIocLKz9WX2zOPFnm6XyHkwvwxnMmPFoC6ojaXoeqbM6jBFTJXHnA2HeetZI6O4Q5jPJFxqWyiOJyoMSo9RqEuZnA0PA4ZJunsDDdichdZP108oZZQOPtI7C71v8Ws3hYUg0wFHH76OUcfa4YMfjL5j7gt14FzpmCf0bKzLrb2jnSOC3EXn24PNpHHSmXRRVPRRmB6-t2rZIHGvKg'
DIR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiMmVmMTYzYzhmYTcwMDY4ZTY2YmU0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDc0Mzc3MywiZXhwIjoxNjEwODMwMTczLCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.hsw5vWp7moRjBPxj1KqcgzwGaerkbiGBroAIkLTUBkgHLE-exwaHjmgo9mT_Ue3huB3t52SJlRces3cJNECyqQnAsuMBzM235pjohJbHdfSaRhQX7xeA0bovaexmHvFJ9ML3kRYIEmSosKHhxzfOuHlJn-Szb-UpwBiKlrBEjZNcVm_wTDdRgmcAZ9zUR8e1VWUrwh-yiS5CppAwf0-8Sze5gsmD5hIvMXdZXdAjAuxp5JTXBBECMjDtVyVJ-wPl2Mx8DnJTIRl_eJi6R9-gStTi6xwDMD7aOQlSqqPS0l9Y3ZV3M-bweHRcMQ4QSBtQACGBVEmbYBn8cVbuCBC96'
EXE_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmZTgzNzFiZTIxMjQwMDcwYTI3NmY0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDc0MzUxOSwiZXhwIjoxNjEwODI5OTE5LCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicG9zdDptb3ZpZSJdfQ.x9xop37PaFo3_usJsXi4wb3YRuOJrE2dh8oaeIVcuKVhdwxMUreETi8naX6HHXMCrVmKk0wvbEjD4AzJtHUrvtg1dYRhRrYai_JC_aBRHL4Sy9nkW_uXwSakU4HYcgMxcDTA5NWS-qWR3hcurAYyBd79aRXY0DXac-6OgFjBRqjDyhDOD55dfAdGseCUZSnEjce5F4eubETEaOHmY7FrbIX_5gnr8ONMAnUO_Rp4eZOm404rzs0anMULtcvbOm86WJ4Kh4L2dVyoin9YS4Ah4EkQeTfUxX0zzs7nGeUf0_O0zjGIJcsgKzAu2cICLTA0LzYc-NdtLRrAwAWu7ybfWQ'

class capstonTestCase(unittest.TestCase):
   

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #  python test_app.py
    def test_get_Actor(self):
        actor = Actor(name='leen', age='12', gender='female')
        actor.insert()
        res = self.client().get('/actors',headers={'Authorization': 'Bearer ' + ASS_TOKEN})
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_fail_get_Actor(self):
        res = self.client().get('/actor',headers={'Authorization': 'Bearer ' + ASS_TOKEN})
        data = json.loads(res.data)
        actor = Actor(name='leen', age='12', gender='female')
        actor.insert()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Resource Not found')

    def test_get_movies(self):
        movie=Movies(title='the walking dead',release_date='23-01-22')
        movie.insert()
        res = self.client().get('/movies', headers={'Authorization': 'Bearer ' + ASS_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
       

    def test_fail_get_movies(self):
        res = self.client().get('/movie', headers={'Authorization': 'Bearer ' + ASS_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Resource Not found')


    def test_new_movie(self):
        new_movie = {
            'title':'whatever',
            'release_date': '28-1-21'
             }
        res = self.client().post('/movies', json=new_movie ,headers={'Authorization': 'Bearer ' + EXE_TOKEN})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_new_movie(self):
        new_movie = {
            'title':'whatever',
            'release_date': '22-3'
             }
        res = self.client().post('/movies/99', json=new_movie ,headers={'Authorization': 'Bearer ' + EXE_TOKEN})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_update_movie(self):
        movie=Movies(title='the walking dead',release_date='23-01-22')
        movie.insert()
        new_movie = {
            'title':'whatever0',
            'release_date': '28-1-21'
             }
        res = self.client().patch('/movies/2', json=new_movie ,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_update_movie(self):
        new_movie = {
            'title':'whatever0',
            'release_date': '28-1-21'
             }
        res = self.client().patch('/movies/999', json=new_movie ,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
       




    def test_new_actor(self):
        new_actor={'name':'raed','age':'34','gender':'male'}

        res=self.client().post('/actors',json=new_actor,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_fail_new_actor(self):
        new_actor = {
            'name':'nora',
            'age':'20',
            'gender':'female'
                }
        res = self.client().post('/actors/99', json=new_actor ,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_update_actor(self):
        actor = Actor(name='SALAF', age='12', gender='female')
        actor.insert()
        new_actor={'name':'raed','age':'35','gender':'male'}

        res=self.client().patch('/actors/2',json=new_actor,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_update_actor(self):
        new_actor={'name':'raed','age':'35','gender':'male'}

        res=self.client().patch('/actors/99',json=new_actor,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        actor = Actor(name='MANAL', age='33', gender='female')
        actor.insert()
      
        res = self.client().delete(f'/actors/{actor.id}' ,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_delete_actor(self):
      
        res = self.client().delete('/actors/99' ,headers={'Authorization': 'Bearer ' + DIR_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_delete_movie(self):
        movie=Movies(title='the walking dead S4',release_date='23-07-22')
        movie.insert()
        res = self.client().delete(f'/movies/{movie.id}' ,headers={'Authorization': 'Bearer ' + EXE_TOKEN})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_fail_delete_movies(self):
      
        res = self.client().delete('/movies/99' ,headers={'Authorization': 'Bearer ' + EXE_TOKEN})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    

        

if __name__ == "__main__":
    unittest.main()