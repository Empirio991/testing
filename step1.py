"""Fizz Buzz game with a little more buzz."""
import argparse


class FizzBuzz:
    """FizzBuzz class."""

    def buzzer(self, n: int) -> None:
        """Function generates FizzBuzz."""
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print("{}".format(i))


def main():
    """ Main method for the script."""
    parser = argparse.ArgumentParser(description="get some input from users")
    parser.add_argument('range', type=int,
                        help="enter the number to run the fizzbuzz game until")
    args = parser.parse_args()
    fb = FizzBuzz()
    fb.buzzer(args.range)


if __name__ == "__main__":
    print("Hello, welcome to a Fizz Buzz game")
    main()


# Sample input to console
#
# python3 step1.py 100
