"""Fizz Buzz game with a twist to it."""
import argparse
import json


class FizzBuzzGame:
    """FizzBuzz game class."""

    def __init__(self, rules):
        """init method for the class."""
        self.rulesDivisible = rules["divisible"]
        self.rulesEndsWith = rules["ends"]

    def buzzer(self, n: int) -> list:
        """Function generates FizzBuzz."""
        output = []
        for i in range(1, n+1):
            answer_string = ""
            for key in self.rulesDivisible.keys():
                if i % int(key) == 0:
                    answer_string += self.rulesDivisible[key]
            for key in self.rulesEndsWith.keys():
                if (i - int(key)) % 10 == 0:
                    answer_string += self.rulesEndsWith[key]
            if not answer_string:
                answer_string = str(i)
            output.append(answer_string)
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
    parser.add_argument('range', type=int, default=100, const=100, nargs='?',
                        help="enter the number to run the fizzbuzz game until")
    parser.add_argument(
        '--output', type=str, help="enter the type of output you desire the fizzbuzz to go into")
    parser.add_argument(
        '--rules', type=str, help="a json file that contians the rules for modified fizzbuzz game")
    args = parser.parse_args()

    fb = FizzBuzzGame(json.loads(args.rules))
    result = fb.buzzer(args.range)
    fb.output(result, args.output)


if __name__ == "__main__":
    print("Hello, welcome to a Fizz Buzz game")
    main()


# sample input to console
#
# python3 step3.py 15 --rules '{
#     "divisible":{
#         "3": "Fizz",
#         "5": "Buzz"
#     },
#     "ends":{
#         "3": "Foo",
#         "5": "Bar"
#     }
# }'
