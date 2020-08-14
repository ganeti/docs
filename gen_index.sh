#!/bin/bash
PYTHONPATH=docs.ganeti.org sphinx-build -b html -W docs.ganeti.org/ ./

# github pages has no directory index, create one here
for v in docs/ganeti/*; do
  if [[ -d "${v}/man/" ]]; then
    tree -H '.' -L 1 --noreport --charset utf-8 -T "Ganeti ${v##docs/ganeti/} Manpages" -I index.html -o ${v}/man/index.html -- ${v}/man/
  fi
done
