import requests


def _url(path):
    return 'https://jsonplaceholder.typicode.com' + path


def get_posts():
    resp = requests.get(_url('/posts/'))
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /posts/ {}'.format(resp.status_code))

    return resp


def describe_post(post_id):
    if 0 < post_id > 100:
        # raise an error if the range is not within 0-100
        raise IndexError
    return requests.get(_url('/posts/{:d}'.format(post_id)))


def add_post(title, body, user_id=10):
    return requests.post(_url('/posts/'), json={
        'user_id': user_id,
        'title': title,
        'body': body,
        })


def update_post(title, body, post_id=100, user_id=10):
    if 0 < post_id > 100:
        raise IndexError
    return requests.put(_url('/posts/:id'.format(post_id)), json={
        'userId': user_id,
        'id': post_id,
        'title': title,
        'body': body,
    })
