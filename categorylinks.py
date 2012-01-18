import re

def category_links(f):
    """Extract category links from file-like.

    Returns
    -------
    links : iterable over (str, str)
        (page_id, title) pairs.
    """
    for ln in f:
        if re.match(r"INSERT INTO `categorylinks` VALUES", ln):
            return re.findall(r"\((\d+),'([^']+)'(?:,'[^']*'){5}\)", ln)
