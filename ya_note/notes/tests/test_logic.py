<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from notes.forms import WARNING
from notes.models import Note

=======
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from notes.models import Note
from notes.forms import WARNING
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
from pytils.translit import slugify

User = get_user_model()

<<<<<<< HEAD
SUCCESS_URL = reverse('notes:success')
=======
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7

class TestNoteCreation(TestCase):
    ADD_NOTE_URL = reverse('notes:add')

    @classmethod
    def setUpTestData(cls):
<<<<<<< HEAD
        cls.author = get_user_model().objects.create(username='Лев Толстой')
        cls.form_data = {
            'title': 'Form title',
            'text': 'Form text',
            'slug': 'form-slug'
        }
=======
        cls.author = User.objects.create(username='Лев Толстой')
        cls.form_data = {'title': 'Form title',
                         'text': 'Form text',
                         'slug': 'form-slug'}

    @staticmethod
    def _get_err_msg(current, expected):
        return f'Текущее значение "{current}", Ожидалось "{expected}"'
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7

    def test_user_can_create_note(self):
        self.client.force_login(self.author)
        response = self.client.post(self.ADD_NOTE_URL, data=self.form_data)
<<<<<<< HEAD
        self.assertRedirects(response, SUCCESS_URL)
=======
        self.assertRedirects(response, reverse('notes:success'))
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        expected_notes_count = 1
        current_notes_count = Note.objects.count()
        self.assertEqual(current_notes_count, expected_notes_count,
                         self._get_err_msg(current_notes_count,
                                           expected_notes_count))
<<<<<<< HEAD
        new_note = Note.objects.filter(slug=self.form_data['slug']).last()
=======
        new_note = Note.objects.filter(slug=self.form_data['slug']).first()
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        self.assertIsNotNone(new_note)
        self.assertEqual(new_note.title, self.form_data['title'])
        self.assertEqual(new_note.text, self.form_data['text'])
        self.assertEqual(new_note.slug, self.form_data['slug'])
        self.assertEqual(new_note.author, self.author)

    def test_anonymous_user_cant_create_note(self):
        response = self.client.post(self.ADD_NOTE_URL, data=self.form_data)
        login_url = reverse('users:login')
        expected_url = f'{login_url}?next={self.ADD_NOTE_URL}'
        self.assertRedirects(response, expected_url)
        expected_notes_count = 0
        current_notes_count = Note.objects.count()
        self.assertEqual(current_notes_count, expected_notes_count,
                         self._get_err_msg(current_notes_count,
                                           expected_notes_count))

    def test_slug_must_be_unique(self):
        self.client.force_login(self.author)
        self.client.post(self.ADD_NOTE_URL, data=self.form_data)
        res = self.client.post(self.ADD_NOTE_URL, data=self.form_data)
        warn = self.form_data['slug'] + WARNING
        self.assertFormError(res, form='form', field='slug', errors=warn)

    def test_empty_slug(self):
        self.client.force_login(self.author)
        del self.form_data['slug']
        res = self.client.post(self.ADD_NOTE_URL,
                               data=self.form_data)
<<<<<<< HEAD
        self.assertRedirects(res, SUCCESS_URL)
=======
        self.assertRedirects(res, reverse('notes:success'))
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        expected_notes_count = 1
        current_notes_count = Note.objects.count()
        self.assertEqual(current_notes_count, expected_notes_count,
                         self._get_err_msg(current_notes_count,
                                           expected_notes_count))
        expected_slug = slugify(self.form_data['title'])
        new_note = Note.objects.filter(slug=expected_slug).first()
        self.assertIsNotNone(new_note)
        self.assertEqual(new_note.slug, expected_slug,
                         self._get_err_msg(new_note.slug,
                                           expected_slug))

<<<<<<< HEAD
    @staticmethod
    def _get_err_msg(current, expected):
        return f'Текущее значение "{current}", Ожидалось "{expected}"'

=======
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7

class TestNoteEditDelete(TestCase):
    NOTE_TITLE = 'title'
    NEW_NOTE_TITLE = 'updated title'
    NOTE_TEXT = 'text'
    NEW_NOTE_TEXT = 'updated text'

    @classmethod
    def setUpTestData(cls):
<<<<<<< HEAD
        cls.author = get_user_model().objects.create(username='Лев Толстой')
        cls.reader = get_user_model().objects.create(username='Читатель простой')
=======
        cls.author = User.objects.create(username='Лев Толстой')
        cls.author_client = Client()
        cls.author_client.force_login(cls.author)
        cls.reader = User.objects.create(username='Читатель простой')
        cls.reader_client = Client()
        cls.reader_client.force_login(cls.reader)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        cls.note = Note.objects.create(
            title=cls.NOTE_TITLE,
            text=cls.NOTE_TEXT,
            slug='note-slug',
            author=cls.author,
        )
        cls.edit_note_url = reverse('notes:edit', args=[cls.note.slug])
        cls.delete_note_url = reverse('notes:delete', args=[cls.note.slug])
        cls.form_data = {
            'title': cls.NEW_NOTE_TITLE,
<<<<<<< HEAD
            'text': cls.NEW_NOTE_TEXT
        }

    def test_author_can_edit_note(self):
        self.client.force_login(self.author)
        self.client.post(self.edit_note_url, self.form_data)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, self.NEW_NOTE_TITLE)
        self.assertEqual(self.note.text, self.NEW_NOTE_TEXT)
        self.assertEqual(self.note.author, self.author)

    def test_other_user_cant_edit_note(self):
        self.client.force_login(self.reader)
        res = self.client.post(self.edit_note_url, self.form_data)
=======
            'text': cls.NEW_NOTE_TEXT}

    def test_author_can_edit_note(self):
        self.author_client.post(self.edit_note_url, self.form_data)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, self.NEW_NOTE_TITLE)
        self.assertEqual(self.note.text, self.NEW_NOTE_TEXT)

    def test_other_user_cant_edit_note(self):
        res = self.reader_client.post(self.edit_note_url, self.form_data)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        self.assertEqual(res.status_code, HTTPStatus.NOT_FOUND)
        note_from_db = Note.objects.filter(id=self.note.id).first()
        self.assertIsNotNone(note_from_db)
        self.assertEqual(self.note.title, note_from_db.title)
        self.assertEqual(self.note.text, note_from_db.text)
<<<<<<< HEAD
        self.assertEqual(note_from_db.author, self.author)

    def test_author_can_delete_note(self):
        self.client.force_login(self.author)
        res = self.client.post(self.delete_note_url)
        self.assertRedirects(res, SUCCESS_URL)
        self.assertEqual(Note.objects.count(), 0)

    def test_other_user_cant_delete_note(self):
        self
=======

    def test_author_can_delete_note(self):
        res = self.author_client.post(self.delete_note_url)
        self.assertRedirects(res, reverse('notes:success'))
        self.assertEqual(Note.objects.count(), 0)

    def test_other_user_cant_delete_note(self):
        res = self.reader_client.post(self.delete_note_url)
        self.assertEqual(res.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(Note.objects.count(), 1)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
