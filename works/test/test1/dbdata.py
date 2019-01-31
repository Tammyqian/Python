from mongo_util import MongoIns
m_util = MongoIns()
DB_NAME = 'sensorcmd'
DB_HOST = '192.168.111.149:27019'

project = m_util.m_find_one('main_vsnproject', dbname=DB_NAME, host=DB_HOST,fields={'monitor_items':1},code_name='bp001')
print project
monitors = project.get('monitor_items')
print monitors
temp_humi, _ = m_util.m_list('newest_data',dbname='bp001',host=DB_HOST,fields={'ts':1,'temperature':1,'humidity':1},sensor_type={'$in':monitors})
print temp_humi