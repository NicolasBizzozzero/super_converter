""" A module used to convert a temperature into different scales.

Currently, the supported scales are :
- Celsius
- Delisle
- Fahrenheit
- Kelvin
- Newton
- Rankine
- Réaumur
- Rømer
All of the name, units and formulas have been scraped from the following page:
http://webcache.googleusercontent.com/search?q=cache:en.wikipedia.org/wiki/Conversion_of_units_of_temperature

Examples:
# Convert 100°C to Fahrenheit
>>> temp1 = Temperature(100, Scale.CELSIUS)
>>> print(temp1)
100°C
>>> temp1.convert(Scale.FAHRENHEIT)
>>> print(temp1)
212.0°F

# Convert 54°Rø to Delisle
>>> temp2 = Temperature(54, Scale.ROMER)
>>> print(temp2)
54°Rø
>>> temp2.convert(Scale.DELISLE)
>>> print(temp2)
17.143°D
"""

from enum import Enum

from lib.tools.switchcase import switch


class UnknownScale(Exception):
    pass


class Scale(Enum):
    CELSIUS = 0
    DELISLE = 1
    FAHRENHEIT = 2
    KELVIN = 3
    NEWTON = 4
    RANKINE = 5
    REAUMUR = 6
    ROMER = 7


class Temperature():
    """ A couple of a scale and a value.

        Attributes:
            scale    The scale currently used to represent the temperature.
            value    The value associated to the temperature.
    """

    def __init__(self, value: float, scale: Scale):
        self.value = value
        self.scale = scale

    def __str__(self):
        unit = None
        for case in switch(self.scale):
            if case(Scale.CELSIUS):
                unit = "°C"
                break
            if case(Scale.DELISLE):
                unit = "°D"
                break
            if case(Scale.FAHRENHEIT):
                unit = "°F"
                break
            if case(Scale.KELVIN):
                unit = "K"
                break
            if case(Scale.NEWTON):
                unit = "°N"
                break
            if case(Scale.RANKINE):
                unit = "°Ra"
                break
            if case(Scale.REAUMUR):
                unit = "°Ré"
                break
            if case(Scale.ROMER):
                unit = "°Rø"
                break
        return "{}{}".format(self.value, unit)

    def convert(self, newScale: Scale, rounding: int = 3):
        if self.scale == newScale:
            return

        for case in switch(self.scale):
            if case(Scale.CELSIUS):
                for case in switch(newScale):
                    if case(Scale.DELISLE):
                        self.value = celsius_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = celsius_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = celsius_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = celsius_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = celsius_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = celsius_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = celsius_to_romer(self.value)
                        break
                break

            if case(Scale.DELISLE):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = delisle_to_celsius(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = delisle_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = delisle_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = delisle_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = delisle_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = delisle_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = delisle_to_romer(self.value)
                        break
                break

            if case(Scale.FAHRENHEIT):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = fahrenheit_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = fahrenheit_to_delisle(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = fahrenheit_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = fahrenheit_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = fahrenheit_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = fahrenheit_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = fahrenheit_to_romer(self.value)
                        break
                break

            if case(Scale.KELVIN):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = kelvin_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = kelvin_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = kelvin_to_fahrenheit(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = kelvin_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = kelvin_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = kelvin_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = kelvin_to_romer(self.value)
                        break
                break

            if case(Scale.NEWTON):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = newton_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = newton_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = newton_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = newton_to_kelvin(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = newton_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = newton_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = newton_to_romer(self.value)
                        break
                break

            if case(Scale.RANKINE):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = rankine_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = rankine_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = rankine_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = rankine_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = rankine_to_newton(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = rankine_to_reaumur(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = rankine_to_romer(self.value)
                        break
                break

            if case(Scale.REAUMUR):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = reaumur_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = reaumur_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = reaumur_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = reaumur_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = reaumur_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = reaumur_to_rankine(self.value)
                        break
                    if case(Scale.ROMER):
                        self.value = reaumur_to_romer(self.value)
                        break
                break

            if case(Scale.ROMER):
                for case in switch(newScale):
                    if case(Scale.CELSIUS):
                        self.value = romer_to_celsius(self.value)
                        break
                    if case(Scale.DELISLE):
                        self.value = romer_to_delisle(self.value)
                        break
                    if case(Scale.FAHRENHEIT):
                        self.value = romer_to_fahrenheit(self.value)
                        break
                    if case(Scale.KELVIN):
                        self.value = romer_to_kelvin(self.value)
                        break
                    if case(Scale.NEWTON):
                        self.value = romer_to_newton(self.value)
                        break
                    if case(Scale.RANKINE):
                        self.value = romer_to_rankine(self.value)
                        break
                    if case(Scale.REAUMUR):
                        self.value = romer_to_reaumur(self.value)
                        break
                break

        self.value = round(self.value, ndigits=rounding)
        self.scale = newScale


def celsius_to_delisle(temperature: float) -> float:
    return (100 - temperature) * (3 / 2)


def celsius_to_fahrenheit(temperature: float) -> float:
    return (temperature * (9 / 5)) + 32


def celsius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def celsius_to_newton(temperature: float) -> float:
    return temperature * (33 / 100)


def celsius_to_rankine(temperature: float) -> float:
    return (temperature + 273.15) * (9 / 5)


def celsius_to_reaumur(temperature: float) -> float:
    return temperature * (4 / 5)


def celsius_to_romer(temperature: float) -> float:
    return (temperature * (21 / 40)) + 7.5


def delisle_to_celsius(temperature: float) -> float:
    return 100 - (temperature * (2 / 3))


def delisle_to_fahrenheit(temperature: float) -> float:
    return 212 - (temperature * (6 / 5))


def delisle_to_kelvin(temperature: float) -> float:
    return 373.15 - (temperature * (2 / 3))


def delisle_to_newton(temperature: float) -> float:
    return 33 - (temperature * (11 / 50))


def delisle_to_rankine(temperature: float) -> float:
    return 671.67 - (temperature * (6 / 5))


def delisle_to_reaumur(temperature: float) -> float:
    return 80 - (temperature * (8 / 15))


def delisle_to_romer(temperature: float) -> float:
    return 60 - (temperature * (7 / 20))


def fahrenheit_to_celsius(temperature: float) -> float:
    return (temperature - 32) * (5 / 9)


def fahrenheit_to_delisle(temperature: float) -> float:
    return (212 - temperature) * (5 / 6)


def fahrenheit_to_kelvin(temperature: float) -> float:
    return (temperature + 459.67) * (5 / 9)


def fahrenheit_to_newton(temperature: float) -> float:
    return (temperature - 32) * (11 / 60)


def fahrenheit_to_rankine(temperature: float) -> float:
    return temperature + 459.67


def fahrenheit_to_reaumur(temperature: float) -> float:
    return (temperature - 32) * (4 / 9)


def fahrenheit_to_romer(temperature: float) -> float:
    return ((temperature - 32) * (7 / 24)) + 7.5


def kelvin_to_celsius(temperature: float) -> float:
    return temperature - 273.15


def kelvin_to_delisle(temperature: float) -> float:
    return (373.15 - temperature) * (3 / 2)


def kelvin_to_fahrenheit(temperature: float) -> float:
    return (temperature * (9 / 5)) - 459.67


def kelvin_to_newton(temperature: float) -> float:
    return (temperature - 273.15) * (33 / 100)


def kelvin_to_rankine(temperature: float) -> float:
    return temperature * (9 / 5)


def kelvin_to_reaumur(temperature: float) -> float:
    return (temperature - 273.15) * (4 / 5)


def kelvin_to_romer(temperature: float) -> float:
    return ((temperature - 273.15) * (21 / 40)) + 7.5


def newton_to_celsius(temperature: float) -> float:
    return temperature * (100 / 33)


def newton_to_delisle(temperature: float) -> float:
    return (33 - temperature) * (50 / 11)


def newton_to_fahrenheit(temperature: float) -> float:
    return (temperature * (60 / 11)) + 32


def newton_to_kelvin(temperature: float) -> float:
    return (temperature * (100 / 33)) + 273.15


def newton_to_rankine(temperature: float) -> float:
    return (temperature * (60 / 11)) + 491.67


def newton_to_reaumur(temperature: float) -> float:
    return temperature * (80 / 33)


def newton_to_romer(temperature: float) -> float:
    return (temperature * (35 / 22)) + 7.5


def rankine_to_celsius(temperature: float) -> float:
    return (temperature - 491.67) * (5 / 9)


def rankine_to_delisle(temperature: float) -> float:
    return (671.67 - temperature) * (5 / 6)


def rankine_to_fahrenheit(temperature: float) -> float:
    return temperature - 459.67


def rankine_to_kelvin(temperature: float) -> float:
    return temperature * (5 / 9)


def rankine_to_newton(temperature: float) -> float:
    return (temperature - 491.67) * (11 / 60)


def rankine_to_reaumur(temperature: float) -> float:
    return (temperature - 491.67) * (4 / 9)


def rankine_to_romer(temperature: float) -> float:
    return ((temperature - 491.67) * (7 / 24)) + 7.5


def reaumur_to_celsius(temperature: float) -> float:
    return temperature * (5 / 4)


def reaumur_to_delisle(temperature: float) -> float:
    return (80 - temperature) * (15 / 8)


def reaumur_to_fahrenheit(temperature: float) -> float:
    return (temperature * (9 / 4)) + 32


def reaumur_to_kelvin(temperature: float) -> float:
    return (temperature * (5 / 4)) + 273.15


def reaumur_to_newton(temperature: float) -> float:
    return temperature * (33 / 80)


def reaumur_to_rankine(temperature: float) -> float:
    return (temperature * (9 / 4)) + 491.67


def reaumur_to_romer(temperature: float) -> float:
    return (temperature * (21 / 32)) + 7.5


def romer_to_celsius(temperature: float) -> float:
    return (temperature - 7.5) * (40 / 21)


def romer_to_delisle(temperature: float) -> float:
    return (60 - temperature) * (20 / 7)


def romer_to_fahrenheit(temperature: float) -> float:
    return ((temperature - 7.5) * (24 / 7)) + 32


def romer_to_kelvin(temperature: float) -> float:
    return ((temperature - 7.5) * (40 / 21)) + 273.15


def romer_to_newton(temperature: float) -> float:
    return (temperature - 7.5) * (22 / 35)


def romer_to_rankine(temperature: float) -> float:
    return ((temperature - 7.5) * (24 / 7)) + 491.67


def romer_to_reaumur(temperature: float) -> float:
    return (temperature - 7.5) * (32 / 21)


if __name__ == '__main__':
    pass
