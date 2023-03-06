import requests
from bs4 import BeautifulSoup
from scraper.models import Wine

def run():
    for a in range(1,10):
        url = "http://www.kajawine.kr/shop/list.php?ca_id=10&sort=&sortodr=&type_color=1&it_price=&it_opt4=&it_opt9=&page="+str(a)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select("li.item_thumb")
        for item in items:
            try:
                #와인 이름
                name= item.select("div.listImg>a>img")[0].get("alt").strip()
                name= name.split("(VAT 별도)")[0]
                print("와인명:",name)
                
                
                #와인 종류, 도수, 용량
                wine_info = item.find("div","list_ex").text.strip()
                info_splited = wine_info.split(' ')
                
                #와인의 종류
                category = info_splited[2][:-2]
                def category_func(category):
                    if category == "RED":
                        return category.replace("RED","레드")
                    elif category == "":                   
                        return category.replace("","정보없음")
                    elif category == "화":
                        return "화이트"
                    else:
                        return category                
                category = category_func(category)
                print("종류:" ,category_func(category))
                
                #와인의 도수
                alcohol= info_splited[-1][:2]
                def alcohol_func(alcohol):
                    if alcohol.endswith("~"):
                        return alcohol.replace("~","")
                    elif alcohol.endswith("%"):
                        return alcohol.replace("%","")
                    elif (alcohol == ":")or(alcohol == "%")or(alcohol == " "):
                        return 12
                    else :
                        return alcohol
                alcohol =alcohol_func(alcohol)                                 
                print("도수:", alcohol_func(alcohol))
                
                #와인의 용량
                capacity= info_splited[4][:-2]
                capacity = capacity.replace(",","")
                def capacity_func(capacity):
                    if capacity != 750:
                        return 750
                print("용량:", capacity_func(capacity))
                capacity = capacity_func(capacity)
                
                
                #와인 세일
                discount = item.find("div","sale_buble_s").text.strip()
                discount = discount.split('%')[0]
                print("세일:",discount)
                
                #와인 가격
                price = item.find_all("div","sct_cost")[0].text.strip()[:-1]
                price = price.split('\n')[1]
                price = price.replace(",","")
                
                # print(price)
                def price_func(prirce):
                    result = ''
                    for s in price:
                        if s.isdigit()==True:
                            result +=s
                    return int(result)
                print("가격:",price_func(price))
                price = price_func(price)
                
                # 이미지        
                img_url = item.select("div.listImg>a>img")[0].get("src").strip() 
                print("이미지url: ", img_url)
                # 상세정보로 가는 링크
                link = item.select("div.listImg>a")[0].get("href").strip()
                print("링크:",link)
                
                
                db_cnt = Wine.objects.filter(link__iexact=link).count()
                print(db_cnt)
                
                if(db_cnt==0):
                    # print("들어왔음")
                    try:
                        print("들어왔음1")
                        print(capacity)
                        Wine(name=name,img_url=img_url,link=link, wine_info=wine_info,category=category,alcohol=alcohol,capacity=capacity,discount=discount,price=price).save()                  
                        print("들어왔음2")
                    except Exception as e:
                        
                        print(e)
                else : 
                    print("실패")


            except Exception as e:
                # #예외 처리
                # category, capacity, alcohol은 숫자만 들어갈 수 있으므로, 예외는 전부 0으로 처리 
                category = (print('레드') if info_splited[2][:-2] == "RED" else info_splited[2][:-2])
                category = (print('정보없음') if info_splited[2][:-2].__len__() == 0 else info_splited[2][:-2])
                
                capacity = 0  if (info_splited[4][: info_splited[4].__len__()-2]=='') else info_splited[4][: info_splited[4].__len__()-2]
                
                alcohol =  0 if (info_splited[-1][:-1] =='') else info_splited[-1][:-1]
                
                price = 0 if (type(price) == str) else int(price)
                
                # type casting 
                # integer : price, capacity, discount
                
                # discount = int(discount)
                
                # price = int(price)
                
                # capacity = int(capacity)
                
                # #float : alcohol
                # alcohol = float(alcohol)
                
                continue