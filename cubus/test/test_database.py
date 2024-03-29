import unittest

from pymongo import MongoClient

from webserver.settings import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASS

client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT), username=MONGO_USERNAME, password=MONGO_PASS)
cubus = client['cubus']
users = cubus['users']

'''
#######################################
REMEMBER TO START DOCKER-COMPOSE FIRST!
#######################################
'''


class Test(unittest.TestCase):

    def test_db_name(self):
        db_name = users.name
        self.assertEqual(db_name, 'users')

    def test_insert_one(self):
        user = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'email': 'email@example.com',
            'os_type': 'intrusion_detection',
            'install_docker': 'on',
        }
        self.assertTrue(users.insert_one(user))

    def test_find_one(self):
        users.insert_one({
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': 'mypass'
        })
        user_id = users.find_one({'email': 'mattia.zanichelli@student.supsi.ch'})['_id']
        self.assertEqual(users.find_one({'email': 'mattia.zanichelli@student.supsi.ch'}), {
            '_id': user_id,
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': 'mypass'
        })
        user = users.find_one({'email': 'mattia.zanichelli@student.supsi.ch'})
        users.delete_one(user)

    def test_remove_one(self):
        user = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'email': 'email@example.com',
            'os_type': 'intrusion_detection',
            'install_docker': 'on',
        }
        self.assertTrue(users.delete_one(user))

    def test_db_size(self):
        users.drop()
        self.assertEqual(users.estimated_document_count(), 0)

        user = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'email': 'email@example.com',
            'os_type': 'intrusion_detection',
            'install_docker': 'on',
        }
        users.insert_one(user)
        self.assertNotEqual(users.estimated_document_count(), 0)

    def test_update_one(self):
        my_filter = {'first_name': 'Name'}
        new_value = {"$set": {'first_name': 'NewName'}}
        users.update_one(my_filter, new_value)
        user = users.find_one()
        self.assertEqual(user['first_name'], 'NewName')
        users.delete_one(user)

