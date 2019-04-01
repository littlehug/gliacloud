import os

def counting(urls):
    counter = dict()
    for url in urls:
        url = os.path.basename(url)
        if url in counter:
            counter[url] += 1
        else:
            counter[url] = 1
    sorting = sorted(counter.items(), key=lambda d: (-d[1], d[0]))
    for k in sorting[:3]:
        print('{} {}'.format(k[0], k[1]))


if __name__ == '__main__':
    urls = [
            "http://www.google.com/a.txt",
            "http://www.google.com.tw/a.txt",
            "http://www.google.com/download/c.jpg",
            "http://www.google.co.jp/a.txt",
            "http://www.google.com/b.txt",
            "https://facebook.com/movie/b.txt",
            "http://yahoo.com/123/000/c.jpg",
            "http://gliacloud.com/haha.png",
            ]
    counting(urls)
