from pyquery import PyQuery as pq

def get_data():
    # with open('./data.html','r') as f:
    #     res = f.read()
    # doc = pq(res)

    # doc = pq(url)

    doc = pq(filename='./data.html')
    response = doc('.odd,.even')
    lst = []
    for item in response.items():
        node = item('.v_sensor_id.th5').text()
        lst.append(node)
    nodes = ','.join(lst)
    print nodes
    print len(lst)
    return nodes


if __name__ == '__main__':
    get_data()

