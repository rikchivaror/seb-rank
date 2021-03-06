# TODO: insert a detailed project description here

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>

""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>

""",
}


# -----------------------------------------------------------------------------
# quicksort(p):
#   Quicksort provides a way to sort any list of data, using an expected
#   number of comparisons that scales as n log n where n is the number of elements
#   in the list.
#
#   The idea of quicksort is quite simple: if the list has zero or one elements,
#       it is already sorted.
#
#   Otherwise, pick a pivot element, and split the list into two partitions: one
#   contains all the elements equal to or lower than the value of the pivot
#   element, and the other contains all the elements that are greater than the
#   pivot element. Recursively sort each of the sub-lists, and then return the
#   result of concatenating the sorted left sub-list, the pivot element, and the
#   sorted right sub-list.
#
# Arguments:
#   p: An unsorted list of the form [[<item>, <value>], ... ] where <value>
#       is a real number belonging to the set {0 to 1} and '<item>' is any object
#       associated with that value.
#
# Return:
#   A sorted list of the form [[<item>, <value>], ... ] were each [<item>,
#   <value>] element is sorted according to <value>, decreasing from left to right.
def quicksort(p):

    if len(p) == 1:
        return [p[0][0]]
    elif len(p) == 0:
        return []

    first_half, second_half = [], []
    pivot = p[0]                    # first list element is the pivot

    for e in p[1:]:                 # compare <value> of each element to pivot's value
        if e[1] <= pivot[1]:
            second_half.append(e)   # place element in the second list if value is
        else:                       # greater than the pivot otherwise place the
            first_half.append(e)    # element in the first list

    return quicksort(first_half) + [pivot[0]] + quicksort(second_half)


# -----------------------------------------------------------------------------
# ordered_search(index, ranks, keyword):
#   The procedure takes takes as input an index, a ranks dictionary (the result
#   of compute_ranks), and a keyword, and returns an ordered list of all the URLs
#   that match the query. The Quicksort algorithm is used to perform list ordering.
#
# Arguments:
#   index: [[<keyword>,[<url>,...]],...]
#   ranks: the result of compute_ranks {<url>: <rank>, ...}
#   keyword: String
#
# Returns:
#   sorted_results: an ordered list of all the URLs that match the query
def ordered_search(index, ranks, keyword):

    results = lookup(index, keyword)
    ranked_results = []   # [[<url>, <rank>] ... ]

    if not results:
        return None

    for e in results:
        ranked_results.append([e, ranks[e]])

    sorted_results = quicksort(ranked_results)

    return sorted_results


# -----------------------------------------------------------------------------
# get_page(url):
#   Get the HTML for an URL, possibly from an in-memory cache.
#
# Arguments:
#   url: URL string
#
# Returns:
#   HTML referenced by URL, as a String type
def get_page(url):

    if url in cache:
        return cache[url]
    return ""

    # try:
    #     import urllib.request
    #     return str(urllib.request.urlopen(url).read())
    # except:
    #     return ""


# -----------------------------------------------------------------------------
# get_next_target(page):
#   Get the HTML for an URL, possibly from an in-memory cache.
#
# Arguments:
#   page: a long String containing HTML code
#
# Returns:
#   url: a String of the first URL found in 'page'
#   end_quote: index position of "url's" end quote
def get_next_target(page):

    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


# TODO: comment get_all_links procedure
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


# TODO: comment union procedure
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)


# TODO: comment add_page_to_index procedure
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


# TODO: comment add_to_index procedure
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]


# TODO: comment lookup procedure
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


# TODO: comment crawl_web procedure
def crawl_web(seed):    # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}          # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


# TODO: comment recipr_links procedure
# -----------------------------------------------------------------------------
# One of the problems with our page ranking system is pages can
# collude with each other to improve their page ranks.  We consider
# A->B a reciprocal link if there is a link path from B to A of length
# equal to or below the collusion level, k.  The length of a link path
# is the number of links which are taken to travel from one page to the
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A,
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link
# A->B, which includes one link and so is of length 1. (it requires
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to
#   - take an extra input k, which is a non-negative integer, and
#   - exclude reciprocal links of length up to and including k from
#     helping the page rank.
def recipr_links(graph, hops, base_node, curr_node=None):

    if hops == -1:
        return []

    loopbacks = []
    if not curr_node:
        curr_node = base_node
    child_nodes = graph[curr_node]

    for node in child_nodes:
        if base_node == node:
            loopbacks.append([curr_node, node])
        else:
            new_links = recipr_links(graph, hops-1, base_node, node)
            for link in new_links:
                if link not in loopbacks:
                    loopbacks.append(link)

    return loopbacks


# TODO: comment find_colluders procedure
def find_colluders(graph, k):

    colluders = []

    for node in graph:
        links = recipr_links(graph, k, node)
        for link in links:
            colluders.append(link)

    return colluders


# TODO: finish commenting computer_ranks procedure
# -----------------------------------------------------------------------------
# compute_ranks(graph, k):
#   This is the page ranking algorithm. It determines the popularity of a page
#   within a graph based on on the inlink relationship between URLs.
#
# Arguments:
#   graph:
#   k:
#
# Return:
#   ranks: {'<url>': <rank>, ...}
def compute_ranks(graph, k):

    d = 0.8     # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    colluding = find_colluders(graph, k)

    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if [node, page] not in colluding:
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# Here are some example showing what ordered_search should do:

# Observe that the result list is sorted so the highest-ranking site is at the
# beginning of the list.

# Note: the intent of this question is for students to write their own sorting
# code, not to use the built-in sort procedure.
def test():

    # test_list = [[9, 0.96], [2, 0.35], [7, 0.77], [6, 0.70], [4, 0.61],
    #              [5, 0.69], [3, 0.45], [1, 0.15], [10, 1.00], [8, 0.88]]
    #
    # print(quicksort(test_list))

    index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    ranks = compute_ranks(graph,2)

    print(ranks)
    print(ordered_search(index, ranks, 'Hummus'))

    # >>> ['http://udacity.com/cs101x/urank/kathleen.html',
    #    'http://udacity.com/cs101x/urank/nickel.html',
    #    'http://udacity.com/cs101x/urank/arsenic.html',
    #    'http://udacity.com/cs101x/urank/hummus.html',
    #    'http://udacity.com/cs101x/urank/index.html']

    print(ordered_search(index, ranks, 'the'))
    # >>> ['http://udacity.com/cs101x/urank/nickel.html',
    #    'http://udacity.com/cs101x/urank/arsenic.html',
    #    'http://udacity.com/cs101x/urank/hummus.html',
    #    'http://udacity.com/cs101x/urank/index.html']

    print(ordered_search(index, ranks, 'babaganoush'))
    # >>> None


if __name__ == '__main__':

    test()

