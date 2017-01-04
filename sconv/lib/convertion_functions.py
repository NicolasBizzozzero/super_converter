def convert(number: str, src_base: int, dest_base: int) -> str:
    """ Convert 'number' from 'src_base' to 'dest_base'. """
    if src_base == 2:
        number = "{}{}".format("0b", number)
    elif src_base == 10:
        pass
    elif src_base == 16:
        number = "{}{}".format("0x", number)
    else:
        return "Invalid base"

    if not is_a_number(number, src_base):
        return "{}\n{}\n{}".format(_("Not a number"), _("or"), _("wrong base"))

    if src_base == 2 and dest_base == 2:
        return str(number)[2:]
    elif src_base == 2 and dest_base == 10:
        return str(int(number, base=2))
    elif src_base == 2 and dest_base == 16:
        return str(hex(int(number, base=2)))[2:].upper()
    elif src_base == 10 and dest_base == 2:
        return str(bin(int(number)))[2:]
    elif src_base == 10 and dest_base == 10:
        return number
    elif src_base == 10 and dest_base == 16:
        return str(hex(int(number)))[2:].upper()
    elif src_base == 16 and dest_base == 2:
        return str(bin(int(number, 16)))[2:]
    elif src_base == 16 and dest_base == 10:
        return str(int(number, 16))
    elif src_base == 16 and dest_base == 16:
        return number[2:]
    else:
        return "Invalid bases"


def is_a_number(number: str, _base: int) -> bool:
    try:
        int(number, base=_base)
        return True
    except ValueError:
        pass
    return False


if __name__ == '__main__':
    pass
