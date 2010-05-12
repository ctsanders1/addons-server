from django import test

from nose.tools import eq_


def test_no_vary_cookie():
    c = test.Client()

    # We don't break good usage of Vary.
    response = test.Client().get('/')
    eq_(response['Vary'], 'Accept-Language')

    # But we do prevent Vary: Cookie.
    response = test.Client().get('/', follow=True)
    assert 'Vary' not in response


def test_redirect_with_unicode_get():
    response = test.Client().get('/da/firefox/addon/5457?from=/da/firefox/addon/5457%3Fadvancedsearch%3D1&lang=ja&utm_source=Google+%E3%83%90%E3%82%BA&utm_medium=twitter&utm_term=Google+%E3%83%90%E3%82%BA')
    eq_(response.status_code, 301)
