import pytest
<<<<<<< HEAD
from django.conf import settings
from django.urls import reverse
from news.forms import CommentForm

HOME_PAGE_URL = reverse('news:home')
=======
from django.urls import reverse
from django.conf import settings
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures('make_bulk_of_news')
def test_news_count(client):
<<<<<<< HEAD
    res = client.get(HOME_PAGE_URL)
    news_object = res.context['object_list']
    comments_count = len(news_object)
    msg = ('На главной странице должно находиться не больше '
=======
    url = reverse('news:home')
    res = client.get(url)
    object_list = res.context['object_list']
    comments_count = len(object_list)
    msg = (f'На главной странице должно находиться не больше '
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
           f'{settings.NEWS_COUNT_ON_HOME_PAGE} новостей,'
           f' выведено {comments_count}')
    assert comments_count == settings.NEWS_COUNT_ON_HOME_PAGE, msg


@pytest.mark.parametrize(
    'username, is_permitted', ((pytest.lazy_fixture('admin_client'), True),
                               (pytest.lazy_fixture('client'), False))
)
def test_comment_form_availability_for_different_users(
<<<<<<< HEAD
        news_detail_url, username, is_permitted):
    response = username.get(news_detail_url)
    result = 'form' in response.context
    assert result == is_permitted
    
    if is_permitted:
        form = response.context.get('form')
        assert isinstance(form, CommentForm)
=======
        pk_from_news, username, is_permitted):
    url = reverse('news:detail', args=pk_from_news)
    res = username.get(url)
    result = 'form' in res.context
    assert result == is_permitted
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7


@pytest.mark.usefixtures('make_bulk_of_news')
def test_news_order(client):
<<<<<<< HEAD
    res = client.get(HOME_PAGE_URL)
    news_object = res.context['object_list']
    sorted_list_of_news = sorted(news_object,
                                 key=lambda news: news.date,
                                 reverse=True)
    for as_is, to_be in zip(news_object, sorted_list_of_news):
        assert as_is.date == to_be.date, ('Должна быть первой в списке'
=======
    url = reverse('news:home')
    res = client.get(url)
    object_list = res.context['object_list']
    sorted_list_of_news = sorted(object_list,
                                 key=lambda news: news.date,
                                 reverse=True)
    for as_is, to_be in zip(object_list, sorted_list_of_news):
        assert as_is.date == to_be.date, (f'Должна быть первой в списке'
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
                                          f' новость "{to_be.title}" с датой'
                                          f' {to_be.date}, получена'
                                          f' "{as_is.title}" {as_is.date}')


@pytest.mark.usefixtures('make_bulk_of_comments')
def test_comments_order(client, pk_from_news):
    url = reverse('news:detail', args=pk_from_news)
    res = client.get(url)
<<<<<<< HEAD
    news_object = res.context['news'].comment_set.all()
    sorted_list_of_comments = sorted(news_object,
                                     key=lambda comment: comment.created)
    for as_is, to_be in zip(news_object, sorted_list_of_comments):
=======
    object_list = res.context['news'].comment_set.all()
    sorted_list_of_comments = sorted(object_list,
                                     key=lambda comment: comment.created)
    for as_is, to_be in zip(object_list, sorted_list_of_comments):
>>>>>>> 2a26fcd51061ee42c1e6bde16130be03ee1749b7
        msg = (
            f'Первым в списке должен быть комментарий "{to_be.text}" с датой'
            f' {to_be.created}, получен "{as_is.text}" {as_is.created}')
        assert as_is.created == to_be.created, msg
