class switch(object):
    """Implementation of a C-like switch-case.

        Example:
            number = 2
            for case in switch(number):
                if case(1):
                    print("Your number is 1")
                    break
                if case(2):
                    print("Your number is 2")
                    break
                if case(3):
                    print("Your number is 3")
                    break
                if case():
                    # Default case
                    print("I can't find your number")

            # Executing this code snippet print the following line :
            Your number is 2
    """
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


if __name__ == "__main__":
    pass
