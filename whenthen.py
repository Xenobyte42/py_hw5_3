def whenthen(func):

    class WhenThen:
        def __init__(self, func):
            self._func = func
            self._when = []
            self._then = []

        def __call__(self, *args, **kwargs):
            for idx, func in enumerate(self._when):
                if func(*args, **kwargs):
                    return self._then[idx](*args, **kwargs)
            return self._func(*args, **kwargs)

        def when(self, func):
            if len(self._when) != len(self._then):
                raise SyntaxError
            self._when.append(func)
            return self

        def then(self, func):
            if len(self._when) - 1 != len(self._then):
                raise SyntaxError
            self._then.append(func)
            return self

    return WhenThen(func)

@whenthen
def fract(x):
    return x * fract(x - 1)


@fract.when
def fract(x):
    return x == 0


@fract.then
def fract(x):
    return 1


@fract.when
def fract(x):
    return x > 5


@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)

if __name__ == "__main__":
    print(fract(6))
