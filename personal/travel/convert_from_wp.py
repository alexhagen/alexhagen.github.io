from bs4 import BeautifulSoup
import requests
import subprocess
import shutil
from datetime import datetime
import time

class post(object):
    def __init__(self, src, banner, title, date):
        self.src = src
        self.banner = banner
        self.title = title
        self.date = date
        self.imgs = []
        self.imgsrcs = []
        self.captions = []
        self.imgurls = []
        self.markdown = ''

    def scrape(self):
        url = self.src
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        title = soup.findAll("h2", {"class" : "entry-title"})[0].text.encode('utf-8').strip().strip()
        self._title = title
        self._entry_content = soup.find('div', {'id': 'entry-content'}).find('p').text.encode('utf-8').strip()
        images = soup.findAll('div', {'class': 'wp-caption'})
        for image in images:
            caption = image.find('p', {'class': 'wp-caption-text'}).text.encode('utf-8').strip()
            imgsrc = image.find('a').get('href')
            self.captions.extend([caption])
            self.imgsrcs.extend([imgsrc])
        return self

    @staticmethod
    def upload_to_imgur(src):
        response = requests.get(src, stream=True)
        with open('/Users/ahagen/temp.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        p = subprocess.Popen(['imgur-uploader /Users/ahagen/temp.png'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True)
        (out, err) = p.communicate()
        print out, err
        url = out.splitlines()[-1].replace('File uploaded - see your image at ', '')
        print url
        return url

    def procimgs(self):
        if self.banner is not None:
            self._feature = self.upload_to_imgur(self.banner)
        else:
            self._feature = ''
        for imgsrc in self.imgsrcs:
            self.imgurls.extend([self.upload_to_imgur(imgsrc)])
        return self

    def printmd(self):
        self.markdown += '''---
title: "{title}"
layout: post-light-feature
date:   {date}
long_title: false
comments: true
image:
    feature: "{fb}"
---\n'''.format(title=self._title, date=self.date, fb=self._feature)
        self.markdown += '# {title}\n\n'.format(title=self._title)
        self.markdown += '{ec}\n\n'.format(ec=self._entry_content)
        for imgurl, caption in zip(self.imgurls, self.captions):
            self.markdown += \
                '''<figure>
    <img src="{url}">
    <figcaption>{cap}</figcaption>
</figure>\n'''.format(url=imgurl, cap=caption)
        time = datetime.strptime(self.date, '%B %d, %Y at %I:%M %p')
        datefortitle = datetime.strftime(time, '%Y-%m-%d-')
        fname = datefortitle + self.title.lower().replace(' ', '_')
        with open('_posts/' + fname + '.md', 'w') as f:
            f.write(self.markdown)
        return self

posts = []

"""
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/16/prague/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_1493.jpg",
    "Prague", "June 16, 2012 at 6:15 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/14/dresden/",
    "https://experimentingexpats.files.wordpress.com/2012/06/sta_1362_stitch.jpg",
    "Dresden", "June 14, 2012 at 10:56 am")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/12/wroclaw/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_13301.jpg",
    "Wroclaw", "June 12, 2012 at 5:53 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/12/berlin/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_1283.jpg",
    "Berlin", "June 12, 2012 at 10:43 am")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/10/amsterdam/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_1213.jpg",
    "Amsterdam", "June 10, 2012 at 1:07 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/08/paris-day-2/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_1054.jpg",
    "Paris, Day 2", "June 8, 2012 at 2:20 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/07/paris-day-1/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_1011.jpg",
    "Paris, Day 1", "June 7, 2012 at 4:51 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/05/munich/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_0821.jpg",
    "Munich", "June 5, 2012 at 5:13 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/04/dachau/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_0741.jpg",
    "Dachau", "June 4, 2012 at 6:19 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/03/vienna-to-munich/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_0452.jpg",
    "Vienna to Munich", "June 3, 2012 at 6:22 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/02/vienna/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_0579.jpg",
    "Vienna", "June 2, 2012 at 5:15 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/06/01/divci-komon-and-cesky-krumlov-day-2/",
    "https://experimentingexpats.files.wordpress.com/2012/06/img_0355.jpg",
    "Divci Komon and Cesky Krumlov, Day 2", "June 1, 2012 at 12:32 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/05/31/cesky-krumlov/",
    "https://experimentingexpats.files.wordpress.com/2012/05/img_0323.jpg",
    "Cesky Krumlov", "May 31, 2012 at 12:26 pm")])
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/05/31/no-pictures-for-now-because-of-delta/",
    None,
    "No Pictures (for now) Because of Delta", "May 31, 2012 at 1:46 am")])
"""
posts.extend([post(\
    "https://experimentingexpats.wordpress.com/2012/05/29/our-europe-itenerary/",
    "https://experimentingexpats.files.wordpress.com/2012/05/europe-itenerary.png",
    "Our Europe Itenerary", "May 29, 2012 at 1:12 pm")])

#time.sleep(3605)
for _post in posts:
    _post.scrape().procimgs().printmd()
    #time.sleep(3605)
