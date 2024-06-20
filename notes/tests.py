from django.test import TestCase
from .models import Note, Post
from django.urls import reverse
from .forms import NoteForm, PostForm


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="Just a test note")

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "Just a test note")
        self.assertIsNotNone(self.note.created_at)
        self.assertIsNotNone(self.note.updated_at)


class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Just a test post")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Just a test post")
        self.assertIsNotNone(self.post.created_at)
        self.assertIsNotNone(self.post.updated_at)


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Another Test Note", content="More testing")

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another Test Note")
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another Test Note")
        self.assertTemplateUsed(response, 'notes/note_detail.html')


class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Another Test Post", content="More testing")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another Test Post")
        self.assertTemplateUsed(response, 'notes/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Another Test Post")
        self.assertTemplateUsed(response, 'notes/post_detail.html')


class NoteFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': "Test Note", 'content': "Just a test note"}
        form = NoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': "", 'content': "Just a test note"}
        form = NoteForm(data=data)
        self.assertFalse(form.is_valid())


class PostFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': "Test Post", 'content': "Just a test post"}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': "", 'content': "Just a test post"}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
