from django.core.exceptions import ValidationError
from django.test import TestCase
from cultural_heritage.models import CulturalHeritage, ContactData
from parser.models import ParsedData
from creative_shell.data_management import save_to_heritage_table, save_to_parsed_table, save_to_contact_data_table


class DataManagementTests(TestCase):

    def test_save_to_heritage_table(self):
        heritage_data = {
            'name': 'Great Wall of China',
            'location': 'China',
            'year': '700 BC',
            'reason': 'Historical significance',
            'image_path': 'great_wall.jpg'
        }
        save_to_heritage_table(heritage_data)

        heritage = CulturalHeritage.objects.get(name='Great Wall of China')
        self.assertEqual(heritage.location, 'China')
        self.assertEqual(heritage.year, '700 BC')
        self.assertEqual(heritage.reason, 'Historical significance')
        self.assertEqual(heritage.image_path, 'great_wall.jpg')

    def test_save_to_parsed_table(self):
        parsed_data = {
            'name': 'Great Wall of China',
            'location': 'China',
            'year': '700 BC',
            'reason': 'Historical significance',
            'image_path': 'great_wall.jpg'
        }
        save_to_parsed_table(parsed_data)

        parsed = ParsedData.objects.get(name='Great Wall of China')
        self.assertEqual(parsed.location, 'China')
        self.assertEqual(parsed.year, '700 BC')
        self.assertEqual(parsed.reason, 'Historical significance')
        self.assertEqual(parsed.image_path, 'great_wall.jpg')

    def test_save_to_contact_data_table(self):
        contact_data = {
            'name': 'Test Contact',
            'contact': '123-456-7890',
            'about': 'Test About'
        }
        save_to_contact_data_table(contact_data)

        contact = ContactData.objects.get(name='Test Contact')
        self.assertEqual(contact.contacts, '123-456-7890')
        self.assertEqual(contact.about, 'Test About')

    def test_save_to_heritage_table_defaults(self):
        heritage_data = {
            'name': 'Great Wall of China',
            'location': 'China'
        }
        save_to_heritage_table(heritage_data)

        heritage = CulturalHeritage.objects.get(name='Great Wall of China')
        self.assertEqual(heritage.location, 'China')
        self.assertEqual(heritage.year, '')
        self.assertEqual(heritage.reason, '')
        self.assertEqual(heritage.image_path, '')

    def test_save_to_parsed_table_defaults(self):
        parsed_data = {
            'name': 'Great Wall of China',
            'location': 'China'
        }
        save_to_parsed_table(parsed_data)

        parsed = ParsedData.objects.get(name='Great Wall of China')
        self.assertEqual(parsed.location, 'China')
        self.assertEqual(parsed.year, '')
        self.assertEqual(parsed.reason, '')
        self.assertEqual(parsed.image_path, '')

    def test_save_to_contact_data_table_defaults(self):
        contact_data = {}
        save_to_contact_data_table(contact_data)

        contact = ContactData.objects.get(name='default name')
        self.assertEqual(contact.contacts, 'Contact Not Found')
        self.assertEqual(contact.about, 'About Field is Empty')

    def test_save_to_heritage_table_missing_required_fields(self):
        heritage_data = {}
        with self.assertRaises(ValidationError):
            save_to_heritage_table(heritage_data)

    def test_save_to_parsed_table_missing_required_fields(self):
        parsed_data = {}
        with self.assertRaises(ValidationError):
            save_to_parsed_table(parsed_data)

    def test_save_to_contact_data_table_missing_required_fields(self):
        contact_data = {}
        with self.assertRaises(ValidationError):
            save_to_contact_data_table(contact_data)
