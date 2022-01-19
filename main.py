import random
import string
import webbrowser
import urllib.request

x = int(input("How many images: "))

c = 0
while c < x:

    #base
    link = "https://prnt.sc/"

    #generate random site
    r = random.randint(6, 7)
    link += "".join(random.choices(string.ascii_lowercase + string.digits, k = r))

    #get website
    request_url = urllib.request.urlopen(urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}))

    #get link
    sub1 = '<img class="no-click screenshot-image" src="'
    sub2 = '" crossorigin="anonymous"'

    html = request_url.read().decode()

    idx1 = html.index(sub1)
    idx2 = html.index(sub2)

    #find image link in the wbsite source
    img_link = ""
    for idx in range(idx1 + len(sub1), idx2):
        img_link += html[idx]

    if (img_link != "//st.prntscr.com/2022/01/07/0148/img/0_173a7b_211be8ff.png"):
        c += 1
        webbrowser.open(img_link, 2)

#webbrowser.open(img_link, 2)