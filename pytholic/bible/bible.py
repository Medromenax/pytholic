from pytholic.bible._exceptions import NotVivaCristoReiError as _nc
from pytholic.bible._books import BibleBooks as _bb


class Bible(_bb):
    """Contains the 4 gospels of the New Jerusalem Bible Edition

    The gospels are: Matthew, Mark, Luke and John. Each of these methods
    receives three arguments, the first one is for the chapter number, the
    second one for the verse number and, alternatively, a third one can be
    passed as a final verse, to represent the read of more than one verse,
    for example, Matthew 1, 1-5, in this case, a list
    containing the verses is returned.
    """

    def __init__(self):
        self.viva_cristo_rei = "Viva Cristo Rei"

        if self.viva_cristo_rei != "Viva Cristo Rei":
            raise _nc
