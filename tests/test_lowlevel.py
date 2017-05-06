# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import textwrap
import unittest


class IterationWithReplacementTest(unittest.TestCase):
    SAMPLE = textwrap.dedent("""\
        Проверяем *CommonMark*.

        Вставляем `код`.
        И [другие](https://example.org) штуки.

        <p>Test of <em>HTML</em>.</p>

        ```pycon
        Python 3.5.0 (default)
        [GCC] on linux
        Type "help" for more information.
        >>> a = 1
        >>> b = 3
        >>> a, b = b, a
        >>> print(a, b)
        3 1
        ```

        Можно ещё здесь что-нибудь написать.

        ```haskell
        Here is a candidate for reduction:

        > add :: Integer -> Integer -> Integer
        > add x y = (+) x y  -- xD
        ```
        """)
    NEW_CODE_BLOCK_TEMPLATE = (
        "<pre><code class=\"language-{}\"><b>It was:</b>\n"
        "&lt;|{}|&gt;\n</code></pre>")
    EXPECTED = textwrap.dedent("""\
        <p>Проверяем <em>CommonMark</em>.</p>
        <p>Вставляем <code>код</code>.
        И <a href="https://example.org">другие</a> штуки.</p>
        <p>Test of <em>HTML</em>.</p>
        <pre><code class="language-pycon"><b>It was:</b>
        &lt;|Python 3.5.0 (default)
        [GCC] on linux
        Type "help" for more information.
        >>> a = 1
        >>> b = 3
        >>> a, b = b, a
        >>> print(a, b)
        3 1
        |&gt;
        </code></pre>
        <p>Можно ещё здесь что-нибудь написать.</p>
        <pre><code class="language-haskell"><b>It was:</b>
        &lt;|Here is a candidate for reduction:

        > add :: Integer -> Integer -> Integer
        > add x y = (+) x y  -- xD
        |&gt;
        </code></pre>
        """)

    def setUp(self):
        from paka.cmark import lowlevel

        self.mod = lowlevel

    def _substitute_code_block_node(self, old_node):
        contents = self.mod.text_to_c(
            self.NEW_CODE_BLOCK_TEMPLATE.format(
                self.mod.text_from_c(self.mod.node_get_fence_info(old_node)),
                self.mod.text_from_c(self.mod.node_get_literal(old_node))))
        new_node = self.mod.node_new(self.mod.NODE_HTML_BLOCK)
        assert self.mod.node_set_literal(new_node, contents) == 1
        assert self.mod.node_replace(old_node, new_node) == 1
        self.mod.node_free(old_node)

    def _substitute_code_blocks(self, root):
        iter_ = self.mod.iter_new(root)
        try:
            while True:
                ev_type = self.mod.iter_next(iter_)
                if ev_type == self.mod.EVENT_DONE:
                    break
                elif ev_type == self.mod.EVENT_ENTER:
                    node = self.mod.iter_get_node(iter_)
                    node_type = self.mod.node_get_type(node)
                    if node_type == self.mod.NODE_CODE_BLOCK:
                        self._substitute_code_block_node(node)
        finally:
            self.mod.iter_free(iter_)

    def runTest(self):
        text_bytes = self.mod.text_to_c(self.SAMPLE)
        root = self.mod.parse_document(
            text_bytes, len(text_bytes), self.mod.OPT_DEFAULT)
        try:
            self._substitute_code_blocks(root)
            result = self.mod.text_from_c(
                self.mod.render_html(root, self.mod.OPT_DEFAULT))
        finally:
            self.mod.node_free(root)
        self.assertEqual(result, self.EXPECTED)