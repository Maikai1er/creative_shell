from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from parser.models import ParsedData


class ParsedDataModelTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'name': 'Great Wall of China',
            'location': 'China',
            'year': '700 BC',
            'reason': 'Historical significance',
            'image_path': 'great_wall.jpg'
        }

    def test_parsed_data_creation(self):
        parsed_data = ParsedData.objects.create(**self.valid_data)
        self.assertEqual(parsed_data.name, self.valid_data['name'])
        self.assertEqual(parsed_data.location, self.valid_data['location'])
        self.assertEqual(parsed_data.year, self.valid_data['year'])
        self.assertEqual(parsed_data.reason, self.valid_data['reason'])
        self.assertEqual(parsed_data.image_path, self.valid_data['image_path'])

    def test_missing_name(self):
        data = self.valid_data.copy()
        data.pop('name')
        with self.assertRaises(ValidationError):
            heritage = ParsedData(**data)
            heritage.full_clean()

    def test_missing_location(self):
        data = self.valid_data.copy()
        data.pop('location')
        with self.assertRaises(ValidationError):
            heritage = ParsedData(**data)
            heritage.full_clean()

    def test_name_max_length(self):
        data = self.valid_data.copy()
        data['name'] = 'A' * 256
        parsed_data = ParsedData(**data)
        with self.assertRaises(ValidationError):
            parsed_data.full_clean()

    def test_location_max_length(self):
        data = self.valid_data.copy()
        data['location'] = 'A' * 256
        parsed_data = ParsedData(**data)
        with self.assertRaises(ValidationError):
            parsed_data.full_clean()

    def test_invalid_year_type(self):
        data = self.valid_data.copy()
        data['year'] = 700
        parsed_data = ParsedData(**data)
        with self.assertRaises(ValidationError):
            parsed_data.clean()

    def test_empty_optional_fields(self):
        data = self.valid_data.copy()
        data['reason'] = ''
        data['image_path'] = ''
        parsed_data = ParsedData.objects.create(**data)
        self.assertEqual(parsed_data.reason, '')
        self.assertEqual(parsed_data.image_path, '')

    def test_null_optional_fields(self):
        data = self.valid_data.copy()
        data['reason'] = None
        data['image_path'] = None
        parsed_data = ParsedData.objects.create(**data)
        self.assertIsNone(parsed_data.reason)
        self.assertIsNone(parsed_data.image_path)

    def test_default_values(self):
        parsed_data = ParsedData.objects.create(
            name='Machu Picchu',
            location='Peru'
        )
        self.assertEqual(parsed_data.year, '')
        self.assertIsNone(parsed_data.reason)
        self.assertIsNone(parsed_data.image_path)

    def test_duplicate_name(self):
        ParsedData.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            duplicate_parsed_data = ParsedData(**self.valid_data)
            duplicate_parsed_data.save()
