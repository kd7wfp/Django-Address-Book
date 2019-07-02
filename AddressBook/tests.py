from django.test import TestCase
from AddressBook.models import Contact

# Create your tests here.
class ModelTestCases(TestCase):
    def setUp(self):
        Contact.objects.create(email='lskywalker@tattooine.com', first_name='Luke', last_name='Skywalker', phone_number='15555555555', street_address='123 OutSkirts, Mos Eisley, Hutt Province, Tatooine, 84-52164')

    def test_contact_created(self):
        """Contact was succesfully created"""
        contact = Contact.objects.get(email="lskywalker@tattooine.com")
        self.assertEqual(contact.first_name, "Luke")
        self.assertEqual(contact.last_name, 'Skywalker')
        self.assertEqual(contact.phone_number, '15555555555')
        self.assertEqual(contact.street_address, '123 OutSkirts, Mos Eisley, Hutt Province, Tatooine, 84-52164')


    def test_contact_failed_creation(self):
        """Contact was not created"""
        try:
            contact = Contact.objects.create(first_name='Han', last_name='Solo', phone_number='16666666666', street_address='Cantina, Mos Eisley, Hutt Province, Tatooine, 84-52164')
            self.assertTrue(False)
        except:
            self.assertTrue(True)