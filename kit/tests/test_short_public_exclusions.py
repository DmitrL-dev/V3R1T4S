# SPDX-License-Identifier: AGPL-3.0-or-later
import os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
from test_check_run import Base, w

class ShortPublicExclusions(Base):
    def exercise(self, token, public_documents):
        self.attack()
        w(os.path.join(self.W,'private','toy-cipher','public_excerpt.txt'), token)
        for i, text in enumerate(public_documents):
            w(os.path.join(self.R,'data','public%d.txt' % i), text)
        w(os.path.join(self.W,'REPORT.md'), '# Report\nPublished excerpt: '+token+'\n')
        return self.run_check(self.W, '--no-exec')

    def test_public_short_excerpts_are_excluded(self):
        for n in range(8, 16):
            with self.subTest(length=n):
                token='ABCDEFGHJKLMNPQRSTUVWXYZ'[:n]
                self.assertEqual(self.exercise(token, ['Published '+token+' ending']),0,self.out)

    def test_public_short_document_is_excluded(self):
        self.assertEqual(self.exercise('ABCDEFGH', ['ABCDEFGH']),0,self.out)

    def test_public_normalized_text_is_excluded(self):
        self.assertEqual(self.exercise('ABCDEFGH', ['ab cd-ef gh']),0,self.out)

    def test_unpublished_short_excerpt_is_still_detected(self):
        self.assertEqual(self.exercise('ABCDEFGH', ['Unrelated public text']),1,self.out)
        self.assertIn('commit-only secrets stay in private', self.out)

    def test_separate_public_documents_are_not_concatenated(self):
        self.assertEqual(self.exercise('ABCDEFGH', ['ABCD','EFGH']),1,self.out)

    def test_public_long_window_controls(self):
        for length in (16, 20):
            with self.subTest(length=length):
                token = 'ABCDEFGHJKLMNPQRSTUVWXYZ'[:length]
                self.assertEqual(self.exercise(token, [token]), 0, self.out)

    def test_unpublished_long_excerpt_is_still_detected(self):
        token = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        self.assertEqual(self.exercise(token, ['Unrelated public text']), 1, self.out)
        self.assertIn('commit-only secrets stay in private', self.out)

if __name__=='__main__': unittest.main(verbosity=2)
