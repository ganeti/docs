#!/bin/bash
PYTHONPATH=docs.ganeti.org sphinx-build -b html -W docs.ganeti.org/ ./

# github pages has no directory index, create one here
version=$(grep 'Stable' docs.ganeti.org/index.rst | cut -d '|' -f 3 | tr -d '* ')
cd docs/ganeti/${version}/man
tree -H '' -L 1 --noreport --charset utf-8 -T "Ganeti ${version} Manpages" -I index.html -o index.html -- ./
cd -
