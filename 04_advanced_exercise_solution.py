wittgensteins_book = '''
@book{wittgenstein2010philosophical,
  title="Philosophical investigations",
  author="Wittgenstein, Ludwig",
  year="2010",
  publisher="John Wiley \& Sons"
}
'''.strip()

einsteins_paper = '''
@article{einstein1935can,
  title="Can quantum-mechanical description of physical reality be considered complete?",
  author="Einstein, Albert and Podolsky, Boris and Rosen, Nathan",
  journal="Physical review",
  volume="47",
  number="10",
  pages="777",
  year="1935",
  publisher="APS"
}
'''.strip()


# Hints: split by lines and iterate. Find the 'author' line
# and return whatever between the first double quote and the
# first comma.
def item_author(item):
    # --- WRITE YOUR CODE HERE --- #
    for line in item.split('\n'):
        if 'author' in line.lower():
            authors = line.split('"')[1]
            first_author_surname = authors.split(',')[0]
            return first_author_surname
    return False
    # ---------------------------- #


assert item_author(wittgensteins_book) == 'Wittgenstein'
assert item_author(einsteins_paper) == 'Einstein'


def item_year(item):
    # --- WRITE YOUR CODE HERE --- #
    for line in item.split('\n'):
        if 'year' in line.lower():
            return int(line.split('"')[1])
    # ---------------------------- #


assert item_year(wittgensteins_book) == 2010
assert item_year(einsteins_paper) == 1935


# Hints: read the content, assume that you can split items by @.
# Use the counter from the discussion about dictionaries to create
# the histogram.
def author_summary(name):
    histogram = {}

    # --- WRITE YOUR CODE HERE --- #
    with open('data/references.bib') as f:
        content = f.read()
    items = content.split('@')
    for item in items:
        if item_author(item) == name:
            year = item_year(item)
            histogram[year] = histogram.get(year, 0) + 1
    # ---------------------------- #

    return histogram


assert author_summary('Bailenson') == {2002: 1, 2004: 1, 2005: 1, 2006: 2, 2008: 3}
assert author_summary('Morency') == {2008: 1, 2009: 1}
assert author_summary('Gratch') == {2006: 1, 2007: 1}
