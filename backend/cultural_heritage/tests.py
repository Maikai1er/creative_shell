from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from .models import CulturalHeritage


class CulturalHeritageModelTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'name': 'Great Wall of China',
            'location': 'China',
            'year': '700 BC',
            'reason': 'Historical significance',
            'image_path': 'great_wall.jpg'
        }

    def test_heritage_creation(self):
        heritage = CulturalHeritage.objects.create(**self.valid_data)
        self.assertEqual(heritage.name, self.valid_data['name'])
        self.assertEqual(heritage.location, self.valid_data['location'])
        self.assertEqual(heritage.year, self.valid_data['year'])
        self.assertEqual(heritage.reason, self.valid_data['reason'])
        self.assertEqual(heritage.image_path, self.valid_data['image_path'])

    def test_missing_name(self):
        data = self.valid_data.copy()
        data.pop('name')
        with self.assertRaises(IntegrityError):
            CulturalHeritage.objects.create(**data)

    def test_missing_location(self):
        data = self.valid_data.copy()
        data.pop('location')
        with self.assertRaises(IntegrityError):
            CulturalHeritage.objects.create(**data)

    def test_name_max_length(self):
        data = self.valid_data.copy()
        data['name'] = 'A' * 256
        heritage = CulturalHeritage(**data)
        with self.assertRaises(ValidationError):
            heritage.full_clean()

    def test_location_max_length(self):
        data = self.valid_data.copy()
        data['location'] = 'A' * 256
        heritage = CulturalHeritage(**data)
        with self.assertRaises(ValidationError):
            heritage.full_clean()

    def test_invalid_year_type(self):
        data = self.valid_data.copy()
        data['year'] = 700
        heritage = CulturalHeritage(**data)
        with self.assertRaises(ValidationError):
            heritage.full_clean()

    def test_empty_optional_fields(self):
        data = self.valid_data.copy()
        data['reason'] = ''
        data['image_path'] = ''
        heritage = CulturalHeritage.objects.create(**data)
        self.assertEqual(heritage.reason, '')
        self.assertEqual(heritage.image_path, '')

    def test_null_optional_fields(self):
        data = self.valid_data.copy()
        data['reason'] = None
        data['image_path'] = None
        heritage = CulturalHeritage.objects.create(**data)
        self.assertIsNone(heritage.reason)
        self.assertIsNone(heritage.image_path)

    def test_default_values(self):
        heritage = CulturalHeritage.objects.create(
            name='Machu Picchu',
            location='Peru'
        )
        self.assertEqual(heritage.year, 'Default')
        self.assertIsNone(heritage.reason)
        self.assertIsNone(heritage.image_path)

    def test_duplicate_name(self):
        CulturalHeritage.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            duplicate_heritage = CulturalHeritage(**self.valid_data)
            duplicate_heritage.save()
