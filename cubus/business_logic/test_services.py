import unittest

from .services import extract_packages, extract_docker_images, serialize_user, get_docker_images


class Test(unittest.TestCase):

    def test_extract_packages_1(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&install_docker=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'

        self.assertEqual(extract_packages(body_example), ['aide', 'checksecurity', 'stenographer', 'suricata'])

    def test_extract_packages_2(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&install_docker=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'
        self.assertEqual(extract_packages(body_example), [])

    def test_extract_docker_images_1(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&install_docker=on'

        self.assertEqual(extract_docker_images(body_example), [])

    def test_extract_docker_images_2(self):
        body_example = b'csrfmiddlewaretoken=QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII&' \
                       b'first_name=Mattia&last_name=Zanichelli&email=mattia.zanichelli%40student.supsi.ch&' \
                       b'os_type=1&aide=on&checksecurity=on&stenographer=on&suricata=on&install_docker=on&' \
                       b'dockerImage=alpine&dockerImage=busybox&dockerImage=mongo'
        self.assertEqual(extract_docker_images(body_example), ['alpine', 'busybox', 'mongo'])

    def test_serialize_user(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'install_docker': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        user = {
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'os_type': 'intrusion_detection',
            'install_docker': 'on',
        }
        self.assertEqual(serialize_user(post_example), user)

    def test_serialize_user_2(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'email': 'email@esempio.com',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'install_docker': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        user = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'email': ' ',
            'os_type': 'intrusion_detection',
            'install_docker': 'on',
        }
        self.assertNotEqual(serialize_user(post_example), user)

    def test_serialize_user_3(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'install_docker': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        user = {
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'os_type': '1',
            'install_docker': 'on',
        }
        self.assertNotEqual(serialize_user(post_example), user)

    def test_write_json(self):
        post_example = {
            'csrfmiddlewaretoken': ['QSgp8CaZXDNR9fNcfaxg4wMjCsh7N2r8Zk4FkjEieMwI6YfbP6nmWOlQI9y5KoII'],
            'first_name': 'Mattia',
            'last_name': 'Zanichelli',
            'email': 'mattia.zanichelli@student.supsi.ch',
            'os_type': '1',
            'aide': 'on',
            'checksecurity': 'on',
            'stenographer': 'on',
            'suricata': 'on',
            'install_docker': 'on',
            'dockerImage': ['alpine', 'busybox', 'mongo']
        }
        user = serialize_user(post_example)
        file_name = user['last_name'] + '-' + user['first_name'] + ".json"
        self.assertEqual('Zanichelli-Mattia.json', file_name)

    def test_get_docker_images(self):
        with open("../cubus/resources/docker_images", "r") as infile:
            content = infile.read()
        docker_images = content.split("\n")
        self.assertEqual(get_docker_images(), docker_images)
