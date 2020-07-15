Website docs.ganeti.org
=======================

This website is served by github pages using the root directory (master branch only). It contains a table listing all versions of Ganeti documentation so far (see `docs.ganeti.org/index.rst`). To transform this into HTML, run `gen_index.sh`.

All other content must be retrieved (copied) from configured and compiled Ganeti source:

* `docs/ganeti/<version>/html` from `configure --enable-manpages-in-doc` out of `doc/man-html/`
* `docs/ganeti/<version>/man` from `man/*.html`
* `docs/ganeti/<version>/api/py` from `doc/api/py`
* `docs/ganeti/<version>/api/hs` from `doc/api/hs`
