from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
import re
import random

class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def setUpClass(self):
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)

    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div", "mw-content-text")
        self.assertIsNotNone(content)

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikiprdia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.countTestCases())
            url = self.getNextLink()
        print("Done!")

    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6) :]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self,source, baseUrl):
        links = self.bs.find('div', {'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

        randomLink = random.SystemRandom().choice(links)

        return 'https://wikipedia.org{}'.format(randomLink.attrs['href'])

if __name__ == "__main__":
    unittest.main()
