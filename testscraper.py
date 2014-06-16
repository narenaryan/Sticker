from scraper import scrape
from urllib import urlretrieve

def first_scrape():
    fir_url_box=scrape('http://ukiyo-e.org/','//a[contains(@href,"artist")]/@href')
    print "i am in first"
    print fir_url_box
    return fir_url_box

def second_scrape():
    fir_url_box=list(first_scrape())
    print "i am in second"
    sec_url_box=[]
    for ele in fir_url_box:
        print ele
        for item in scrape(ele,'//a[@class="img"]/@href'):
            yield item

def third_scrape():
    print "i am in third"
    third_url_box=[]
    for ele in second_scrape():
        for item in scrape(ele,'//a[contains(@href,"images")]/@href'):
            yield item
def art_download():
    print "Downloading art from ukiyo.org"
    for url in third_scrape():
         print "Downloading from %s"%(url)
         urlretrieve(url,"%s"% url.split('/')[-1])
    print "finished"

art_download()
