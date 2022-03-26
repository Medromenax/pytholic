import unittest
from pytholic.variety import sanctify, __UnholyWordError as ue, __NumberTooBigError as nb


class TestSanctify(unittest.TestCase):
    def test_string(self):
        self.assertEqual((sanctify("Hello World!")), "HELLO WORLD!")

    def test_letter_u(self):
        self.assertEqual(sanctify("u"), "V")

    def test_numbers(self):
        self.assertEqual(sanctify("5, 55, 555"), "V, LV, DLV")

    def test_full_text(self):
        self.assertEqual(
            sanctify(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum massa elit, ultrices volutpat "
                "purus consectetur, convallis commodo justo. Quisque et facilisis felis. Integer et enim eleifend, "
                "faucibus augue ac, pulvinar nunc. Maecenas vitae dui turpis. Etiam dignissim sodales purus a elementum."
                " Donec malesuada lobortis purus vitae varius. Suspendisse rutrum magna eu pretium gravida. Curabitur "
                "eu massa et diam imperdiet congue sit amet quis ex. Fusce at metus sem. Nulla facilisi. Nunc in lectus"
                " quis nisl hendrerit ullamcorper. Cras at iaculis magna, sed volutpat risus. Etiam imperdiet finibus"
                " ante quis laoreet."),
                "LOREM IPSVM DOLOR SIT AMET, CONSECTETVR ADIPISCING ELIT. VESTIBVLVM MASSA ELIT, VLTRICES VOLVTPAT"
                " PVRVS CONSECTETVR, CONVALLIS COMMODO JVSTO. QVISQVE ET FACILISIS FELIS. INTEGER ET ENIM ELEIFEND,"
                " FAVCIBVS AVGVE AC, PVLVINAR NVNC. MAECENAS VITAE DVI TVRPIS. ETIAM DIGNISSIM SODALES PVRVS A "
                "ELEMENTVM. DONEC MALESVADA LOBORTIS PVRVS VITAE VARIVS. SVSPENDISSE RVTRVM MAGNA EV PRETIVM GRAVIDA. "
                "CVRABITVR EV MASSA ET DIAM IMPERDIET CONGVE SIT AMET QVIS EX. FVSCE AT METVS SEM. NVLLA FACILISI. "
                "NVNC IN LECTVS QVIS NISL HENDRERIT VLLAMCORPER. CRAS AT IACVLIS MAGNA, SED VOLVTPAT RISVS. ETIAM "
                "IMPERDIET FINIBVS ANTE QVIS LAOREET."
            )

    def test_unholy_word_error(self):
        uw = ["satan", "baphomet", "devil", "666", "demon", "lucifer"]

        for w in uw:
            with self.assertRaises(ue):
                sanctify(w)

    def test_number_too_big_error(self):
        with self.assertRaises(nb):
            sanctify("1111111111111")

    def test_different_type(self):
        with self.assertRaises(TypeError):
            sanctify(1)