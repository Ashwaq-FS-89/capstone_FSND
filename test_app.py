import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor , Movies

ASS_TOKEN= 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjNGY2NTAxYTc1NTAwMDc2MDRhZGMyIiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDczMzEzMywiZXhwIjoxNjEwNzQwMzMzLCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.DcbZTywWnasjzYzKXr0TDdPVGV4JVRgDrQiosmmwx82YfU_Ix5DpOCf0NoBIk1tnK6ExTQ9cVNFDVdLrPLYJClGCuIE47wQcbe5N2x_9A6PejRGitTVnfewH2AzOW3PCl-qHxckIACGAv76i4OTIzS_fO-fKLARujsR3oUrXgQTbwUzZtX9ZoG9htnqNnQQYrTLVnMuik8Mpkp-WoKMT10fue4vWpkCMRY1b1UjfeqgWrKoNQE-Mq4FppWNr62OIXBrFgUJGVFar0_cJos0MjFA_4UDI3Z3vSF9QE8aEObOlMCmSf06QaNnddQun5a9bUlcU1L8ZkRLnOXxDLcriug'
DIR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiMmVmMTYzYzhmYTcwMDY4ZTY2YmU0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDczMzE4MywiZXhwIjoxNjEwNzQwMzgzLCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.dStWenwTpJ21h9uQVsnhnvd5rpVKM9RcY2Bj8iegKIBTbjddGYuJt3xKFNxtXhTyd-oaYRmO6iY9NNCBW8i4u3AHBKIFmlt5ifj9aZPMa6goaAUUY2fCuOXtjde3OXC5ihS0ZqvQKmMn2wdlEBorTt58BScvLakbQiqWEHBlZBivaBVxa9XJVEWqFuKtkMqtup4iCckGUbvlK2VTr6BXz9X-CPsTHvlGKx8C9wVzySp4BxwgwSFVlN5YSgE9RA-5h45pXTZcD6TYSaCgRh1k9vni4JL1E8by2-mvxndC231N_Tc3CdMj8DRsmF10rmQ8G2MVWtkhl2FWVbv5dFUd_g'
EXE_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmZTgzNzFiZTIxMjQwMDcwYTI3NmY0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDczMzA3OCwiZXhwIjoxNjEwNzQwMjc4LCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicG9zdDptb3ZpZSJdfQ.RTJLHfMGJq_HJeGr0FyIDP_q4535Jzmd4JDNAMycfK2fOq4broej6kIJ2s5ydukWCx5N2ty_zTAEcvfB5qWipFgNs13zUcvaK8oTJhrptExBT_i3WcEFUn5tT5LpQ0R7ITdchntZVTvUQf2ZuLJnJaTsSHuRGqgmxEEFwLDV6V6Ue-otPgv97RZC7Z1GNYwhd9RUzs1YfHOE8Q3jYju_zJkxiD930qgEl-m_I5rioWz1Fwkd22n3g0GQWjnj8hsywc1S8DHUHuyppbxrK1Pr-OAQcsT_7StHkmNqkf6xHxWu6Za_5EbEcMz729JlObVl0HtCkO3eRE8-4huc8wf1TQ'

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