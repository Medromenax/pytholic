class NotVivaCristoReiError(Exception):
    def __str__(self):
        print("Viva Cristo Rei!")


class ChapterDoesntExistError(Exception):
    def __str__(self):
        print("Chapter doesn't exist.")


class VerseDoesntExistError(Exception):
    def __str__(self):
        print("Verse doesn't exist.")


class StartVerseGreaterThanEndOneError(Exception):
    def __str__(self):
        print("End verse must be greater than start verse.")


class ChapterAndVerseMustBeIntError(Exception):
    def __str__(self):
        print("Chapter or verse must be Int.")


class EndVerseEqualToStartOne(Exception):
    def __str__(self):
        print("End verse must not be equal to start verse.")
