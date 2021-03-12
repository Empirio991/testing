"""
Very flexible Object oriented fizz buzz.

In this my general apporach will be to create seperate rule class.
extended it for the differet possible rules and create a chain of rules to apply.
"""


class Rule:
    def applyTo(self, number):
        pass


class NoMatchRule(Rule):
    def applyTo(self, number):
        return str(number)


class HamRule(Rule):

    def __init__(self, nextRule):
        self.nextRule = nextRule

    def applyTo(self, number):
        return "ham" if number % 3 == 0 or (number - 5) % 10 == 0 else self.nextRule.applyTo(number)


class EggsRule(Rule):

    def __init__(self, nextRule):
        self.nextRule = nextRule

    def applyTo(self, number):
        return "eggs" if number % 5 == 0 else self.nextRule.applyTo(number)


class SpamRule(Rule):

    def __init__(self, nextRule):
        self.nextRule = nextRule

    def isPrime(self, number):
        if number > 1:
            for i in range(2, (number//2) + 1):
                if number % i == 0:
                    return False
            return True
        return False

    def applyTo(self, number):
        return "spam" if self.isPrime(number) and (number - 7) % 10 == 0 else self.nextRule.applyTo(number)


class FizzRule(Rule):
    def __init__(self, nextRule):
        self.nextRule = nextRule

    def applyTo(self, number):
        return "Fizz" if number % 3 == 0 else self.nextRule.applyTo(number)


class CompositeExampleRule(Rule):
    def applyTo(self, number):
        noMatchRule = NoMatchRule()
        hamRule = HamRule(noMatchRule)
        eggsRule = EggsRule(hamRule)
        spamRule = SpamRule(eggsRule)

        return spamRule.applyTo(number)


class NumericRange:
    def __init__(self, end):
        self.range_end = end + 1
        self.range_start = 1

    def apply(self, rule: Rule):
        return [rule.applyTo(ele) for ele in range(self.range_start, self.range_end)]


"""
if I had more time, 
the implementation will start with a main function that gathers the input range from the user.
followed by the rules definition. we deconstruct that into class or compositie rules based on what we choose to implement.
I will also increase the number of rules class to help with building more composite and unique rules.
"""
