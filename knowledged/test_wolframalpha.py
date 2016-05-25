import unittest
from jasper import testutils, diagnose
from . import knowledged


class TestWolframAlphaPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = testutils.get_plugin_instance(
            knowledged.WolframAlphaPlugin)

    def test_is_valid(self):
        self.assertTrue(self.plugin.is_valid(
            "Who is George Washington?"))
        self.assertTrue(self.plugin.is_valid(
            "How old is Eminem?"))
        self.assertTrue(self.plugin.is_valid(
            "How many cups are in a gallon?"))
        self.assertTrue(self.plugin.is_valid(
            "What is pi?"))
        self.assertTrue(self.plugin.is_valid(
            "How much money does Bill Gates have?"))
        self.assertFalse(self.plugin.is_valid(
            "Tell me a joke."))

    def test_handle_method(self):
        mic = testutils.TestMic()
        self.plugin.handle(
            "Who is George Washington?", mic)
        self.assertTrue(len(mic.outputs) > 0)
        self.assertFalse("I can not find anything" in mic.outputs)
        self.assertFalse("Sorry, Could you be more specific?" in mic.outputs)
