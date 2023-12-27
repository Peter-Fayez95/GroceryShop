import requests
from bs4 import BeautifulSoup
import pandas as pd

no_pages = 2

def get_data(pageNo):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get(f"https://www.amazon.eg/-/en/gp/bestsellers/grocery/ref=zg_bs_pg_{pageNo}_grocery?ie=UTF8&pg={pageNo}", headers=headers)
    content = r.content
    soup = BeautifulSoup(content,'lxml')
    #print(soup)

    alls = []
    for d in soup.findAll('div', attrs={'class':'a-cardui _cDEzb_grid-cell_1uMOS expandableGrid p13n-grid-content'}):
        #print(d)
        photo = d.find('div', attrs={'class':'a-section a-spacing-mini _cDEzb_noop_3Xbw5'})
        p = photo.find('img', alt=True)
        #print(p['src'])
        desc = d.find('div', attrs={'class':'_cDEzb_p13n-sc-css-line-clamp-3_g3dy1'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        price = d.find('span', attrs={'class':'_cDEzb_p13n-sc-price_3mJ9Z'})
        productPage = d.find('a', attrs={'class':'a-link-normal'})
        nextContent = requests.get( "https://www.amazon.eg"+productPage['href'] , headers=headers)
        soupNext = BeautifulSoup(nextContent.content,'lxml')
        brand = soupNext.find('tr', attrs = {'class' : 'a-spacing-small po-brand'})
        if brand is not None:
            brand = brand.find('span', attrs = {'class' : 'a-size-base po-break-word'})
        
        #print(brand.text)
        
        all1=[]

        if desc is not None:
            #print(author.text)
            all1.append(desc.text)
        else:    
            all1.append('Unknown')
        
        if brand is not None:
            #print(author.text)
            all1.append(brand.text)
        else:    
            all1.append('Unknown')
        
        
        
        if rating is not None:
            #print(rating.text)
            all1.append(rating.text)
        else:
            all1.append('-1')   

        if price is not None:
            #print(price.text)
            all1.append("EGP " +price.text[4:])
        else:
            all1.append('0')
            
        if p is not None:
            #print(n[0]['alt'])
            all1.append(p['src'])
        else:
            all1.append("unknown-product")
        alls.append(all1)    
        
    return alls

results = []
for i in range(1, no_pages+1):
    results.append(get_data(i))
#print(results[:10])
# get_data(2)
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Description','Brand' ,'Rating', 'Price','Img url'])
print(df.head())
df.to_csv('products.csv', index=False, encoding='utf-8')

# df = pd.read_csv("/home/mongy/Documents/scraper/products.csv")
# print(len(df))