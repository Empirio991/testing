"""Fizz Buzz game with a little more buzz."""
import argparse


class FizzBuzz:
    """FizzBuzz class."""

    def __init__(self):
        """init method for the class."""

    def buzzer(self, n: int) -> list:
        """Function generates FizzBuzz."""
        output = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 5 == 0:
                output.append("Buzz")
            elif i % 3 == 0:
                output.append("Fizz")
            else:
                output.append("{}".format(i))
        return output

    def output(self, outputList, outputType: str) -> None:
        """Prints the output using the desired method."""
        outputTypeDict = {
            "console": "console",
            "file": "file",
            "email": "email"
        }
        if outputType in outputTypeDict:
            for ele in outputList:
                print("{}: {}".format(outputTypeDict[outputType], ele))
        else:
            print("Output type is not defined, hence printing to console")
            for ele in outputList:
                print("{}: {}".format("console", ele))


def main():
    """ Main method for the script."""
    parser = argparse.ArgumentParser(description="get some input from users")
    parser.add_argument('range', type=int,
                        help="enter the number to run the fizzbuzz game until")
    parser.add_argument(
        '--output', type=str, help="enter the type of output you desire the fizzbuzz to go into")
    args = parser.parse_args()
    fb = FizzBuzz()
    result = fb.buzzer(args.range)
    fb.output(result, args.output)


if __name__ == "__main__":
    print("Hello, welcome to a Fizz Buzz game")
    main()


# Sample input to console
#
# python3 step2.py 10 --output email
#
# python3 step2.py 10 --output file
#
# python3 step2.py
