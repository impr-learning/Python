import re

html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> 一路上有你 </li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''


def eg1(html):
    results = re.findall(r'<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
    print(results)
    print(type(results))
    for result in results:
        print(result[0], result[1], result[2])


def eg2(html):
    results = re.findall('<li.*?>(.*?)</li>', html, re.S)
    for result in results:
        print(re.sub('<a .*?>|</a>', '', result.strip()).strip())
        # print(result.strip())


def compiles():
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 12:55'
    content3 = '2016-12-22 13:21'
    pattern = re.compile(r'\s.*')
    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)
    print(result1, result2, result3)


def eg3():
    pattern = re.compile(r'(\d{3})-(\d{3,8})')
    print(pattern)
    res = re.match(pattern, '010-123456')
    print(res.group())
    print(res.groups())


if __name__ == '__main__':
    # eg1(html)
    # eg2(html)
    # compiles()
    eg3()
