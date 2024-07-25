# import json
# import unittest
#
# from django.test import TestCase, Client
# from django.urls import reverse
# from unittest.mock import patch
# from cultural_heritage.models import CulturalHeritage
# from parser.models import ParsedData
#
#
# class ViewTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.create_sample_heritage()
#
#     def create_sample_heritage(self):
#         CulturalHeritage.objects.create(
#             name='Great Wall of China',
#             location='c',
#             year='700 BC',
#             reason='Historical significance',
#             image_path='great_wall.jpg'
#         )
#         ParsedData.objects.create(
#             name='Great Wall of China',
#             location='China',
#             year='700 BC',
#             reason='Historical significance',
#             image_path='great_wall.jpg'
#         )
#
#     @patch('creative_shell.views.parse_and_save_to_temp_table')
#     def test_update_data_success(self, mock_parse_and_save):
#         mock_parse_and_save.return_value = None
#         response = self.client.get(reverse('update_data'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Parsing completed successfully')
#
#     @patch('creative_shell.views.get_next_heritage')
#     def test_get_next_heritage_success(self, mock_get_next_heritage):
#         mock_get_next_heritage.return_value = {
#             'name': 'Parsed Heritage',
#             'location': 'Parsed Location',
#             'year': '2024',
#             'reason': 'Parsed Reason',
#             'image_path': '/path/to/image.jpg'
#         }
#         response = self.client.get(reverse('get_next_heritage'))
#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(
#             response.content,
#             {
#                 'name': 'Parsed Heritage',
#                 'location': 'Parsed Location',
#                 'year': '2024',
#                 'reason': 'Parsed Reason',
#                 'image_path': '/path/to/image.jpg'
#             }
#         )
#
#     @patch('creative_shell.views.get_next_heritage')
#     @patch('creative_shell.views.save_heritage')
#     def test_save_heritage_success(self, mock_save_heritage, mock_get_next_heritage):
#         mock_get_next_heritage.return_value = {
#             'name': 'Parsed Heritage',
#             'location': 'Parsed Location',
#             'year': '2024',
#             'reason': 'Parsed Reason',
#             'image_path': '/path/to/image.jpg'
#         }
#         mock_save_heritage.return_value = None
#         post_data = {
#             'data': {
#                 'name': 'Parsed Heritage',
#                 'location': 'Parsed Location',
#                 'year': '2024',
#                 'reason': 'Parsed Reason',
#                 'image_path': '/path/to/image.jpg'
#             },
#             'decision': 'approve'
#         }
#         response = self.client.post(reverse('save_heritage'), json.dumps(post_data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(response.content, {'message': 'Heritage saved successfully'})
#
#     def test_load_more_heritages(self):
#         response = self.client.get(reverse('load_more_heritages'))
#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(response.content, [
#             {
#                 'name': 'Sample Heritage',
#                 'location': 'Sample Location',
#                 'year': '2024',
#                 'reason': 'Sample Reason',
#                 'image_path': '/path/to/image.jpg'
#             }
#         ])
#
#     @patch('creative_shell.views.get_next_heritage')
#     def test_get_next_heritage_no_pending(self, mock_get_next_heritage):
#         mock_get_next_heritage.return_value = None
#         response = self.client.get(reverse('get_next_heritage'))
#         self.assertEqual(response.status_code, 404)
#         self.assertJSONEqual(response.content, {'message': 'No pending objects'})
#
#     @patch('creative_shell.views.get_next_heritage')
#     def test_get_next_heritage_invalid_method(self, mock_get_next_heritage):
#         response = self.client.post(reverse('get_next_heritage'))
#         self.assertEqual(response.status_code, 405)
#         self.assertJSONEqual(response.content, {'message': 'Method not allowed'})
#
#     @patch('creative_shell.views.data_management.save_to_contact_data_table')
#     def test_receive_contact_data_success(self, mock_save_contact_data):
#         mock_save_contact_data.return_value = None
#         post_data = {
#             'name': 'John Doe',
#             'contact': '1234567890',
#             'about': 'About John Doe'
#         }
#         response = self.client.post(reverse('receive_contact_data'), json.dumps(post_data),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(response.content, {'message': 'Contact data saved successfully'})
#
#     def test_receive_contact_data_invalid_method(self):
#         response = self.client.get(reverse('receive_contact_data'))
#         self.assertEqual(response.status_code, 405)
#         self.assertJSONEqual(response.content, {'message': 'Method not allowed'})
#
#     @patch('creative_shell.views.data_management.save_to_contact_data_table')
#     def test_receive_contact_data_missing_data(self, mock_save_contact_data):
#         post_data = {
#             'name': 'John Doe',
#             'contact': '1234567890'
#         }
#         response = self.client.post(reverse('receive_contact_data'), json.dumps(post_data),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         self.assertJSONEqual(response.content, {'message': 'Missing required data'})
#
#     @patch('creative_shell.views.parse_and_save_to_temp_table')
#     def test_update_data_exception(self, mock_parse_and_save):
#         mock_parse_and_save.side_effect = Exception("Test exception")
#         response = self.client.get(reverse('update_data'))
#         self.assertEqual(response.status_code, 500)
#         self.assertJSONEqual(response.content, {'error': 'Test exception'})
#
#
# if __name__ == '__main__':
#     unittest.main()
