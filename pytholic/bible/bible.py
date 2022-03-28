from pytholic.bible._exceptions import NotVivaCristoReiError as _nc
from pytholic.bible._books import BibleBooks as _bb


class Bible(_bb):
    """Contains the 4 gospels of the New Jerusalem Bible Edition

    These gospels are represented by the following methods: matthew(), mark(),
    luke() and john(). They receive three arguments, the first one is for the
    chapter number, the second one for the verse number and an optional third
    argument can be passed, it represents a final verse, for example,
    Matthew 1, 1-5, that "5" would be represented by the final verse, the
    third argument.

    >>> bible = Bible()
    >>> print(bible.matthew(1, 1))
    Roll of the genealogy of Jesus Christ, son of David, son of Abraham:

    >>> print(bible.mark(1, 1, 2))
    ['1. The beginning of the gospel about Jesus Christ, the Son of God. ', '2. It is written in the prophet Isaiah: Look, I am going to send my messenger in front of you to prepare your way before you. ']
    """

    def __init__(self):
        self.viva_cristo_rei = "Viva Cristo Rei"

        if self.viva_cristo_rei != "Viva Cristo Rei":
            raise _nc


if __name__ == "__main__":
    import doctest
    doctest.testmod()