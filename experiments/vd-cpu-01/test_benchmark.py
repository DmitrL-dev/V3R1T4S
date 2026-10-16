import copy
import unittest

import benchmark as b


class PrimitiveTests(unittest.TestCase):
    def setUp(self):
        self.graph = {'family': 'graph', 'object': {'n': 4, 'edges': [[0, 1], [1, 2], [2, 3]]},
                      'claim': {'vertices': 4, 'degree': 2, 'diameter': 3}}
        self.code = {'family': 'code', 'object': {'length': 4, 'words': ['1100', '0011', '1010']},
                     'claim': {'count': 3, 'weight': 2, 'distance': 2}}

    def test_known_values(self):
        for engine in ('A', 'B', 'oracle'):
            self.assertTrue(b.verify(self.graph, engine))
            self.assertTrue(b.verify(self.code, engine))
        self.assertEqual(b.graph_oracle(self.graph['object']), (4, 2, 3))
        self.assertEqual(b.code_oracle(self.code['object']), (3, [2, 2, 2], 2))

    def test_invalid_formats(self):
        invalid = [None, {}, [], {'family': 'other', 'object': {}, 'claim': {}}]
        for base, field, value in [(self.graph, 'n', True), (self.graph, 'edges', [[0, 0]]),
                                   (self.graph, 'edges', [[1, 0]]), (self.graph, 'edges', [[0, 1], [0, 1]]),
                                   (self.graph, 'edges', [[0, 4]]), (self.code, 'words', ['1100', '1100']),
                                   (self.code, 'words', ['xxxx', '0000']), (self.code, 'words', ['1100']),
                                   (self.code, 'length', True)]:
            c = copy.deepcopy(base)
            c['object'][field] = value
            invalid.append(c)
        for base in (self.graph, self.code):
            for target in ('claim', 'object'):
                c = copy.deepcopy(base)
                c[target]['extra'] = 1
                invalid.append(c)
            c = copy.deepcopy(base)
            c['claim'][next(iter(c['claim']))] = False
            invalid.append(c)
        for c in invalid:
            for engine in ('A', 'B', 'oracle'):
                self.assertFalse(b.verify(c, engine), (c, engine))

    def test_disconnected(self):
        self.graph['object']['edges'] = [[0, 1], [2, 3]]
        for engine in ('A', 'B', 'oracle'):
            self.assertFalse(b.verify(self.graph, engine))

    def test_nonconstant_weight_rejected(self):
        self.code['object']['words'][0] = '1000'
        for engine in ('A', 'B', 'oracle'):
            self.assertFalse(b.verify(self.code, engine))

    def test_canonical_equivalence(self):
        other = {'n': 4, 'edges': [[0, 2], [0, 3], [1, 3]]}
        self.assertEqual(b.canonical_graph(self.graph['object']), b.canonical_graph(other))
        other_code = {'length': 4, 'words': [w[::-1] for w in self.code['object']['words'][::-1]]}
        self.assertEqual(b.canonical_code(self.code['object']), b.canonical_code(other_code))

    def test_confusion_labels(self):
        # One manually supplied case, independent of the generated regression data.
        case = {'id': 'code-test/true', 'base': 'code-test', 'split': 'development',
                'variant': 'true', 'expected': True, 'input': self.code}
        summary = b.summarize(b.evaluate([case]))
        self.assertEqual(summary['code/all/always_fail']['A_confusion']['FN'], 1)
        self.assertEqual(summary['code/all/always_pass']['A_confusion']['TP'], 1)


if __name__ == '__main__':
    unittest.main()
