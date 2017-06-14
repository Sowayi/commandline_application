import httpclient

def user_view_post():
    print('='*20)
    print("See Post")
    print('=' * 20)
    number = input("What is the number of the post you wish to see: ")

    if number.isdigit():
        number = int(number)
    get_post = httpclient.describe_post(number)

    if get_post.status_code != 200:
        raise ApiError('Post unavailable: {}'.format(get_post.status_code))

    print("Post requested. \n ID: {}\n Title: {}\n Body: {}".format(get_post.json()["id"],
                                                                    get_post.json()["title"],
                                                                    get_post.json()["body"]
                                                                    )
          )


def user_add_post():
    print("Please add post: ")
    print('='*10)
    print("Add Post")
    print('=' * 10)

    topic = input("Give your post a topic ")
    body = input("Create body")

    add = httpclient.add_post(title, body)
    if add.status_code != 201:
        raise ApiError('Unable to create post: {}'.format(add.status_code))
    print("Post added. \n ID: {}\n Title: {}\n Body: {}".format(add.json()["id"],
                                                                add.json()["title"],
                                                                add.json()["body"]
                                                                )
          )


def user_post_update():
    print("Time to update a post: ")
    print('='*10)
    print("Update Post")
    print('=' * 10)
    title = input("update title ")
    body = input("update body")

    update = httpclient.update_post(title, body)

    print(update.status_code)

    if update.status_code != 200:
        if update.status_code == 404:
            raise Exception('Post cannot be found: {}'.format(update.status_code))
        else:
            raise Exception('No permissions to update post: '.format(update.status_code))

    print("Post updated. \n ID: {}\n Title: {}\n Body: {}".format(update.json()["id"],
                                                                  update.json()["title"],
                                                                  update.json()["body"]
                                                                 )
          )


def main():
    print("This is a simple http client to view or update posts")


    user_view_post()

    user_add_post()

    user_post_update()

if __name__ == '__main__':
    main()
