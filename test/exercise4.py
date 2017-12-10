import unittest
from adventofcode_2017.exercise4 import check_passphrase, check_passphrase_v2


class TestExercise(unittest.TestCase):
    PassPhraseData = {
        "aa bb cc dd ee": True,
        "aa bb cc dd aa": False,
        "aa bb cc dd aaa": True,
        "hlo mmv vmm mvm": True,
    }

    PassPhraseV2Data = {
        "abcde fghij": True,
        "abcde xyz ecdab": False,
        "a ab abc abd abf abj": True,
        "iiii oiii ooii oooi oooo": True,
        "oiii ioii iioi iiio": False
    }

    def test_check_passphrase(self):
        for key, value in self.PassPhraseData.items():
            result = check_passphrase(key)
            self.assertEqual(value, result, "Passphrase: {0}".format(key))

    def test_check_passphrase_v2(self):
        for key, value in self.PassPhraseV2Data.items():
            result = check_passphrase_v2(key)
            self.assertEqual(value, result, "Passphrase V2: {0}".format(key))
