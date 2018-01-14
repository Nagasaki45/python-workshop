def author_summary(name):
    # Write your code here
    with open('data/references.bib') as f:
        content = f.read()
    histogram = {}
    items = content.split('@')
    for item in items:
        lines = item.split('\n')
        item_by_author = False
        for line in lines:
            if 'author' in line.lower() and name.lower() in line.lower():
                item_by_author = True
                break
        if item_by_author:
            for line in lines:
                if 'year' in line.lower():
                    year = int(line.split('"')[1])
                    histogram[year] = histogram.get(year, 0) + 1
                    break
    return histogram


assert author_summary('Bailenson') == {2002: 2, 2003: 1, 2004: 1, 2005: 1, 2006: 2,
                                       2007: 2, 2008: 4, 2009: 1, 2014: 2}
assert author_summary('Morency') == {2006: 1, 2008: 1, 2009: 1, 2011: 1}
assert author_summary('de Kok') == {2008: 1, 2011: 1, 2012: 1}
