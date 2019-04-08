from mongo_util import MongoIns
m_util = MongoIns()

host = '192.168.111.149:27017'
dbname = 'luzhou'


fields = {'name': 1, 'bridgetype': 1, 'qiaolcd': 1, 'qiaommj': 1, 'xunjzq': 1, 'location': 1 }
bridges, _ = m_util.m_list('bridgeinfo',dbname=dbname,host=host, fields=fields, findall=True, location={'$exists': True})
bids = [item['_id'] for item in bridges]
print bids,'dddddddddddd'
cond = [
        {'$match': {'bridgeid': {'$in': bids}, 'weixiu': {'$ne': True}, 'chuzhi': {'$ne': True}}},
        {'$group': {
            '_id': '$bridgeid',
            'disease_count': {'$sum': 1}
        }},
]
disease = m_util.m_aggregate('bridgexunjian', cond, dbname=dbname, host=host)
print list(disease)


piplines = [
            {'$match': {'bridgeid': {'$in': bids}, 'record': True}},
            {'$sort': {'ts': -1}},
            {'$group': {
                '_id': '$bridgeid',
                'xunj_lasttime': {'$first': '$time'},
                'addon': {'$first': '$addon'},
                'user': {'$first': '$user'}
            }},
]
record = m_util.m_aggregate('bridgexunjian', piplines, dbname=dbname, host=host)
print list(record)
