import requests,bs4
print('Getting webpage')
i=0

for i in range(500000):
    res=requests.get('http://www.imdb.com/title/tt'+str(i)+'/')
    #print('Got webpage,beginning to parse')
    if(res.status_code==requests.codes.ok):
        souper=bs4.BeautifulSoup(res.text,"lxml")
        xx=souper.select('h1[itemprop="name"]')
        bb=souper.select('span[itemprop="ratingValue"]')
        if(len(xx)!=0):
            xxy=xx[0]
            if(len(bb)!=0):
                bby=bb[0]
                #xx=souper.select('span[itemprop="ratingValue"]')[0]
                print(xxy.getText()+ '\t\t\t\t\t\t\t\t\t' +bby.getText())
            else:
                print(xxy.getText()) 
    #print(len(xx))
    
