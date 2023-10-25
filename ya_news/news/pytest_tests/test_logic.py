<<<<<<< HEAD
import pytest
from http import HTTPStatus
from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertFormError

=======
from http import HTTPStatus
from random import choice

import pytest
from pytest_django.asserts import assertRedirects, assertFormError

from django.urls import reverse

>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
from news.forms import BAD_WORDS, WARNING
from news.models import Comment

pytestmark = pytest.mark.django_db


<<<<<<< HEAD
def test_anonymous_user_cant_create_comment(client, form_data, news_detail_url):
    initial_comments_count = Comment.objects.count()
    response = client.post(news_detail_url, data=form_data)
    login_url = reverse('users:login')
    expected_url = f'{login_url}?next={news_detail_url}'
    assertRedirects(response, expected_url)
    comments_count = Comment.objects.count()
    assert comments_count == initial_comments_count, (
        'Количество комментариев в базе данных изменилось:'
        f' было {initial_comments_count}, стало {comments_count}'
    )


def test_user_can_create_comment(admin_user, admin_client, news, form_data):
=======
def test_anonymous_user_cant_create_comment(client, pk_from_news, form_data):
    url = reverse('news:detail', args=pk_from_news)
    response = client.post(url, data=form_data)
    login_url = reverse('users:login')
    expected_url = f'{login_url}?next={url}'
    assertRedirects(response, expected_url)
    comments_count = Comment.objects.count()
    expected_comments = 0
    assert comments_count == expected_comments, (
        f'Создано {comments_count} комментариев,'
        f' ожидалось {expected_comments}')


def test_user_can_create_comment(
        admin_user, admin_client, news, form_data):
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    url = reverse('news:detail', args=[news.pk])
    response = admin_client.post(url, data=form_data)
    expected_url = url + '#comments'
    assertRedirects(response, expected_url)
    comments_count = Comment.objects.count()
    expected_comments = 1
    assert comments_count == expected_comments, (
        f'Создано {comments_count} комментариев,'
<<<<<<< HEAD
        f' ожидалось {expected_comments}'
    )
    new_comment = Comment.objects.last()
=======
        f' ожидалось {expected_comments}')
    new_comment = Comment.objects.get()
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    assert new_comment.text == form_data['text']
    assert new_comment.news == news
    assert new_comment.author == admin_user


<<<<<<< HEAD
def test_user_cant_use_bad_words(admin_client, news_detail_url):
    bad_words_data = {'text': f'Какой-то text, {choice(BAD_WORDS)}, еще text'}
    response = admin_client.post(news_detail_url, data=bad_words_data)
=======
def test_user_cant_use_bad_words(admin_client, pk_from_news):
    bad_words_data = {'text': f'Какой-то text, {choice(BAD_WORDS)}, еще text'}
    url = reverse('news:detail', args=pk_from_news)
    response = admin_client.post(url, data=bad_words_data)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    assertFormError(response, form='form', field='text', errors=WARNING)
    comments_count = Comment.objects.count()
    expected_comments = 0
    assert comments_count == expected_comments


def test_author_can_edit_comment(
<<<<<<< HEAD
        author_client, pk_from_news, comment, form_data, news_edit_url
):
    original_author = comment.author
    original_news = comment.news
    response = author_client.post(news_edit_url, data=form_data)
=======
        author_client, pk_from_news, comment, form_data):
    url = reverse('news:edit', args=[comment.pk])
    response = author_client.post(url, data=form_data)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    expected_url = reverse('news:detail', args=pk_from_news) + '#comments'
    assertRedirects(response, expected_url)
    comment.refresh_from_db()
    assert comment.text == form_data['text'], (
<<<<<<< HEAD
        f'Комментарий "{comment.text}" не был обновлен,'
        f' ожидалось {form_data["text"]}'
    )
    assert comment.author == original_author, (
        'Автор комментария изменился после редактирования'
    )
    assert comment.news == original_news, (
        'Новость комментария изменилась после редактирования'
    )


def test_author_can_delete_comment(author_client, news_detail_url, news_delete_url):
    response = author_client.post(news_delete_url)
    expected_url = news_detail_url + '#comments'
=======
        f'Комментарий "{comment.text}" не был обновлен ,'
        f' ожидалось {form_data["text"]}')


def test_author_can_delete_comment(
        author_client, pk_from_news, pk_from_comment):
    url = reverse('news:delete', args=pk_from_comment)
    response = author_client.post(url)
    expected_url = reverse('news:detail', args=pk_from_news) + '#comments'
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    assertRedirects(response, expected_url)
    comments_count = Comment.objects.count()
    expected_comments = 0
    assert comments_count == expected_comments, (
        f'Создано {comments_count} комментариев,'
        f' ожидалось {expected_comments}')


def test_other_user_cant_edit_comment(
<<<<<<< HEAD
        admin_client, comment, form_data, news_edit_url):
    original_author = comment.author
    original_news = comment.news
    old_comment = comment.text
    response = admin_client.post(news_edit_url, data=form_data)
=======
        admin_client, pk_from_news, comment, form_data):
    url = reverse('news:edit', args=[comment.pk])
    old_comment = comment.text
    response = admin_client.post(url, data=form_data)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    assert response.status_code == HTTPStatus.NOT_FOUND
    comment.refresh_from_db()
    assert comment.text == old_comment, (
        f'Комментарий "{comment.text}" был обновлен,'
<<<<<<< HEAD
        f' ожидался {old_comment}'
    )
    assert comment.author == original_author, (
        'Автор комментария изменился после неудачной попытки редактирования'
    )
    assert comment.news == original_news, (
        'Новость комментария изменилась после неудачной попытки редактирования'
    )


def test_other_user_cant_delete_comment(admin_client, news_delete_url):
    response = admin_client.post(news_delete_url)
=======
        f' ожидался {old_comment}')


def test_other_user_cant_delete_comment(
        admin_client, pk_from_news, pk_from_comment):
    url = reverse('news:delete', args=pk_from_comment)
    response = admin_client.post(url)
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
    assert response.status_code == HTTPStatus.NOT_FOUND
    comments_count = Comment.objects.count()
    expected_comments = 1
    assert comments_count == expected_comments, (
        f'Создано {comments_count} комментариев,'
<<<<<<< HEAD
        f' ожидалось {expected_comments}'
    )
=======
        f' ожидалось {expected_comments}')
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
