from lxml import html
import requests
from urlparse import urljoin
def scrape(url,cont=""):
    page=requests.get(url)
    tree=html.fromstring(page.text)
    url_box=set(tree.xpath(cont))
    return url_box
