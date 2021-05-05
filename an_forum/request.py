import requests
from bs4 import BeautifulSoup as bs

def get_urls(url):
    count=0
    response=requests.get(url)
    response.status_code
    response.ok
    response.headers
    response.text

    s={}
    s=set(s)
    soup=bs(response.text,'html.parser')
    b=0
    l=set((soup.find_all("td",{"class":"subject windowbg2"})))
    l1=set((soup.find_all("td",{"class":"subject stickybg2"})))
    l = l.union(l1)
    urls=set({})
    for k in l:
        b+=1
        urls.add(k.find("span").a['href'])
    return urls

def analise(url):
    count=0
    response=requests.get(url)
    response.status_code
    response.ok
    response.headers
    response.text

    s={}
    s=set(s)
    soup=bs(response.text,'html.parser')
    l=len(soup.find_all("div",{"class":"poster"}))
    for i in range(0,l):
        a=soup.find_all("div",{"class":"poster"})[i]
        c=a.a
        if hasattr(c, '__iter__'):
            for i in c:
                    count+=1
                    s.add(i)
    return (count,s)
def analise_more(a):

    arr=[]
    num=0
    for z in a:
        name=get_name(z)
        s=""
        title=get_title(z)
        for i in name:
            s+="  "
            s+=i
        count=get_count(z)
        num+=1
        struct=(num,title,count,s,name)
        arr.append(struct)
    return arr


def get_title(usr):
    response = requests.get(usr)
    response.status_code
    response.ok
    response.headers
    response.text

    s = {}
    s = set(s)
    soup = bs(response.text, 'html.parser')
    a = (soup.find_all("div", {"class": "keyinfo"}))
    b = a[0]
    c = b.a
    for i in c:
        z = i

        return z

def page_info(arr):
    count=0
    amount=0
    for i in arr:
        count+=1
        amount+=i[2]
    av_num=amount/count
    return av_num

def page_name(arr):

    maxelem=-1
    name="empty"
    dic=dict({})
    for i in arr:
        for j in i[4]:
            dic[str(j)]=0
            if ( dic[str(j)])>maxelem:
                maxelem=dic[str(j)]
                name=str(j)

    for i in arr:
        for j in i[4]:
            dic[str(j)]+=1
            if ( dic[str(j)])>maxelem:
                maxelem=dic[str(j)]
                name=str(j)
    par=[name,maxelem]
    return par[0]

def page_mes(arr):

    maxelem=-1
    name="empty"
    dic=dict({})
    for i in arr:
        for j in i[4]:
            dic[str(j)]=0
            if ( dic[str(j)])>maxelem:
                maxelem=dic[str(j)]
                name=str(j)

    for i in arr:
        for j in i[4]:
            dic[str(j)]+=1
            if ( dic[str(j)])>maxelem:
                maxelem=dic[str(j)]
                name=str(j)
    par=[name,maxelem]
    return par[1]

def get_name(url):
    return analise(url)[1]

def get_count(url):
    return analise(url)[0]
