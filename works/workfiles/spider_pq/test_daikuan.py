import pandas as pd
from pyquery import PyQuery as pq
# import pandas as pd

def get_data():
    doc = pq(filename='./newdata.html')
    ul = doc('li')
    lst = []
    for i in ul.items():
        name = i("a > h6").text()
        addr = i("a > p").eq(0).text()
        lst.append([name, addr])

    print len(lst)
    return lst


def get_data2():
    doc = pq(filename='./newdata2.html')
    ul = doc('li')
    lst = []
    for i in ul.items():
        name = i("a > h6").text()
        addr = i("a > p").eq(0).text()
        lst.append([name, addr])

    print len(lst)
    return lst


if __name__ == '__main__':
    l1 = get_data()
    l2 = get_data2()
    lst = l1 + l2
    print lst
    print len(lst)
    df = pd.DataFrame(lst, columns=['name', 'addr'])
    df.to_csv('daikuan.csv', encoding='utf8')

