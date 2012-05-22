from lxml import etree

_NS = {"w": "http://www.mediawiki.org/xml/export-0.6/"}
_PAGE_TAG = "{%s}page" % _NS["w"]


def _xpath(et, expr):
    return et.xpath(expr, namespaces=_NS)


def extract_pages(f):
    """Extract pages from Wikimedia database dump.

    Returns
    -------
    pages : iterable over (int, str, str)
        Generates (page_id, title, content) triples.
    """
    for event, elem in etree.iterparse(f, events=["end"]):
        if elem.tag == _PAGE_TAG:
            text = _xpath(elem, "string(./w:revision/w:text)")
            yield (int(_xpath(elem, "string(./w:id)")),
                   _xpath(elem, "string(./w:title)"),
                   text)

            # http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
            # We do this only for <page>s, since we need to inspect the
            # ./revision/text element. That shouldn't matter since the pages
            # comprise the bulk of the file.
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]


if __name__ == "__main__":
    import sys

    for pageid, title, text in extract_pages(sys.stdin):
        print("%d '%s' (%s)" % (pageid, title, text[:40].replace("\n", "_")))
