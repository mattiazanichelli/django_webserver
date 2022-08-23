import crypt
import unittest

from cubus.business_logic.services import extract_packages, extract_docker_images, serialize_iso, get_docker_images, \
    serialize_user
from webserver.settings import PASSWDSALT


class Test(unittest.TestCase):

    def test_extract_packages_1(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&include_docker_images=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'

        self.assertEqual(extract_packages(body_example), ['aide', 'checksecurity', 'stenographer', 'suricata'])

    def test_extract_packages_2(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&include_docker_images=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'
        self.assertEqual(extract_packages(body_example), [])

    def test_extract_packages_3(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&iwatch=on&packit=on&snort=on&' \
                       b'stenographer=on&suricata=on&tiger=on&tripwire=on&include_docker_images=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'
        self.assertEqual(extract_packages(body_example),
                         ['aide', 'checksecurity', 'iwatch', 'packit', 'snort', 'stenographer', 'suricata',
                          'tiger', 'tripwire'])

    def test_extract_docker_images_1(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&include_docker_images=on'

        self.assertEqual(extract_docker_images(body_example), [])

    def test_extract_docker_images_2(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&include_docker_images=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'
        self.assertEqual(extract_docker_images(body_example), ['alpine', 'busybox', 'mongo'])

    def test_extract_docker_images_3(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&iwatch=on&packit=on&snort=on&' \
                       b'stenographer=on&suricata=on&tiget=on&tripwire=on&include_docker_images=on&' \
                       b'dockerImage=alpine&dockerImage=busbox&dockerImage=mongoDB'
        self.assertNotEqual(extract_docker_images(body_example),
                            ['alpine', 'busybox', 'mongo'])

    def test_serialize_user(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': "pass",
            'creations': []
        }
        user = {
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': crypt.crypt("pass", PASSWDSALT),
            'creations': []
        }
        self.assertEqual(serialize_user(post_example), user)

    def test_serialize_user_2(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'email': 'email@esempio.com',
            'password': "pass",
            'creations': []
        }
        user = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'email': ' ',
            'password': crypt.crypt("pass", PASSWDSALT),
            'creations': []
        }
        self.assertNotEqual(serialize_user(post_example), user)

    def test_serialize_user_3(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': "different_pass",
            'creations': []
        }
        user = {
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'password': crypt.crypt("pass", PASSWDSALT),
            'creations': []
        }
        self.assertNotEqual(serialize_user(post_example), user)

    def test_serialize_iso_1(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'isoName': 'Prova',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'include_docker_images': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        iso = {
            'name': 'Prova',
            'os_type': "intrusion_detection",
            'include_docker_images': 'on',
        }
        self.assertEqual(serialize_iso(post_example), iso)

    def test_serialize_iso_2(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'isoName': 'Prova',
            'os_type': '1',
            'suricata': 'on',
            'include_docker_images': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        iso = {
            'name': 'Prova',
            'os_type': "2",
            'include_docker_images': 'on',
        }
        self.assertNotEqual(serialize_iso(post_example), iso)

    def test_serialize_iso_3(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'isoName': 'Prova',
            'os_type': '2',
            'suricata': 'on',
            'include_docker_images': 'on',
            'dockerImage': []
        }
        iso = {
            'name': 'Prova',
            'os_type': "network_monitoring",
            'include_docker_images': 'off',
        }
        self.assertNotEqual(serialize_iso(post_example), iso)

    def test_json_file_name(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'isoName': 'Prova',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'include_docker_images': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        iso = serialize_iso(post_example)
        file_name = iso['name'] + ".json"
        self.assertEqual('Prova.json', file_name)

    def test_get_docker_images(self):
        with open("./cubus/resources/docker_images", "r") as infile:
            content = infile.read()
        docker_images = content.split("\n")
        self.assertEqual(get_docker_images(), docker_images)
