# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest


class ToLatexTest(unittest.TestCase):
    SAMPLE = (
        "My humble mentoring experience tells me something about learning "
        "programming. For complete beginners, it may be easier to learn "
        "some kind of Lisp, and then transition to Python for more “real "
        "world” code.\nOf course, various Lisps are used in production in "
        "various companies in various projects, but Python is just more "
        "popular.\n\nOne mentoree really understood object-oriented "
        "programming (OOP) only after learning it with Racket, which is "
        "usually characterized as “dialect of Scheme” (functional "
        "language).\nMaybe it has something to do with syntax not getting "
        "on beginner’s way :)")

    def setUp(self):
        from paka.cmark import LineBreaks, to_latex

        self.func = to_latex
        self.line_breaks = LineBreaks

    def check(self, source, expected, **kwargs):
        self.assertEqual(self.func(source, **kwargs), expected)

    def test_empty(self):
        self.check("", "\n")

    def test_newline(self):
        self.check("\n", "\n")

    def test_hello_world(self):
        self.check("Hello, Noob!\n", "Hello, Noob!\n")

    def test_list(self):
        expected = (
            "\\begin{itemize}\n"
            "\\item a\n\n"
            "\\item b\n\n"
            "\\end{itemize}\n")
        self.check(" * a\n * b\n", expected)

    def test_no_breaks_and_width(self):
        expected = (
            "My humble mentoring experience tells me something about "
            "learning programming. For complete beginners, it may be easier "
            "to learn some kind of Lisp, and then transition to Python for "
            "more ``real world'' code. Of course, various Lisps are "
            "used in production in various companies in various projects, "
            "but Python is just more popular.\n\n"
            "One mentoree really understood object-oriented programming "
            "(OOP) only after learning it with Racket, which is usually "
            "characterized as ``dialect of Scheme'' (functional language"
            "). Maybe it has something to do with syntax not "
            "getting on beginner's way :)\n")
        self.check(self.SAMPLE, expected)
        self.check(self.SAMPLE, expected, breaks=False)
        self.check(self.SAMPLE, expected, breaks=False, width=0)
        self.check(self.SAMPLE, expected, breaks=False, width=7)

    def test_hard_breaks_and_zero_width(self):
        expected = (
            "My humble mentoring experience tells me something about "
            "learning programming. For complete beginners, it may be easier "
            "to learn some kind of Lisp, and then transition to Python for "
            "more ``real world'' code.\\\\\n"
            "Of course, various Lisps are used in production in various "
            "companies in various projects, but Python is just more "
            "popular.\n\n"
            "One mentoree really understood object-oriented programming "
            "(OOP) only after learning it with Racket, which is usually "
            "characterized as ``dialect of Scheme'' (functional language"
            ").\\\\\n"
            "Maybe it has something to do with syntax not getting on "
            "beginner's way :)\n")
        self.check(self.SAMPLE, expected, breaks="hard")
        self.check(self.SAMPLE, expected, breaks=self.line_breaks.hard)
        self.check(
            self.SAMPLE, expected, breaks=self.line_breaks.hard, width=0)

    def test_hard_breaks_and_non_zero_width(self):
        expected = (
            "My\nhumble\nmentoring\nexperience\ntells\nme\nsomething\n"
            "about\nlearning\nprogramming.\nFor\ncomplete\nbeginners,"
            "\nit may\nbe\neasier\nto\nlearn\nsome\nkind of\nLisp,"
            "\nand\nthen\ntransition\nto\nPython\nfor\nmore\n``real\n"
            "world''\ncode.\\\\\n"
            "Of\ncourse,\nvarious\nLisps\nare\nused in\n"
            "production\nin\nvarious\ncompanies\nin\nvarious\n"
            "projects,\nbut\nPython\nis just\nmore\npopular.\n\n"
            "One\nmentoree\nreally\nunderstood\nobject-oriented\n"
            "programming\n(OOP)\nonly\nafter\nlearning\nit with"
            "\nRacket,\nwhich\nis\nusually\ncharacterized\nas\n"
            "``dialect\nof\nScheme''\n(functional\nlanguage).\\\\\n"
            "Maybe\nit has\nsomething\nto do\nwith\nsyntax\nnot"
            "\ngetting\non\nbeginner's\nway :)\n")
        width = 7
        self.check(self.SAMPLE, expected, breaks="hard", width=width)
        self.check(
            self.SAMPLE, expected, breaks=self.line_breaks.hard,
            width=width)

    def test_soft_breaks_and_zero_width(self):
        expected = (
            "My humble mentoring experience tells me something about "
            "learning programming. For complete beginners, it may be easier "
            "to learn some kind of Lisp, and then transition to Python for "
            "more ``real world'' code.\nOf course, various Lisps are "
            "used in production in various companies in various projects, "
            "but Python is just more popular.\n\n"
            "One mentoree really understood object-oriented programming "
            "(OOP) only after learning it with Racket, which is usually "
            "characterized as ``dialect of Scheme'' (functional "
            "language).\nMaybe it has something to do with syntax not "
            "getting on beginner's way :)\n")
        self.check(self.SAMPLE, expected, breaks=True)
        self.check(self.SAMPLE, expected, breaks="soft")
        self.check(self.SAMPLE, expected, breaks=self.line_breaks.soft)
        self.check(self.SAMPLE, expected, breaks=True, width=0)

    def test_soft_breaks_and_non_zero_width(self):
        expected = (
            "My\nhumble\nmentoring\nexperience\ntells\nme\nsomething\n"
            "about\nlearning\nprogramming.\nFor\ncomplete\nbeginners,"
            "\nit may\nbe\neasier\nto\nlearn\nsome\nkind of\nLisp,"
            "\nand\nthen\ntransition\nto\nPython\nfor\nmore\n``real\n"
            "world''\ncode.\nOf\ncourse,\nvarious\nLisps\nare\nused in\n"
            "production\nin\nvarious\ncompanies\nin\nvarious\n"
            "projects,\nbut\nPython\nis just\nmore\npopular.\n\n"
            "One\nmentoree\nreally\nunderstood\nobject-oriented\n"
            "programming\n(OOP)\nonly\nafter\nlearning\nit with"
            "\nRacket,\nwhich\nis\nusually\ncharacterized\nas\n"
            "``dialect\nof\nScheme\''\n(functional\nlanguage).\n"
            "Maybe\nit has\nsomething\nto do\nwith\nsyntax\nnot"
            "\ngetting\non\nbeginner's\nway :)\n")
        width = 7
        self.check(self.SAMPLE, expected, breaks=True, width=width)
        self.check(self.SAMPLE, expected, breaks="soft", width=width)
        self.check(
            self.SAMPLE, expected, breaks=self.line_breaks.soft, width=width)