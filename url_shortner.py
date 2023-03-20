import pyshorteners
url = input('Enter the url:')


def shortenur1(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenur1(url)

