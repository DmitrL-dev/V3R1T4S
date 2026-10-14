# SPDX-License-Identifier: AGPL-3.0-or-later
"""Synthetic regressions: execute our scanner only, never submission code."""
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest

CHECKER = Path(os.environ.get('CHECK_RUN_UNDER_TEST', str(Path(__file__).parents[1] / 'check_run.py')))
spec = importlib.util.spec_from_file_location('checker_under_test', CHECKER)
check_run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_run)


class CppPlaceholders(unittest.TestCase):
    def scan(self, text, path='object/code.cpp', **kwargs):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
            c = check_run.Checker(quiet=True)
            check_run.leak_scan(c, tmp, 'synthetic', **kwargs)
            return c.fails

    def test_real_standard_operands(self):
        for path in ('object/code.cpp', 'object/code.hpp', 'object/code.h', '.hidden.cpp', '.private/code.hpp'):
            for source in ('#include <unordered_map>\n', '#include <unordered_set>\n',
                           '\ufeff#include <unordered_map>\n',
                           '  # include <type_traits>\r\n',
                           '#/**/include /* spacing */ <unordered_map> // harmless\n',
                           "auto n = 1'000;\n#include <unordered_map>\n"):
                with self.subTest(path=path, source=source):
                    self.assertEqual([], self.scan(source, path))

    def test_comments_and_literals_remain_scanned(self):
        sources = [
            '// #include <unordered_map>\n',
            '/*\n#include <unordered_map>\n*/\n',
            'auto s = "#include <unordered_map>";\n',
            'auto s = R"raw(\n#include <unordered_map>\n)raw";\n',
            '\ufeffR"raw("\n#include <unordered_map>\n)raw";\n',
            'auto s = R"raw("\n#include <unordered_map>\n',
            "auto c = '#include <unordered_map>';\n",
            '/* unterminated\n#include <unordered_map>\n',
            '"unterminated\n#include <unordered_map>\n',
            '// continued\\\n#include <unordered_map>\n',
            '// continued\\ \n#include <unordered_map>\n',
            '// continued\\\t\n#include <unordered_map>\n',
            '/\\\n/ hidden\n#include <unordered_map>\n',
            '// continued??/\n#include <unordered_map>\n',
            'auto s = ""_R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'auto s = ""_u8R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'auto s = ""R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'auto s = nameR"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'auto s = x\u0301R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'auto s = ""_\u0301R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            "1'//\n#include <unordered_map>\n'",
            '/\\\r*\n#include <unordered_map>\n*/\n',
            "#define UNUSED 1é'0 /* '\n#include <unordered_map>\n*/\n",
            "#define UNUSED 1\\u00e9'0 /* '\n#include <unordered_map>\n*/\n",
            "#define UNUSED 1\\N{LATIN SMALL LETTER E WITH ACUTE}'0 /* '\n#include <unordered_map>\n*/\n",
            'name\\u{0301}R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
            'name\\N{COMBINING ACUTE ACCENT}R"del(";\n/*\n)del"\n#include <unordered_map>\n*/\n',
        ]
        for source in sources:
            with self.subTest(source=source):
                self.assertTrue(any('unfilled placeholder' in f for f in self.scan(source)))

    def test_only_operand_exempt(self):
        for source in (
            '#include <unordered_map> // <tag>\n',
            '#include <unordered_map> /* <path> */\n',
            '#include <unordered_map>\nconst char *x = "<name>";\n',
            '/* <value> */ #include <unordered_map>\n',
            '#include <unordered_map>\n// <unordered_map>\n',
            '#include <project_header>\n',
            '#include <tag>\n',
            '#include <unordered_map> <unordered_set>\n',
            '# "ignored" include <unordered_map>\n',
            '#include <unordered_map> "ignored"\n',
            '#include <unordered_map> 123\n',
        ):
            with self.subTest(source=source):
                self.assertTrue(any('unfilled placeholder' in f for f in self.scan(source)))

    def test_unknown_and_hidden_suffixes_stay_scanned(self):
        for path in ('README.md', '.hidden', '.private/payload.custom', 'object/code.c', 'object/code.cc'):
            with self.subTest(path=path):
                self.assertTrue(any('unfilled placeholder' in f for f in self.scan('#include <unordered_map>\n', path)))

    def test_hidden_placeholders_beside_valid_include(self):
        for path in ('.hidden.cpp', '.private/code.hpp'):
            self.assertTrue(any('unfilled placeholder <tag>' in f for f in self.scan('#include <unordered_map> // <tag>\n', path)))

    def test_leak_scan_uses_unmodified_text(self):
        source = '#include <unordered_map> // /' + 'home/alice/private\n'
        self.assertTrue(any('absolute Linux home path' in f for f in self.scan(source)))
        self.assertTrue(any('never_publish' in f for f in self.scan('#include <unordered_map>\n', never_publish=('unordered_map',))))

    def test_translation_edge_cases_fail_closed(self):
        for source in ('#include <unordered_map>\n#define X \\\n 1\n',
                       '#include <unordered_map>\n// ??/\n'):
            self.assertTrue(any('unfilled placeholder' in f for f in self.scan(source)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
