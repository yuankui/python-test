import sys


class Name:
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


def first(self, *args, **kwargs):
    print(args)
    print(kwargs)


Name.__call__ = first

Name()
# Name()('hello', 'kitty', name="first", age="this is hello")
