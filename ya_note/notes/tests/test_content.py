from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

<<<<<<< HEAD
from notes.forms import NoteForm
=======
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
from notes.models import Note

User = get_user_model()


class TestContent(TestCase):

    @classmethod
    def setUpTestData(cls):
<<<<<<< HEAD
        cls.author = get_user_model().objects.create(username='Лев Толстой')
        cls.reader = get_user_model().objects.create(username='Читатель простой')
=======
        cls.author = User.objects.create(username='Лев Толстой')
        cls.reader = User.objects.create(username='Читатель простой')
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        cls.note = Note.objects.create(
            title='Заголовок',
            text='Текст заметки',
            slug='note-slug',
            author=cls.author,
        )

    def test_notes_list_for_different_users(self):
        users_notes = (
            (self.author, True),
            (self.reader, False),
        )
        url = reverse('notes:list')
        for user, note_in_list in users_notes:
<<<<<<< HEAD
            with self.subTest(user=user.username, note_in_list=note_in_list):
                self.client.force_login(user)
                response = self.client.get(url)
                note_in_object = self.note in response.context['object_list']
                self.assertEqual(note_in_object, note_in_list)
=======
            self.client.force_login(user)
            with self.subTest(user=user.username, note_in_list=note_in_list):
                response = self.client.get(url)
                note_in_object_list = self.note in response.context[
                    'object_list']
                self.assertEqual(note_in_object_list, note_in_list)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7

    def test_pages_contains_form(self):
        urls = (
            ('notes:add', None),
            ('notes:edit', (self.note.slug,)),
        )
        for page, args in urls:
            with self.subTest(page=page):
                url = reverse(page, args=args)
                self.client.force_login(self.author)
                response = self.client.get(url)
                self.assertIn('form', response.context)
<<<<<<< HEAD
                form = response.context['form']
                self.assertIsInstance(form, NoteForm)
=======
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
