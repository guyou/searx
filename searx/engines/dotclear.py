# Doku Wiki
#
# @website     https://www.dotclear.org/
# @provide-api no
#
# @using-api   no
# @results     HTML
# @stable      yes
# @parse       (general)    url, title, content

from urllib import urlencode
from lxml.html import fromstring
from searx.engines.xpath import extract_text
from searx.search import logger

logger = logger.getChild('dotclear engine')


# engine dependent config
categories = ['general']  # TODO , 'images', 'music', 'videos', 'files'
paging = False
language_support = False
number_of_results = 5

# search-url
# Doku is OpenSearch compatible
base_url = 'http://localhost:8090'
search_url = '/?{query}'
# TODO             '&startRecord={offset}'\
# TODO             '&maximumRecords={limit}'\

# XPATH for selecting posts
# Depending on the version, Dotclear use content or d-content
posts_xpath = '//div[@id="content" or @id="d-content"]/'\
              'div[contains(concat(" ", normalize-space(@class), " "), " post ")]'


# do search-request
def request(query, params):

    params['url'] = base_url +\
        search_url.format(query=urlencode({'q': query}))

    return params


# get response from search-request
def response(resp):
    results = []

    doc = fromstring(resp.text)

    # parse results
    matches = doc.xpath(posts_xpath)
    logger.debug("Found %d", len(matches))
    for r in matches:
        try:
            res_url = r.xpath('.//h2[@class="post-title"]/a/@href')[-1]
        except:
            continue

        if not res_url:
            continue

        title = extract_text(r.xpath('.//h2[@class="post-title"]/a'))
        content = extract_text(r.xpath('.//div[@class="post-content"]'))

        # append result
        results.append({'title': title,
                        'content': content,
                        'url': base_url + res_url})

    # return results
    return results
