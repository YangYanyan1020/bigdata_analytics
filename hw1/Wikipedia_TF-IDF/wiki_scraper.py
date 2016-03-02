from goose import Goose

def get_wiki_pages():
    g = Goose()
    base_url = 'https://en.wikipedia.org/wiki/List_of_NP-complete_problems'
    base_article = g.extract(url=base_url)

    # filter and clean links, now we only have links to problems
    links = filter(lambda s: ('/wiki/' in s) and (':' not in s), base_article.links)
    upto_idx = links.index('/wiki/Karp%27s_21_NP-complete_problems')
    links = links[:upto_idx]

    for link in links:
        url = 'https://en.wikipedia.org' + link
        print link[6:]
        article = g.extract(url=url)

        filename = 'wiki-pages/' + link[6:]
        f = open(filename, 'w')
        f.write(article.cleaned_text.encode('ascii', 'ignore'))
        f.close()

if __name__ == '__main__':
    get_wiki_pages()
