from enum import Enum
import gettext


translation_instance = None


class Language(Enum):
    ENGLISH = "en"
    FRENCH = "fr"
    SPANISH = "es"


def switch_language(language: Language) -> None:
    translation_instance = gettext.translation(
        'gui', localedir='locale', languages=[language.value])
    translation_instance.install()


def str_to_language(string: str) -> Language:
    if string == "en":
        return Language.ENGLISH
    elif string == "fr":
        return Language.FRENCH
    elif string == "es":
        return Language.SPANISH
    else:
        raise Exception("Language doesn't exists.")


if __name__ == '__main__':
    pass
