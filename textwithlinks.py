import re

_UNWANTED = re.compile(r"""
  (:?
    # this one may leave some stuff behind...
    \{\{ .*? \}\}
  | <math> .*? </math>
  | <ref> .*? </ref>
  | \[\[ (:?Bestand|Categorie): (\[\[.*?\]\]|.)*? \]\]
  | \[\[ [a-z]{2,}:.*? \]\]                 # interwiki links
  | =+ .*? =+                               # headers
  | ''+
  )
""", re.DOTALL | re.MULTILINE | re.VERBOSE)


def text_with_links(text):
    return re.sub(_UNWANTED, "", text)


if __name__ == "__main__":
    import sys

    print(text_with_links(sys.stdin.read()))
