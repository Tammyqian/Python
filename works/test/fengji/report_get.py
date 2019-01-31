from mongo_util import MongoIns
import time

HOST = "192.168.111.10:27037"

def get_data(fj_num):
	condition = {"fj_num": fj_num, "findall":"1"}
	alarms, _ = MongoIns().m_list("data_6d_mean_err", host=HOST, dbname="wf_HuaRui", sorts=[("ts",1)], **condition)
	cache_a = 0
	sy_lst = []
	for index, alarm in enumerate(alarms):
		alarm["ts"] = int(alarm["ts"])
		ts = alarm["ts"]
		if cache_a == 0:
			cache_a = ts
			continue
		if ts - cache_a != 300:
			_a = alarms[index - 1]
			for i in range(int(cache_a), int(ts), 300):
				sy_lst.append({"ts":i,"Score":_a["Score"]})
		cache_a = ts

	res = alarms + sy_lst
	datas = sorted(res, key=lambda d: d["ts"])
	str_time = lambda x:time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x))
	alarms = [data["ts"] for data in datas if data["Score"] >=50]
	delt = 300
	def compute_split(datas, delts=300):
		m = len(datas)
		result = []
		count = 0
		split = 0
		for i in range(1, len(datas), 1):
			if datas[i] - datas[i-1] > delts:
				if not result:
					result.append((datas[0], datas[i-1]))
				else:
					result.append((datas[i-1-count], datas[i-1]))
				count = 0
				split = i
			else:
				count += 1

			if i == m-1:
				if count:
					result.append((datas[split], datas[m-1]))
		return result

	res = compute_split(alarms, delts=delt)
	res2 = [["start", "end", "keep_time"]]
	for s,e in res:
		res2.append([str_time(s), str_time(e), e-s])
	return res2

#test: 34,44,48,54,64
res = get_data(64)
for i in res:
	print i