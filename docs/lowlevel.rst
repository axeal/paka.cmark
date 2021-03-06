Low-level API
=============

.. currentmodule:: paka.cmark.lowlevel

.. automodule:: paka.cmark.lowlevel
  :no-members:
  :no-undoc-members:

.. autofunction:: version_string

.. autofunction:: parse_document
.. autofunction:: node_new
.. autofunction:: node_free
.. autofunction:: node_get_type
.. autofunction:: node_get_type_string
.. autofunction:: node_get_fence_info
.. autofunction:: node_get_literal
.. autofunction:: node_set_literal
.. autofunction:: node_get_heading_level
.. autofunction:: node_set_heading_level
.. autofunction:: node_get_list_type
.. autofunction:: node_set_list_type
.. autofunction:: node_get_list_delim
.. autofunction:: node_set_list_delim
.. autofunction:: node_get_list_start
.. autofunction:: node_set_list_start
.. autofunction:: node_get_list_tight
.. autofunction:: node_set_list_tight
.. autofunction:: node_get_url
.. autofunction:: node_set_url
.. autofunction:: node_get_title
.. autofunction:: node_set_title
.. autofunction:: node_get_start_line
.. autofunction:: node_get_start_column
.. autofunction:: node_get_end_line
.. autofunction:: node_get_end_column

Parsing (streaming API)
-----------------------
.. autofunction:: parser_new
.. autofunction:: parser_free
.. autofunction:: parser_feed
.. autofunction:: parser_finish

Tree traversal
--------------
.. autofunction:: node_next
.. autofunction:: node_previous
.. autofunction:: node_parent
.. autofunction:: node_first_child
.. autofunction:: node_last_child

Tree manipulation
-----------------
.. autofunction:: node_unlink
.. autofunction:: node_insert_before
.. autofunction:: node_insert_after
.. autofunction:: node_replace
.. autofunction:: node_prepend_child
.. autofunction:: node_append_child
.. autofunction:: consolidate_text_nodes

Iteration
---------
.. autofunction:: iter_new
.. autofunction:: iter_free
.. autofunction:: iter_next
.. autofunction:: iter_get_node
.. autofunction:: iter_get_event_type
.. autofunction:: iter_get_root
.. autofunction:: iter_reset

.. _iteration_event_types:

Iteration event types
---------------------
.. autodata:: EVENT_ENTER
.. autodata:: EVENT_EXIT
.. autodata:: EVENT_DONE

Rendering
---------
.. autofunction:: markdown_to_html
.. autofunction:: render_html
.. autofunction:: render_xml
.. autofunction:: render_man
.. autofunction:: render_commonmark
.. autofunction:: render_latex

.. _options:

Options
-------
.. autodata:: OPT_DEFAULT
.. autodata:: OPT_HARDBREAKS
.. autodata:: OPT_NOBREAKS
.. autodata:: OPT_SOURCEPOS
.. autodata:: OPT_UNSAFE
.. autodata:: OPT_SMART

.. _node_types:

Node types
----------
.. autodata:: NODE_NONE
.. autodata:: NODE_CODE_BLOCK
.. autodata:: NODE_HTML_BLOCK
.. autodata:: NODE_DOCUMENT
.. autodata:: NODE_BLOCK_QUOTE
.. autodata:: NODE_LIST
.. autodata:: NODE_ITEM
.. autodata:: NODE_CUSTOM_BLOCK
.. autodata:: NODE_PARAGRAPH
.. autodata:: NODE_HEADING
.. autodata:: NODE_THEMATIC_BREAK
.. autodata:: NODE_FIRST_BLOCK
.. autodata:: NODE_LAST_BLOCK
.. autodata:: NODE_TEXT
.. autodata:: NODE_SOFTBREAK
.. autodata:: NODE_LINEBREAK
.. autodata:: NODE_CODE
.. autodata:: NODE_HTML_INLINE
.. autodata:: NODE_CUSTOM_INLINE
.. autodata:: NODE_EMPH
.. autodata:: NODE_STRONG
.. autodata:: NODE_LINK
.. autodata:: NODE_IMAGE
.. autodata:: NODE_FIRST_INLINE
.. autodata:: NODE_LAST_INLINE

.. _list_types:

List types
----------
.. autodata:: BULLET_LIST
.. autodata:: ORDERED_LIST
.. autodata:: NO_LIST

.. _list_delimiters:

List delimiters
---------------
.. autodata:: PERIOD_DELIM
.. autodata:: PAREN_DELIM
.. autodata:: NO_DELIM

Python Helpers
--------------
.. autofunction:: text_to_c
.. autofunction:: text_from_c
