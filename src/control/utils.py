


class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
        learn from tornado  utils.py
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value



def _content(blogs):
    if not isinstance(blogs, list):
        posts = [posts]

    return [ObjectDict({
        'title': post.title,
        'url': post.url,
        'content': markdown(post.content),
        'created_time': post.created_time,
        'tags': post.tags,
        'type': post.type,}) for post in posts]

