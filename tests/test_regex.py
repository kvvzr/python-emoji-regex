# -*- coding: utf-8 -*-

from emoji_regex import emoji_regex
import unittest
import sys

class TestEmojiRegex(unittest.TestCase):

    def test_emoji_regex(self):
        emoji_re = emoji_regex.compile()
        if sys.version_info >= (3, 0):
            self.assertEqual(None, emoji_re.search('普通の文章'))
            self.assertNotEqual(None, emoji_re.search('⌚'))
            self.assertNotEqual(None, emoji_re.search('🧀'))
            self.assertNotEqual(None, emoji_re.search('🇯🇵'))
        else:
            self.assertEqual(None, emoji_re.search(u'普通の文章'))
            self.assertNotEqual(None, emoji_re.search(u'⌚'))
            self.assertNotEqual(None, emoji_re.search(u'🧀'))
            self.assertNotEqual(None, emoji_re.search(u'🇯🇵'))

if __name__ == '__main__':
    unittest.main()
