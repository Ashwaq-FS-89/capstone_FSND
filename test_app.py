import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor , Movies

ASS_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjNGY2NTAxYTc1NTAwMDc2MDRhZGMyIiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDU5NDk3NywiZXhwIjoxNjEwNjAyMTc3LCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.eZ09HZMjF92tKgAiXQ_1aJZIEJpbut9QOwvOHeV-bSfAhppp6cXUExESFTmNikikxFI4y908BVBNHaRra3FeLKyYlvpbfGcFnxNtMB8pDwGFlufBzMTFWd134SjxBCQ6PoWJgD19czALFeHOG71Q0kmH-RUCSiIeoOcTq3_vykL1dSEASpJk27aF76QdKp9ZpTxHgAuQvtiesZcsBZVMUtcQvtFh2oDqlE3-0ID2KLg5fBSZxmInbKrzMIxEwX3yDDuF3ryPpGzchPQBke8pWfxlU75bzaW980PuFd2iaK2Wbl7EkJCKk6tG2KEE-84iuJ0wzMngqgv5edJzRMRUyA'
DIR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiMmVmMTYzYzhmYTcwMDY4ZTY2YmU0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDU5MzUzOCwiZXhwIjoxNjEwNjAwNzM4LCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.N0lJO6WwjnfzK5NGp-RSZ48aD7DSLMQrRwYEg4SwEroOQEV-ecJjzm8oFgURLMCynhqECuFOBO6woOXdwM-D_iV6lg9LtrTbCswZ8TiF6v4VQrFRFARLOjV5Id8YkrjWYegS8tTW-1YRZ4j0YPPpDTG4t8iOWNeqTaRvkaoOirdEXCflxOqfoZV-Y5_NvEbbZQ4MC7-AOmq2rZoUlXGNPMVCWsdN0IsI-1I1FS_0vsPBV1yJb2YIr7u-P1yPGEUGS3Gle2s0_gpH0Q0HGLHXEHWm3y1cPTB6tBy2g4Hji3FiNWd9yNgG3tCLZUq-BA1LuRcrLBrVgQO7-LZG02hrow'
EXE_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBXSG9ycjZ6Q3QxSXlVcDgwbjdsYiJ9.eyJpc3MiOiJodHRwczovL2Rldi1hZ2FjN2MyNC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmZTgzNzFiZTIxMjQwMDcwYTI3NmY0IiwiYXVkIjoiYWdlbmN5MSIsImlhdCI6MTYxMDU5Mzk3NiwiZXhwIjoxNjEwNjAxMTc2LCJhenAiOiIxZXNXWnhtbXNUQm5lUDIzUWEwbE5IejhDTkpwWk1zeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicG9zdDptb3ZpZSJdfQ.g8mdEr3Mit0UMeEjEST16KQ-v6r2t5bMbI4uzthzprK5GnmTLl6BcrP4wRyvtrOZQIw4MWSFAgQYxptrJ8hTin0CnULSms2Z4O4qX1R3PC_myZZ2ZkzoMv7IoS1nz8LM26aXkQ5lcyI2O0As0_GBvw6P9h8O1nL7QpncMxRzIMT_AYJaKqoTk2PDwdECNMo7e_DGpMZ1BeQXuKeRQCR0-9cuAeNdE0g6ZnVlYhlOkxEKe1Zn3Gc4ModK51C_BIkAN_QPXEidwG0-n7W7FgdAQp0UJ1vN4sN7wd-wi_dNG-GaPpliTtD2pc2fv_gWBD15CwnCIi68lAOHfn0dskReMw'

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
        # self.assertTrue(data['movies'])
        # self.assertTrue(len(data['movies']))

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