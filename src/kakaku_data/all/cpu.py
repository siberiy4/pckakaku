
import json
import get_data

def get_cpu():
    kind='cpu'


    pages=get_data.page_num(kind)
    pages = 1
    print(pages)

    for i in range(1,pages+1):
        elems=get_data.get_item(kind,i)
        data = purse_CPU(elems)
        path1 = './cpu'+str(i)+'.json'
        json_file1 = open(path1, mode="w", encoding="utf-8" )
        json.dump(data, json_file1, ensure_ascii=False)
        json_file1.close()
        pass







def purse_CPU(elems):
    length = (len(elems)-2)//3
    data=[]

    for i in range(length):
        item={
        'ID':elems[i*3+2].find('input').attrs['value'] ,
        'maker':elems[i*3+2].find('span').text.replace('\u3000', '') ,
        'name':elems[i*3+2].find('a').text.split('\u3000')[1],
        'price':elems[i*3+3].find(class_="pryen").text.replace(',','')[1:],
        'processor':elems[i*3+3].find(class_="swdate2").next_element.next_element.next_element.text,
        'socket':elems[i*3+3].find(class_="sortBox").text,
        'generation':elems[i*3+4].find('a').text,
        'core':elems[i*3+3].find_all(class_="sortBox")[1].text.replace('コア',''),
        'thread':elems[i*3+3].find_all("td")[12].text,
        }
        data.append(item)

        pass

    return data

    pass
