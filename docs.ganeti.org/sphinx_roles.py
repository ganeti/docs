"""Sphinx extension for Ganeti documentation overview.

"""
import re
from docutils.parsers.rst.roles import set_classes
from docutils import nodes

# Regular expression for role types in doc overview
_OVW_RE = re.compile(r"^(?P<text>\w+)\s+<(?P<version>[\w\.]+)>$")

def _GenericRole(role, rawtext, text, lineno, inliner, options={}, content=[]):
  try: 
    m = _OVW_RE.match(text)
    if not m:
      raise ValueError
  except ValueError:
    msg= inliner.reporter.error("reference '%s' does not match regular"
                                " expression '%s'" % (text, _OVW_RE.pattern))
    prb = inliner.problematic(rawtext, rawtext, msg)
    return [prb], [msg]

  linktext = m.group("text")
  version = m.group("version")
  # pint to the path belonging to role
  if role == 'gdoc':
    ref = 'docs/ganeti/' + version + '/html/index.html'
  elif role == 'hapi':
    ref = 'docs/ganeti/' + version + '/api/hs/index.html'
  elif role == 'papi':
    ref = 'docs/ganeti/' + version + '/api/py/index.html'
  elif role == 'man':
    ref = 'docs/ganeti/' + version + '/man/index.html'
  elif role == 'api':
    ref = 'docs/ganeti/' + version + '/api/index.html'
  else:
    ref = 'nonexistent'
  set_classes(options)
  node = nodes.reference(rawtext, linktext, refuri=ref,
                         **options)
  return [node], []

def setup(app):
  """Sphinx extension callback.

  """
  app.add_role("gdoc", _GenericRole)
  app.add_role("hapi", _GenericRole)
  app.add_role("papi", _GenericRole)
  app.add_role("man",  _GenericRole)
  app.add_role("api",  _GenericRole)
