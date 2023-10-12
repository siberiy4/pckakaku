from bs4 import BeautifulSoup
import requests

base_url="https://kakaku.com/pc/"

def get_item(item_kind,current):
    # データ保存配列

    url="https://kakaku.com/pc/"+item_kind+"/itemlist.aspx"

    # pages=page_num(url=url)

    # データダウンロード
    page_url_base = base_url+"?pdf_vi=d&pdf_so=e2&pdf_pg="
    

    page_url = page_url_base + str(current)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    elems=soup.find_all(class_="tr-border")

    return elems

    pass




def page_num(item_kind):
    url="https://kakaku.com/pc/"+item_kind+"/itemlist.aspx"

    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    soup.find(class_="result").span.text
    elems=soup.find_all(class_="tr-border")


    # 上で確認したページ数を入力
    pages = int(soup.find(class_="result").span.text)//40 + 1

    return pages 
    pass
