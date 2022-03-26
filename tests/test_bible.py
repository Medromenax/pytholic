import unittest
from pytholic.bible.bible import Bible
from pytholic.bible._exceptions import ChapterDoesntExistError, VerseDoesntExistError, StartVerseGreaterThanEndOneError, ChapterAndVerseMustBeIntError, EndVerseEqualToStartOne


class TestBible(unittest.TestCase):
    def test_matthew_prints_right_verses(self):
        values = (
            (
                1, 1,
                "Roll of the genealogy of Jesus Christ, son of David, son of Abraham:"
            ),
            (
                2, 23,
                "There he settled in a town called Nazareth. In this way the words spoken through the prophets were to be fulfilled: He will be called a Nazarene."
            ),
            (
                9, 31,
                "But when they had gone away, they talked about him all over the countryside."
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse, text = value
            self.assertEqual(bible.matthew(chapter, verse), text)

    def test_matthew_prints_right_verse_list(self):
        values = (
            (
                10, 20, 23,
                [
                    '20. because it is not you who will be speaking; the Spirit of your Father will be speaking in you.',
                    "21. 'Brother will betray brother to death, and a father his child; children will come forward against their parents and have them put to death.",
                    '22. You will be universally hated on account of my name; but anyone who stands firm to the end will be saved.',
                    '23. If they persecute you in one town, take refuge in the next; and if they persecute you in that, take refuge in another. In truth I tell you, you will not have gone the round of the towns of Israel before the Son of man comes.'
                ]
            ),
            (
                11, 29, 30,
                [
                    '29. Shoulder my yoke and learn from me, for I am gentle and humble in heart, and you will find rest for your souls.',
                    "30. Yes, my yoke is easy and my burden light.'"
                ]
            ),
            (
                18, 9, 13,
                [
                    '9. And if your eye should be your downfall, tear it out and throw it away: it is better for you to enter into life with one eye, than to have two eyes and be thrown into the hell of fire. ',
                    "10. 'See that you never despise any of these little ones, for I tell you that their angels in heaven are continually in the presence of my Father in heaven. ",
                    '11. ',
                    "12. 'Tell me. Suppose a man has a hundred sheep and one of them strays; will he not leave the ninety-nine on the hillside and go in search of the stray? ",
                    '13. In truth I tell you, if he finds it, it gives him more joy than do the ninety-nine that did not stray at all. '
                ]
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse_start, verse_end, list = value
            self.assertEqual(bible.matthew(
                chapter, verse_start, verse_end), list)

    def test_mark_prints_right_verses(self):
        values = (
            (
                1, 1,
                "The beginning of the gospel about Jesus Christ, the Son of God. "
            ),
            (
                8, 37,
                "And indeed what can anyone offer in exchange for his life? "
            ),
            (
                16, 20,
                "while they, going out, preached everywhere, the Lord working with them and confirming the word by the signs that accompanied it."
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse, text = value
            self.assertEqual(bible.mark(chapter, verse), text)

    def test_mark_prints_right_verse_list(self):
        values = (
            (
                1, 1, 2,
                [
                    '1. The beginning of the gospel about Jesus Christ, the Son of God. ',
                    '2. It is written in the prophet Isaiah: Look, I am going to send my messenger in front of you to prepare your way before you. '
                ]
            ),
            (
                7, 5, 7,
                [
                    "5. So the Pharisees and scribes asked him, 'Why do your disciples not respect the tradition of the elders but eat their food with unclean hands?' ",
                    "6. He answered, 'How rightly Isaiah prophesied about you hypocrites in the passage of scripture: This people honours me only with lip-service, while their hearts are far from me. ",
                    '7. Their reverence of me is worthless; the lessons they teach are nothing but human commandments. '
                ]
            ),
            (
                16, 18, 20,
                [
                    "18. they will pick up snakes in their hands and be unharmed should they drink deadly poison; they will lay their hands on the sick, who will recover.' ",
                    '19. And so the Lord Jesus, after he had spoken to them, was taken up into heaven; there at the right hand of God he took his place, ',
                    '20. while they, going out, preached everywhere, the Lord working with them and confirming the word by the signs that accompanied it.'
                ]
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse_start, verse_end, list = value
            self.assertEqual(bible.mark(chapter, verse_start, verse_end), list)

    def test_luke_prints_right_verses(self):
        values = (
            (
                1, 1,
                "Seeing that many others have undertaken to draw up accounts of the events that have reached their fulfilment among us, "
            ),
            (
                11, 25,
                "But on arrival, finding it swept and tidied, "
            ),
            (
                24, 53,
                "and they were continually in the Temple praising God."
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse, text = value
            self.assertEqual(bible.luke(chapter, verse), text)

    def test_luke_prints_right_verse_list(self):
        values = (
            (
                1, 1, 2,
                [
                    '1. Seeing that many others have undertaken to draw up accounts of the events that have reached their fulfilment among us, ',
                    '2. as these were handed down to us by those who from the outset were eyewitnesses and ministers of the word, '
                ]
            ),
            (
                14, 6, 8,
                [
                    '6. And to this they could find no answer. ',
                    '7. He then told the guests a parable, because he had noticed how they picked the places of honour. He said this, ',
                    "8. 'When someone invites you to a wedding feast, do not take your seat in the place of honour. A more distinguished person than you may have been invited, "
                ]
            ),
            (
                24, 2, 3,
                [
                    '2. They found that the stone had been rolled away from the tomb, ',
                    '3. but on entering they could not find the body of the Lord Jesus. '
                ]
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse_start, verse_end, list = value
            self.assertEqual(bible.luke(chapter, verse_start, verse_end), list)

    def test_john_prints_right_verses(self):
        values = (
            (
                1, 1,
                "In the beginning was the Word: the Word was with God and the Word was God. "
            ),
            (
                10, 19,
                "These words caused a fresh division among the Jews. ",
            ),
            (
                21, 25,
                "There was much else that Jesus did; if it were written down in detail, I do not suppose the world itself would hold all the books that would be written."
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse, text = value
            self.assertEqual(bible.john(chapter, verse), text)

    def test_john_prints_right_verse_list(self):
        values = (
            (
                1, 1, 2,
                [
                    '1. In the beginning was the Word: the Word was with God and the Word was God. ',
                    '2. He was with God in the beginning. '
                ]
            ),
            (
                7, 20, 21,
                [
                    "20. The crowd replied, 'You are mad! Who wants to kill you?' ",
                    "21. Jesus answered, 'One work I did, and you are all amazed at it. "
                ]
            ),
            (
                21, 13, 14,
                [
                    '13. Jesus then stepped forward, took the bread and gave it to them, and the same with the fish. ',
                    '14. This was the third time that Jesus revealed himself to the disciples after rising from the dead. '
                ]
            )
        )

        bible = Bible()

        for value in values:
            chapter, verse_start, verse_end, list = value
            self.assertEqual(bible.john(chapter, verse_start, verse_end), list)

    def test_bible_chapter_doenst_exist_error(self):
        bible = Bible()

        with self.assertRaises(ChapterDoesntExistError):
            bible.matthew(29, 1)
            bible.mark(17, 1)
            bible.luke(25, 1)
            bible.jonh(22, 1)

    def test_bible_chapter_isnt_int_error(self):
        bible = Bible()

        with self.assertRaises(ChapterAndVerseMustBeIntError):
            bible.matthew("a", 1)
            bible.mark("a", 1)
            bible.luke("a", 1)
            bible.john("a", 1)

    def test_bible_verse_doesnt_exist_error(self):
        bible = Bible()

        with self.assertRaises(VerseDoesntExistError):
            bible.matthew(1, 100)
            bible.mark(1, 100)
            bible.luke(1, 100)
            bible.john(1, 100)

            bible.matthew(1, 1, 100)
            bible.mark(1, 1, 100)
            bible.luke(1, 1, 100)
            bible.john(1, 1, 100)

    def test_bible_verse_isnt_int_error(self):
        bible = Bible()

        with self.assertRaises(ChapterAndVerseMustBeIntError):
            bible.matthew(1, "a")
            bible.mark(1, "a")
            bible.luke(1, "a")
            bible.john(1, "a")

            bible.matthew(1, 1, "a")
            bible.mark(1, 1, "a")
            bible.luke(1, 1, "a")
            bible.john(1, 1, "a")

    def test_bible_end_verse_is_greater_than_start_verse_error(self):
        bible = Bible()

        with self.assertRaises(StartVerseGreaterThanEndOneError):
            bible.matthew(1, 2, 1)
            bible.mark(1, 2, 1)
            bible.luke(1, 2, 1)
            bible.john(1, 2, 1)

    def test_bible_end_verse_is_equal_to_start_verse_error(self):
        bible = Bible()

        with self.assertRaises(EndVerseEqualToStartOne):
            bible.matthew(1, 1, 1)
            bible.mark(1, 1, 1)
            bible.luke(1, 1, 1)
            bible.john(1, 1, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
