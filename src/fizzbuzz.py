from rx import from_iterable
from rx.operators import to_list, map


class FizzBuzz:
    def fixxBuzz(self):
        return from_iterable(range(1, 101)).pipe(
            map(lambda i: "Fizz" if i % 3 == 0 else i),
            to_list()).run()


def _fizzBuzz(i):
    if (i % 3 == 0) and (i % 5 == 0):
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i.toString()
