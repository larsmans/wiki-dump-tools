# -*- coding: utf-8 -*-

import re

# Media and categories; the codes for these differ per language.
# We have the most popular ones (>900.000 articles as of July 2012) here,
# as well as Latin, which is useful for testing.
# Add other languages as required.
_MEDIA_CAT = """
  [Ii]mage|[Cc]ategory      # English
 |[Aa]rchivo                # Spanish
 |[Ff]ile                   # English, Italian
 |[CcKk]at[ée]gor[íi][ea]   # Dutch, German, French, Italian, Spanish, Polish, Latin
 |[Bb]estand                # Dutch
 |[Bb]ild                   # German
 |[Ff]icher                 # French
 |[Pp]lik                   # Polish
 |[Ff]asciculus             # Latin
"""

_UNWANTED = re.compile(r"""
  (:?
    \{\{ .*? \}\}                           # templates
  | \| .*? \n                               # left behind from templates
  | \}\}                                    # left behind from templates
  | <!-- .*? -->
  | <div .*?> .*? </div>
  | <math> .*? </math>
  | <nowiki> .*? </nowiki>
  | <ref .*?> .*? </ref>
  | <ref .*?/>
  | <span .*?> .*? </span>
  | \[\[ (:?%s): (\[\[.*?\]\]|.)*? \]\]
  | \[\[ [a-z]{2,}:.*? \]\]                 # interwiki links
  | =+                                      # headers
  | \{\| .*? \|\}
  | \[\[ (:? [^]]+ \|)?
  | \]\]
  | '{2,}
  )
""" % _MEDIA_CAT,
re.DOTALL | re.MULTILINE | re.VERBOSE)


def text_only(text):
    return _UNWANTED.sub("", text)


if __name__ == "__main__":
    import sys

    print(text_only(sys.stdin.read()))
