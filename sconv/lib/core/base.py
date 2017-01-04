from enum import Enum


class NotANumberOrWrongBase(Exception):
    pass


class Base(Enum):
    NONE = 0
    BINARY = 2
    DECIMAL = 10
    HEXADECIMAL = 16


class NumberWithBase():
    """A number associated with a base.

    Attributes:
        base         An enum representing the current base of the number.
        number       A string representation of the number.
        IS_INVALID   A boolean flag set to True if the string representation
                     of the number makes no sense with the current base.
    """

    def __init__(self, number: str, base: Base):
        self.number = number
        self.base = base
        self.IS_INVALID = not self.is_a_number()

    def __str__(self):
        if self.IS_INVALID:
            return "{}\n{}\n{}".format(_("Not a number"),
                                       _("or"),
                                       _("wrong base"))

        if self.base == Base.BINARY:
            prefix = 'b'
        elif self.base == Base.DECIMAL:
            prefix = 'd'
        elif self.base == Base.HEXADECIMAL:
            prefix = 'h'
        else:
            prefix = '?'
        return "0{}{}".format(prefix, self.number)

    def is_a_number(self) -> bool:
        """ Dirty method to check if a number is correctly written in his corresponding
            base.
        """
        try:
            int(self.number, base=self.base.value)
            return True
        except Exception:
            return False

    def convert(self, new_base: Base) -> None:
        # Convert the number into a new base
        if self.base == Base.BINARY:
            if new_base == Base.DECIMAL:
                self.base = Base.DECIMAL
                self.number = binary_to_decimal(self.number)
            elif new_base == Base.HEXADECIMAL:
                self.base = Base.HEXADECIMAL
                self.number = binary_to_hexadecimal(self.number)

        elif self.base == Base.DECIMAL:
            if new_base == Base.BINARY:
                self.base = Base.BINARY
                self.number = decimal_to_binary(self.number)
            elif new_base == Base.HEXADECIMAL:
                self.base = Base.HEXADECIMAL
                self.number = decimal_to_hexadecimal(self.number)

        elif self.base == Base.HEXADECIMAL:
            if new_base == Base.BINARY:
                self.base = Base.BINARY
                self.number = hexadecimal_to_binary(self.number)
            elif new_base == Base.DECIMAL:
                self.base = Base.DECIMAL
                self.number = hexadecimal_to_decimal(self.number)

        # Set the flag value if the number match his current base
        self.IS_INVALID = not self.is_a_number()


def binary_to_decimal(number: str) -> str:
    return str(int(number, base=2))


def binary_to_hexadecimal(number: str) -> str:
    return str(hex(int(number, base=2))).upper()


def decimal_to_binary(number: str) -> str:
    return str(bin(int(number)))


def decimal_to_hexadecimal(number: str) -> str:
    return str(hex(int(number))).upper()


def hexadecimal_to_binary(number: str) -> str:
    return str(bin(int(number, 16)))


def hexadecimal_to_decimal(number: str) -> str:
    return str(int(number, 16))


if __name__ == '__main__':
    pass
