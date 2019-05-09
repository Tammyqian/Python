#encoding=utf-8


LOCATION = {'0': '路面系','1':'上部结构','2':'下部结构'}

DISEASE_STATUS = [('0', '病害发生'), ('1', '已处置'), ('2', '已维修')]

#需要进行养护的工程类别
GONGCLB = ['养护维修(小修)', '大中修', '改扩建']

# 道路
ROAD_SEARCH_COLUMN = [
	('道路识别数据', [
		(u"道路名称", "name", "input", {}),
		(u"路面结构", "lumjg", "select", {}),
		(u"道路类别", "daollb", "select", {}),
		(u"道路养护等级", "daolyanhdj", "select", {}),
		(u"道路等级", "daoldj", "select", {}),
		(u"设计年限", "shejnx", "input", {"datatype":"n", "unit":"年"}),
		(u"巡检周期", "xunjzq", "select", {"datatype":"n", "unit":""}),
		(u"道路总面积", "daolzmj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
		(u"车行道面积", "chexdmj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
		(u"非机动车道面积", "feijdcdmj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
		(u"机动车道面积", "jidcdmj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
		(u"人行道面积", "renxdmj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
		(u"地区", "postcode", "select", {}),
		(u"道路起点", "daolqd", "input", {}),
		(u"道路终点", "daolzd", "input", {}),
		(u"开工日期", "kaigrq", "input", {"datatype":"/^\d{4}-\d{2}-\d{2}$/", "placeholder":"yyyy-mm-dd", "errormsg" : "请输入正确的日期:yyyy-mm-dd"}),
		(u"竣工日期", "jungrq", "input", {"datatype":"/^\d{4}-\d{2}-\d{2}$/", "placeholder":"yyyy-mm-dd", "errormsg" : "请输入正确的日期:yyyy-mm-dd"}),
		(u"接管日期", "jiegrq", "input", {"datatype":"/^\d{4}-\d{2}-\d{2}$/", "placeholder":"yyyy-mm-dd", "errormsg" : "请输入正确的日期:yyyy-mm-dd"}),
		(u"道路总宽度", "daolzkd", "input", {"unit":"m"}),
		(u"道路长度", "daolcd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"非机动车道宽度", "feijdcdkd", "input", {"unit":"m"}),
		(u"机动车道宽度", "jidcdkd", "input", {"unit":"m"}),
		(u"人行道宽度", "renxdkd", "input", {"unit":"m"}),
		(u"设计单位", "shejdw", "input", {}),
		(u"管理单位", "guanldw", "select", {}),
		(u"养护单位", "yanghdw", "select", {}),
		(u"监理单位", "jianldw", "input", {}),
		(u"施工单位", "shigdw", "input", {}),
		(u"建设单位", "jiansdw", "input", {}),
		(u"桥梁编号", "no", "input", {})
		]),
	('附属设施', [
		(u"雨水管长", "ysgc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"检查井", "jcj", "input", {"datatype":"n", "unit":"座"}),
		(u"标志牌", "bzp", "input", {"datatype":"n", "unit":"块"}),
		(u"排水沟", "psg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"雨水井", "ysj", "input", {"datatype":"n", "unit":"只"}),
		(u"盲道", "md", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"雨水出水口", "yscsk", "input", {"datatype":"n", "unit":"个"}),
		(u"涵洞", "hd", "input", {"datatype":"n", "unit":"个"}),
		(u"停车场", "tcc", "input", {"datatype":"n", "unit":"个"}),
		(u"广场", "gc", "input", {"datatype":"n", "unit":"个"})
		]),
	('下水道', [
		(u"总长度", "zcd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"∮150~∮230", u"zj150~230", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"∮300", u"zj300", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"≤∮500", u"ltezj500", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"∮600", u"zj600", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"∮800", u"zj800", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u"∮1000", u"zj1000", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u">∮1000", u">zj1000", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
		]),
	('路面技术状况及养护状况', [
		(u"城镇道路养护等级", "road_hgl", "input", {"type" : ["disabled"]}),
		(u"路面综合评价评分", "cdpqi", "input", {"type" : ["disabled"]}),
		(u"路面综合评价等级", "cdpqi_level", "input", {"type" : ["disabled"]}),
		(u"路面损坏状况评分", "cd_pci", "input", {"type" : ["disabled"]}),
		(u"路面损坏状况等级", "cd_pci_level", "input", {"type" : ["disabled"]}),
		(u"路面行驶质量评分", "cdpzd_rqi", "input", {"type" : ["disabled"]}),
		(u"路面行驶质量等级", "cdpzd_rqi_level", "input", {"type" : ["disabled"]}),
		(u"机动车道路面抗滑SFC", "jidcdkh_sfc", "input", {"type" : ["disabled"]}),
		(u"机动车道路面抗滑SFC等级", "jidcdkh_sfc_level", "input", {"type" : ["disabled"]}),
		(u"机动车道路面抗滑BPN", "jidcdkh_bpn", "input", {"type" : ["disabled"]}),
		(u"机动车道路面抗滑BPN等级", "jidcdkh_bpn_level", "input", {"type" : ["disabled"]}),
		(u"非机动车道路面抗滑SFC", "feijidcdkh_sfc", "input", {"type" : ["disabled"]}),
		(u"非机动车道路面抗滑SFC等级", "feijidcdkh_sfc_level", "input", {"type" : ["disabled"]}),
		(u"非机动车道路面抗滑BPN", "feijidcdkh_bpn", "input", {"type" : ["disabled"]}),
		(u"非机动车道路面抗滑BPN等级", "feijidcdkh_bpn_level", "input", {"type" : ["disabled"]}),
		(u"人行道损坏状况评分", "renxd_fci", "input", {"type" : ["disabled"]}),
		(u"人行道损坏状况等级", "renxd_fci_level", "input", {"type" : ["disabled"]}),
		(u"人行道质量评分", "renxdpzd_fqi", "input", {"type" : ["disabled"]}),
		(u"人行道质量等级", "renxdpzd_fqi_level", "input", {"type" : ["disabled"]}),
		(u"路面结构强度弯沉值", "jiegqd_lbhtwcz", "input", {"type" : ["disabled"]}),
		(u"路面结构强度等级", "jiegqd_lbhtwcz_level", "input", {"type" : ["disabled"]}),
		(u"车行道合格率", "road_chexd_hgl", "input", {"type" : ["disabled"]}),
		(u"人行道合格率", "road_renxd_hgl", "input", {"type" : ["disabled"]}),
		(u"路基和排水设施合格率", "road_lujpais_hgl", "input", {"type" : ["disabled"]}),
		(u"其他设施合格率", "road_other_hgl", "input", {"type" : ["disabled"]}),
		(u"城镇道路综合完好率", "road_whl", "input", {"type" : ["disabled"]}),
		]),
	('自定义', [
		(u"交通量等级", "jiaotldj", "select", {}),
		(u"基层类型", "jiclx", "select", {})
		])
]



ROAD_WEIXIUCHUZHI = [(u'道路名称', 'road_name'),
					(u'路段名称', 'name'),
                    (u'病害说明', 'content'),
                    (u'维修类型', 'type_name'),
                    (u'维修单位', 'company_name'),
                    (u'维修时间', 'weixrq'),
                    (u'维修对策', 'weixdc'),
                    (u'维修内容', 'weixnr'),
                    (u'工程量', 'gongcl'),
                    (u'维护费用', 'weihfy'),
                    (u'质量状况', 'zhilzk'),
                    (u'处置时间', 'weixrq'),
                    (u'处置情况', 'chuzqk'),
                    (u'观测责任人', 'guanczrr')
                    ]

# 道路列名单位
ROAD_COLUMN_NAME_UNIT = {
	"shejnx" : "年",
	"xunjzq" : "天",
	"daolzmj" : "㎡",
	"chexdmj" : "㎡",
	"feijdcdmj" : "㎡",
	"jidcdmj" : "㎡",
	"renxdmj" : "㎡",
	"daolzkd" : "m",
	"daolcd" : "m",
	"feijdcdkd" : "m",
	"jidcdkd" : "m",
	"renxdkd" : "m",
	"ysgc" : "m",
	"tcc" : "个",
	"gc" : "个",
	"jcj" : "座",
	"bzp" : "块",
	"psg" : "m",
	"ysj" : "只",
	"md" : "m",
	"yscsk" : "个",
	"hd" : "个",
	"zcd" : "m",
	u"zj150~230" : "m",
	u"zj300" : "m",
	u"≤zj500" : "m",
    u"ltezj500":'m',
	u"zj600" : "m",
	u"zj800" : "m",
	u"zj1000" : "m",
	u">zj1000" : "m"
}

# 道路具体项中应排序的keys
ROAD_COLUMN_SORT_KEYS = {
	"道路类别" : ["kuaisl", "zhugl", "cigl", "zhiljqt"],
	"道路养护等级" : ["1", "2", "3"],
	"巡检周期" : ["1", "2", "3"]
}
# 道路具体项
ROAD_COLUMN_VALUES = {
	"路面结构" : {
		"liqlm" : "沥青路面",
		"shuinlm" : "水泥路面",
	},
	"路面类型" : {
		"liqlm" : "沥青路面",
		"shuinlm" : "水泥路面",
	},
	"道路类别" : {
		"kuaisl" : "快速路",
		"zhugl" : "主干路",
		"cigl" : "次干路",
		"zhiljqt" : "支路及其他"
	},
	"道路等级" : {
		"1" : "一级",
		"2" : "二级",
		"3" : "三级",
		"4" : "四级"
	},
	"道路养护等级" : {
		"1" : "Ⅰ级",
		"2" : "Ⅱ级",
		"3" : "Ⅲ级"
	},
	"巡检周期" : {
		"1" : "1",
		"2" : "2",
		"3" : "3"
	},
	"城镇道路养护状况等级" : {
		"1" : "优",
		"2" : "良",
		"3" : "合格",
		"4" : "不合格"
	},
	"路面综合评价等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"路面损坏状况等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"路面平整度等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"人行道损坏状况等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"人行道平整度等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"路面结构强度等级" : {
		"1" : "足够",
		"2" : "临界",
		"3" : "不足"
	},
	"路面抗滑等级" : {
		"1" : "A",
		"2" : "B",
		"3" : "C",
		"4" : "D"
	},
	"基层类型" : {
		'sssjc' : '碎砾石基层',
		'bgxjc' : '半钢性基层'
	},
	"交通量等级" : {
		"1" : "很轻",
		"2" : "轻",
		"3" : "中",
		"4": "重",
		"5" : "特重"
	}
}

ROAD_SECTION = [
	('路段信息', [
		('路段基本信息', [
			(u'路段索引', 'order', 'input', {}),
			(u'路段名称', 'name', 'input', {}),
			(u'起点', 'daolqd', 'input', {}),
			(u'终点', 'daolzd', 'input', {}),
			(u'路段编码', 'ludbm', 'input', {}),
			(u'路面类型', 'lumjg', 'select', {}),
			(u'是否巡检', 'shifxj', 'select', {}),
			(u'建成年代', 'jiancnd', 'input', {}),
			(u'道路类别', 'daollb', 'select', {}),
			(u'路口类型', 'luklx', 'input', {}),
			(u'断面类型', 'duanmlx', 'input', {}),
			(u'车行道总面积', 'chexdzmj', 'input', {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'长度', 'daolcd', 'input', {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'宽度', 'daolzkd', 'input', {"unit":"m"}),
			(u'总面积', 'daolzmj', 'input', {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u"管理单位", "guanldw", "select", {}),
			(u"养护单位", "yanghdw", "select", {})
			]),
		('路段综合评价信息', [
			(u'路面结构强度等级', 'jidcdjiegqd', "input", {"type" : ["disabled"]}),
			(u'路面抗滑等级', '', "input", {"type" : ["disabled"]}),
			(u'路面综合评价等级', 'lumzhpjdj', "input", {"type" : ["disabled"]}),
			(u'PCI评分', 'cd_pci', "input", {"type" : ["disabled"]}),
			(u'车道路面损坏状况等级', 'cd_pci_level', "input", {"type" : ["disabled"]}),
			(u'PQI评分', 'cd_pqi', "input", {"type" : ["disabled"]}),
			(u'PQI等级', 'cd_pqi_level', "input", {"type" : ["disabled"]}),
			(u'RQI评分', 'cdpzd_rqi', "input", {"type" : ["disabled"]}),
			(u'车道路面行驶质量等级', 'cdpzd_rqi_level', "input", {"type" : ["disabled"]}),
			(u'车行道完好率', 'chexd_whl', "input", {"type" : ["disabled"]}),
			(u'车行道养护状况等级', 'chexd_hgl', "input", {"type" : ["disabled"]}),
			(u'人行道完好率', 'renxd_whl', "input", {"type" : ["disabled"]}),
			(u'人行道养护状况等级', 'renxd_hgl', "input", {"type" : ["disabled"]}),
			(u'路基和排水设施完好程度', 'lujpais_whl', "input", {"type" : ["disabled"]}),
			(u'路基和排水设施养护状况等级', 'lujpais_hgl', "input", {"type" : ["disabled"]}),
			(u'其他设施完好程度', 'other_whl', "input", {"type" : ["disabled"]}),
			(u'其他设施养护状况等级', 'other_hgl', "input", {"type" : ["disabled"]}),
		])
	]),
	('机动车道信息', [
		('机动车道基本信息', [
			(u'机动车道面积', 'jidcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行机动车道面积', 'shangxjdcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行机动车道长度', 'shangxjdcdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行机动车道宽度', 'shangxjdcdkd', "input", {"unit":"m"}),
			(u'上行机动车道平石长度', 'shangxjdcdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行机动车道道牙长度', 'shangxjdcddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行机动车道面积', 'xiaxjdcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'下行机动车道长度', 'xiaxjdcdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行机动车道宽度', 'xiaxjdcdkd', "input", {"unit":"m"}),
			(u'下行机动车道平石长度', 'xiaxjdcdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行机动车道道牙长度', 'xiaxjdcddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'机动车道路面结构类型', 'jidcdlmjglx', "input", {}),
			(u'机动车道面层厚度', 'jidcdmchd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'机动车道基层类型', 'jidcdjclx', "input", {}),
			(u'机动车道基层厚度', 'jidcdjchd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'机动车道横断面坡度', 'jidcdhdmpd', "input", {})
		]),
		('机动车道评价信息', [
			(u'机动车道PCI评分', 'jidcd_pci', "input", {"type" : ["disabled"]}),
			(u'机动车道路面损坏状况等级', 'jidcd_pci_level', "input", {"type" : ["disabled"]}),
			(u'机动车道RQI评分', 'jidcdpzd_rqi', "input", {"type" : ["disabled"]}),
			(u'机动车道路面行驶质量等级', 'jidcdpzd', "input", {"type" : ["disabled"]}),
			(u'机动车道PQI评分', 'jidcd_pqi', "input", {"type" : ["disabled"]}),
			(u'机动车道路面PQI等级', 'jidcd_pqi_level', "input", {"type" : ["disabled"]}),
			(u'机动车道结构强度', 'jidcdjiegqd_lbhtwcz', "input", {"type" : ["disabled"]}),
			(u'机动车道结构强度等级', 'jidcdjiegqd', "input", {"type" : ["disabled"]}),
			(u'机动车道路面抗滑BPN', 'jidcdkh_bpn', "input", {"type" : ["disabled"]}),
			(u'机动车道路面抗滑SFC', 'jidcdkh_sfc', "input", {"type" : ["disabled"]}),
			(u'机动车道路面抗滑等级', 'jidcdkh', "input", {"type" : ["disabled"]})
		])
		]),
	('非机动车道信息', [
		('非机动车道基本信息', [
			(u'非机动车道面积', 'feijdcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行非机动车道面积', 'shangxfjdcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行非机动车道长度', 'shangxfjdcdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行非机动车道宽度', 'shangxfjdcdkd', "input", {"unit":"m"}),
			(u'上行非机动车道平石长度', 'shangxfjdcdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行非机动车道道牙长度', 'shangxfjdcddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行非机动车道面积', 'xiaxfjdcdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'下行非机动车道长度', 'xiaxfjdcdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行非机动车道宽度', 'xiaxfjdcdkd', "input", {"unit":"m"}),
			(u'下行非机动车道平石长度', 'xiaxfjdcdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行非机动车道道牙长度', 'xiaxfjdcddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'非机动车道路面结构类型', 'feijdcdlmjglx', "input", {}),
			(u'非机动车道面层厚度', 'feijdcdmchd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'非机动车道基层类型', 'feijdcdjclx', "input", {}),
			(u'非机动车道基层厚度', 'feijdcdjchd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'非机动车道横断面坡度', 'feijdcdhdmpd', "input", {}),
		]),
		('非机动车道评价信息', [
			(u'非机动车道PCI评分', 'feijdcd_pci', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面损坏状况等级', 'feijdcd_pci_level', "input", {"type" : ["disabled"]}),
			(u'非机动车道RQI评分', 'feijdcdpzd_rqi', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面行驶质量等级', 'feijdcdpzd', "input", {"type" : ["disabled"]}),
			(u'非机动车道PQI评分', 'feijdcd_pqi', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面PQI等级', 'feijdcd_pqi_level', "input", {"type" : ["disabled"]}),
			(u'非机动车道结构强度', 'feijdcdjiegqd_lbhtwcz', "input", {"type" : ["disabled"]}),
			(u'非机动车道结构强度等级', 'feijdcdjiegqd', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面抗滑BPN', 'feijdcdkh_bpn', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面抗滑SFC', 'feijdcdkh_sfc', "input", {"type" : ["disabled"]}),
			(u'非机动车道路面抗滑等级', 'feijdcdkh', "input", {"type" : ["disabled"]})
		])
	]),
	('人行道信息', [
		('人行道基本信息', [
			(u'人行道面积', 'renxdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行人行道面积', 'shangxrxdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'上行人行道长度', 'shangxrxdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行人行道宽度', 'shangxrxdkd', "input", {"unit":"m"}),
			(u'上行人行道平石长度', 'shangxrxdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'上行人行道道牙长度', 'shangxrxddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行人行道面积', 'xiaxrxdmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'下行人行道长度', 'xiaxrxdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行人行道宽度', 'xiaxrxdkd', "input", {"unit":"m"}),
			(u'下行人行道平石长度', 'xiaxrxdpsdycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'下行人行道道牙长度', 'xiaxrxddycd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'人行道路面结构类型', 'renxdlmjglx', "input", {}),
			(u'人行道铺装厚度', 'renxdpzhd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'人行道基层类型', 'renxdjclx', "input", {}),
			(u'人行道基层厚度', 'renxdjchd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'人行道横断面坡度', 'renxdhdmpd', "input", {}),
			(u'桥下铺装面积', 'qiaoxpzmj', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"㎡"}),
			(u'桥下铺装长度', 'qiaoxpzcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
			(u'桥下铺装宽度', 'qiaoxpzkd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
		]),
		('人行道评价信息', [
			(u'人行道FCI评分', 'renxd_fci', "input", {"type" : ["disabled"]}),
			(u'人行道路面损坏状况等级', 'renxd_fci_level', "input", {"type" : ["disabled"]}),
			(u'人行道FQI评分', 'renxdpzd_fqi', "input", {"type" : ["disabled"]}),
			(u'人行道质量等级', 'renxdpzd', "input", {"type" : ["disabled"]})
		])
	]),
	('自定义基本信息', [
		(u'设计荷载标准', 'shejhzbz', "input", {}),
		(u'图纸编号', 'tuzbh', "input", {}),
		(u'起止点桩号', 'qizdzh', "input", {}),
		(u'盲道长度', 'mandcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u'中央分隔带类型', 'zhongyfgdlx', "input", {}),
		(u'中央分隔带长度', 'zhongyfgdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u'中央分隔带宽度', 'zhongyfgdkd', "input", {"unit":"m"}),
		(u'上行机动非机动车道分隔带类型', 'shangxjdfjddfgdlx', "input", {}),
		(u'上行机动非机动车道分隔带长度', 'shangxjdfjddfgdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u'上行机动非机动车道分隔带宽度', 'shangxjdfjddfgdkd', "input", {"unit":"m"}),
		(u'下行机动非机动车道分隔带类型', 'xiaxjdfjddfgdlx', "input", {}),
		(u'下行机动非机动车道分隔带长度', 'xiaxjdfjddfgdcd', "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
		(u'下行机动非机动车道分隔带宽度', 'xiaxjdfjddfgdkd', "input", {"unit":"m"}),
		(u'交通量等级', 'jiaotldj', 'select', {}),
		(u'基层类型', 'jiclx', 'select', {}),
		(u'备注', 'beiz', "input", {})
		])
]

# 路面技术评估中路面位置划分
ROAD_LOCATION = {'jidcd' : '机动车道', 'feijdcd' : '非机动车道', 'renxd' : '人行道','chexd':'车行道','lujpais':'路基及排水设施'}
# 路段具体项中应该排序的keys
ROAD_SECTION_SORT_KEYS = {
	"daollb" : ["kuaisl", "zhugl", "cigl", "zhiljqt"]
}
# 路段具体项
ROAD_SECTION_VALUES = {
	"lumjg" : {
		"liqlm" : "沥青路面",
		"shuinlm" : "水泥路面"
	},
    "shifxj" : {
		"need" : "要巡检",
		"not" : "不巡检"
	},
	"daollb" : {
		"kuaisl" : "快速路",
		"zhugl" : "主干路",
		"cigl" : "次干路",
		"zhiljqt" : "支路及其他"
	},
	"jiclx" : {
		'sssjc' : '碎砾石基层',
		'bgxjc' : '半钢性基层'
	},
	"jiaotldj" : {
		"1" : "很轻",
		"2" : "轻",
		"3" : "中",
		"4" : "重",
		"5" : "特重"
	}
}

# 巡检部分
ROAD_XUNJIAN_PROJECT = [
                    ('chexd','车行道',['无病害', '有病害'],'', ''),
                    ('renxd','人行道',['无病害', '有病害'],'', ''),
					('yuans', '缘石', ['完整', '不完整'], '', ''),
					('weizjl', '违章掘路', ['有', '无'], '', ''),
                    ('jcj','检查井',['完整', '不完整'],'', ''),
                    ('ysj','雨水井',['完整', '不完整'],'', ''),
                    ('luj','路基',['无病害', '有病害'],'', ''),
					('lujian', '路肩', ['无病害', '有病害'],'', ''),
                    ('bianp','边坡',['无病害', '有病害'],'', ''),
                    ('dangtq','挡土墙',['无病害', '有病害'],'', ''),
                    ('hd','涵洞',['无病害', '有病害'],'', ''),
                    ('fgd','分隔带',['完整', '不完整'],'', ''),
                    ('hul','护栏',['完整', '不完整'],'', ''),
                    ('bzp','标志牌',['完整', '不完整'],'', ''),
                    ('spz','声屏障',['完整', '不完整'],'', ''),
                    ('zmss','照明设施',['完整', '不完整'],'', ''),
                    ('wajjk','道路保护区内挖掘基坑、建筑打桩、地下管道顶进、河道疏浚、爆破、堆载等',['无', '有'],'', ''),
                    ('jiansjzw','道路保护区内建设建筑物、构筑物',['无', '有'],'', ''),
                    ('meiqg_gaoyx','道路上架设煤气管线或高压线',['无', '有'],'', ''),
                    ('daolsg','道路、道路区域施工',['无', '有'],'', ''),
                    ('daolaq','道路安全运行情况',['良好', '一般'],'', ''),
                    ('other','其他危机行车、行人安全的病害',['无', '有'],'', '')
                    ]

DOUBLE_ROAD_5 = [(u'道路名称', 'road_name'),
                    (u'维修时间', 'weixrq'),
                    (u'维修类型', 'gongclb_name'),
                    (u'维修单位', 'company_name'),
                    (u'维修内容', 'weixnr'),
                    (u'处置情况', 'chuzqk'),
                    (u'维护费用', 'weihfy'),
                    (u'质量状况', 'zhilzk'),
                    (u'观测责任人', 'guanczrr')
                    ]


# 定检部分
ROAD_LUMJG = [
	('liqlm', '沥青路面', [('lumpzd', '路面平整度'), ('renxdpzd', '人行道平整度'), ('jiegqd', '结构强度'), ('lumkh', '路面抗滑'), ('lum', '路面'), ('renxd', '人行道')]),
	('shuinlm', '水泥路面', [('lumpzd', '路面平整度'), ('renxdpzd', '人行道平整度'), ('lum', '路面'), ('renxd', '人行道')])
]

# 病害损坏类型
ROAD_DISEASE_TYPE = [
	('lum', '路面',
		('liqlm', '沥青路面', [('liefl', '裂缝类', [('xianl', '线裂'), ('wangl', '网裂'), ('suil', '碎裂')]),
							  ('bianxl', '变形类', [('chez', '车辙'), ('chenx', '沉陷'), ('yongb', '拥包'), ('fangj', '翻浆')]),
							  ('songsl', '松散类', [('bol', '剥落'), ('kengc', '坑槽'), ('kengb', '啃边')]),
							  ('other', '其他类', [('lukc', '路框差'), ('xiubsh', '修补损坏'), ('jijiang', '唧浆'), ('fanyou', '泛油')])
							  ]),
		('shuinlm', '水泥路面', [('liefl', '裂缝类', [('xianl', '线裂'), ('banjdl', '板角断裂'), ('Dlf', '边角裂缝'), ('jiaoclf', '交叉裂缝和破碎板')]),
								('jiefphl', '接缝破坏类', [('jieflsh', '接缝料损坏'), ('bianjbl', '边角剥落')]),
								('biaomphl', '表面破坏类', [('kengd', '坑洞'), ('biaomflyczbl', '表面纹裂'),('chenzbl','层状剥落')]),
								('other', '其他类', [('cuot', '错台'), ('gongq', '拱起'), ('jij', '唧浆'), ('xiubsh', '修补损坏'), ('lukc', '路框差')])])),
	('renxd', '人行道',
		[('lief', '裂缝'), ('songdhbx', '松动或变形'), ('cangq', '残缺')])
]


# 评分标准
# 综合等级评价
SCORE_PQI = {
	'kuaisl' : [(90, 100, 'A'), (75, 90, 'B'), (65, 75, 'C'), (0, 65, 'D')],
	'zhugl' : [(85, 100, 'A'), (70, 85, 'B'), (60, 70, 'C'), (0, 60, 'D')],
	'cigl' : [(85, 100, 'A'), (70, 85, 'B'), (60, 70, 'C'), (0, 60, 'D')],
	'zhiljqt' : [(80, 100, 'A'), (65, 80, 'B'), (60, 65, 'C'), (0, 60, 'D')]
}
# 路面平整度: RQI = 4.98 - 0.34 * IRI, RQI(0~5)-->IRI(0, 14.7)
SCORE_LUMPZD = {
	'kuaisl' : [(3.6, 5, 'A'), (3, 3.6, 'B'), (2.5, 3, 'C'), (0, 2.5, 'D')],
	'zhugl' : [(3.2, 5, 'A'), (2.8, 3.2, 'B'), (2.4, 2.8, 'C'), (0, 2.4, 'D')],
	'cigl' : [(3.2, 5, 'A'), (2.8, 3.2, 'B'), (2.4, 2.8, 'C'), (0, 2.4, 'D')],
	'zhiljqt' : [(3, 5, 'A'), (2.6, 3, 'B'), (2.2, 2.6, 'C'), (0, 2.2, 'D')]
}
# 人行道平整度
SCORE_RENXDPZD = [
	(2.6, 5, 'A'),
	(2.1, 2.6, 'B'),
	(1.8, 2.1, 'C'),
	(0, 1.8, 'D')
]
# 路面抗滑
BPN_MAX = 10000000
BPN_MIN = -BPN_MAX
SFC_MAX = 10000000
SFC_MIN = -SFC_MAX
SCORE_LUMKH = {
	'BPN' : {
		'kuaisl' : [(42, BPN_MAX, 'A'), (37, 42, 'B'), (34, 37, 'C'), (BPN_MIN, 34, 'D')],
		'zhugl' : [(40, BPN_MAX, 'A'), (35, 40, 'B'), (32, 35, 'C'), (BPN_MIN, 32, 'D')],
		'cigl' : [(40, BPN_MAX, 'A'), (35, 40, 'B'), (32, 35, 'C'), (BPN_MIN, 32, 'D')],
		'zhiljqt' : [(38, BPN_MAX, 'A'), (33, 38, 'B'), (30, 33, 'C'), (BPN_MIN, 30, 'D')]
	},
	'SFC' : {
		'kuaisl' : [(0.42, BPN_MAX, 'A'), (0.37, 0.42, 'B'), (0.34, 0.37, 'C'), (BPN_MIN, 0.34, 'D')],
		'zhugl' : [(0.40, BPN_MAX, 'A'), (0.35, 0.40, 'B'), (0.32, 0.35, 'C'), (BPN_MIN, 0.32, 'D')],
		'cigl' : [(0.40, BPN_MAX, 'A'), (0.35, 0.40, 'B'), (0.32, 0.35, 'C'), (BPN_MIN, 0.32, 'D')],
		'zhiljqt' : [(0.38, BPN_MAX, 'A'), (0.33, 0.38, 'B'), (0.30, 0.33, 'C'), (BPN_MIN, 0.30, 'D')]
	}
}
# 沥青路面/水泥路面损坏状况评价标准
PCI_MAX = 100
PCI_MIN = 0
SCORE_PCI = {
	'kuaisl' : [(90, PCI_MAX, 'A'), (75, 90, 'B'), (65, 75, 'C'), (PCI_MIN, 65, 'D')],
	'zhugl' : [(85, PCI_MAX, 'A'), (70, 85, 'B'), (60, 70, 'C'), (PCI_MIN, 60, 'D')],
	'cigl' : [(85, PCI_MAX, 'A'), (70, 85, 'B'), (60, 70, 'C'), (PCI_MIN, 60, 'D')],
	'zhiljqt' : [(80, PCI_MAX, 'A'), (65, 80, 'B'), (60, 65, 'C'), (PCI_MIN, 60, 'D')]
}
# 人行道损坏状况评价标准
FCI_MAX = 100
FCI_MIN = 0
SCORE_FCI = [
	(FCI_MIN, 50, 'D'),
	(50, 65, 'C'),
	(65, 80, 'B'),
	(80, FCI_MAX, 'A')
]
# 结构强度
PSSI_MAX =100000000
PSSI_MIN = -PSSI_MAX
SCORE_PSSI = {
	'sssjc' : {
		"1" : [(0, 98, '足够'), (98, 126, '临界'), (126, PSSI_MAX, '不足')],
		"2" : [(0, 77, '足够'), (77, 98, '临界'), (98, PSSI_MAX, '不足')],
		"3" : [(0, 60, '足够'), (60, 81, '临界'), (81, PSSI_MAX, '不足')],
		"4" : [(0, 46, '足够'), (46, 67, '临界'), (67, PSSI_MAX, '不足')],
		"5" : [(0, 35, '足够'), (35, 56, '临界'), (56, PSSI_MAX, '不足')]
	},
	'bgxjc' : {
		"1" : [(0, 77, '足够'), (77, 98, '临界'), (98, PSSI_MAX, '不足')],
		"2" : [(0, 56, '足够'), (56, 77, '临界'), (77, PSSI_MAX, '不足')],
		"3" : [(0, 42, '足够'), (42, 59, '临界'), (59, PSSI_MAX, '不足')],
		"4" : [(0, 31, '足够'), (31, 46, '临界'), (46, PSSI_MAX, '不足')],
		"5" : [(0, 21, '足够'), (21, 35, '临界'), (35, PSSI_MAX, '不足')],
	}
}

# 沥青路面损坏单项扣分表
SCORE_LIQLM = {
	'xianl' : [(0, 0.01, 0, 3), (0.01, 0.1, 3, 5), (0.1, 1, 5, 8), (1, 10, 8, 16), (10, 50, 16, 38), (50, 100, 38, 48)],
	'wangl' : [(0, 0.01, 0, 5), (0.01, 0.1, 5, 8), (0.1, 1, 8, 10), (1, 10, 10, 20), (10, 50, 20, 45), (50, 100, 45, 70)],
	'suil' : [(0, 0.01, 0, 8), (0.01, 0.1, 8, 10), (0.1, 1, 10, 15), (1, 10, 15, 30), (10, 50, 30, 55), (50, 100, 55, 80)],
	'chenx' : [(0, 0.01, 0, 3), (0.01, 0.1, 3, 5), (0.1, 1, 5, 12), (1, 10, 12, 25), (10, 50, 25, 47), (50, 100, 47, 63)],
	'chez' : [(0, 0.01, 0, 2), (0.01, 0.1, 2, 7), (0.1, 1, 7, 12), (1, 10, 12, 25), (10, 50, 25, 45), (50, 100, 45, 55)],
	'yongb' : [(0, 0.01, 0, 3), (0.01, 0.1, 3, 10), (0.1, 1, 10, 15), (1, 10, 15, 30), (10, 50, 30, 52), (50, 100, 52, 65)],
	'kengc' : [(0, 0.01, 0, 10), (0.01, 0.1, 10, 15), (0.1, 1, 15, 25), (1, 10, 25, 40), (10, 50, 40, 65), (50, 100, 65, 72)],
	'kengb' : [(0, 0.01, 0, 2), (0.01, 0.1, 2, 4), (0.1, 1, 4, 8), (1, 10, 8, 15), (10, 50, 15, 30), (50, 100, 30, 40)],
	'bol' : [(0, 0.01, 0, 2), (0.01, 0.1, 2, 5), (0.1, 1, 5, 8), (1, 10, 8, 15), (10, 50, 15, 35), (50, 100, 35, 45)],
	'lukc' : [(0, 0.01, 0, 3), (0.01, 0.1, 3, 8), (0.1, 1, 8, 12), (1, 10, 12, 12), (10, 50, 12, 12), (50, 100, 12, 12)],
	'xiubsh' : [(0, 0.01, 0, 2), (0.01, 0.1, 2, 5), (0.1, 1, 5, 8), (1, 10, 8, 15), (10, 50, 15, 25), (50, 100, 25, 33)]
}
SCORE_SHUINLM = {
	'xianl' : [(0, 0.1, 0, 4), (0.1, 1, 4, 9), (1, 5, 9, 38), (5, 10, 38, 62), (10, 20, 62, 70), (20, 100, 70, 80)],
	'banjdl' :[(0, 0.5, 0, 12), (0.5, 1, 12, 25), (1, 3, 25, 33), (3, 5, 33, 44), (5, 7, 44, 55), (7, 100, 55, 65)],
	'Dlf' : [(0, 0.5, 0, 5), (0.5, 1, 5, 12), (1, 3, 12, 17), (3, 5, 17, 23), (5, 7, 23, 29), (7, 100, 29, 35)],
	'jiaoclf' : [(0, 1, 0, 8), (1, 5, 8, 17), (5, 10, 17, 27), (10, 30, 27, 55), (30, 50, 55, 65), (50, 100, 65, 75)],
	'cuot' : [(0, 0.1, 0, 4), (0.1, 1, 4, 7), (1, 5, 7, 23), (5, 10, 23, 29), (10, 20, 29, 36), (20, 100, 36, 41)],
	'gongq' : [(0, 1, 0, 7), (1, 5, 7, 15), (5, 10, 15, 25), (10, 30, 25, 48), (30, 50, 48, 58), (50, 100, 58, 68)],
	'jij' : [(0, 0.1, 0, 2), (0.1, 1, 2, 3), (1, 5, 3, 13), (5, 10, 13, 18), (10, 20, 18, 23), (20, 100, 23, 25)],
	'bianjbl' : [(0, 0.5, 0, 4), (0.5, 1, 4, 11), (1, 3, 11, 15), (3, 5, 15, 21), (5, 7, 21, 27), (7, 100, 27, 35)],
	'kengd' : [(0, 0.02, 0, 9), (0.02, 0.1, 9, 19), (0.1, 0.2, 19, 30), (0.2, 0.6, 30, 60), (0.6, 1, 60, 70), (1, 100, 70, 80)],
	'xiubsh' : [(0, 0.5, 0, 8), (0.5, 1, 8, 17), (1, 5, 17, 34), (5, 10, 34, 52), (10, 50, 52, 71), (50, 100, 71, 80)],
	'biaomflyczbl' : [(0, 0.5, 0, 5), (0.5, 1, 5, 8), (1, 5, 8, 10), (5, 10, 10, 16), (10, 50, 16, 33), (50, 100, 33, 42)],
	'jieflsh' : [(0, 0.1, 0, 1), (0.1, 1, 1, 3), (1, 5, 3, 5), (5, 10, 5, 7), (10, 20, 7, 10),(20, 100, 10, 12)],
	'lukc' : [(0, 0.01, 0, 3), (0.01, 0.1, 3, 8), (0.1, 1, 8, 12), (1, 10, 12, 12), (10, 50, 12, 12), (50, 100, 12, 12)]
}
# 人行道损坏单项扣分表
SCORE_RENXD = {
	'lief' : [(0, 0.01, 0, 12), (0.01, 0.1, 12, 20), (0.1, 1, 20, 25), (1, 10, 25, 42), (10, 50, 42, 64), (50, 100, 64, 80)],
	'songdhbx' : [(0, 0.01, 0, 10), (0.01, 0.1, 10, 18), (0.1, 1, 18, 25), (1, 10, 25, 40), (10, 50, 40, 62), (50, 100, 62, 75)],
	'cangq' : [(0, 0.01, 0, 9), (0.01, 0.1, 9, 15), (0.1, 1, 15, 21), (1, 10, 21, 38), (10, 50, 38, 54), (50, 100, 54, 64)]
}

# 路面养护对策
YANGH_STRATEGY = {
	'liqlm' : [
		{'PCI' : ['A', 'B'], 'RQI' : ['A', 'B'], 'result' : '保养小修'},
		{'PCI' : ['B', 'C'], 'RQI' : ['B', 'C'], 'result' : '保养小修或中修'},
		{'PCI' : ['C'], 'RQI' : ['C'], 'result' : '中修或局部大修'},
		{'PCI' : ['D'], 'RQI' : ['D'], 'result' : '大修或改扩建工程'},
		{'BPN' : ['D'], 'result' : '大修或改扩建工程'},
		{'SFC' : ['D'], 'result' : '大修或改扩建工程'}
	],
	'shuinlm' : [
		{'PCI' : ['A'], 'result' : '保养小修'},
		{'PCI' : ['B'], 'result' : '保养小修或中修'},
		{'PCI' : ['C'], 'result' : '中修或局部大修'},
		{'PCI' : ['D'], 'result' : '大修或改扩建工程'}
	],
	'renxd' : [
		{'FCI' : ['A'], 'result' : '保养小修'},
		{'FCI' : ['B'], 'result' : '保养小修或中修'},
		{'FCI' : ['C'], 'result' : '中修或局部大修'},
		{'FCI' : ['D'], 'result' : '大修或改扩建工程'}
	]
}


# 城镇道路养护状况评定
YANGH_MIN = -100000000
SCORE_YANGH = {
	'kuaisl' : [(95.5, 100, '优'), (88.5, 95.5, '良'), (80.0, 88.5, '合格'), (YANGH_MIN, 80, '不合格')],
	'zhugl' : [(95.0, 100, '优'), (88, 95, '良'), (79, 88, '合格'), (YANGH_MIN, 79, '不合格')],
	'cigl' : [(94.5, 100, '优'), (87.5, 94.5, '良'), (78.5, 87.5, '合格'), (YANGH_MIN, 78.5, '不合格')],
	'zhiljqt' : [(94.0, 100, '优'), (85.5, 94, '良'), (76.5, 85.5, '合格'), (YANGH_MIN, 76.5, '不合格')]
}
# 车行道养护状况评定等级标准
CHEXD_YANGH = {
	'kuaisl' : [(99, 100, '优'), (98, 99, '良'), (95, 98, '合格'), (YANGH_MIN, 95, '不合格')],
	'zhugl' : [(98.5, 100, '优'), (97, 98.5, '良'), (93, 97, '合格'), (YANGH_MIN, 93, '不合格')],
	'cigl' : [(98, 100, '优'), (96, 98, '良'), (91, 96, '合格'), (YANGH_MIN, 91, '不合格')],
	'zhiljqt' : [(95, 100, '优'), (90, 95, '良'), (85, 90, '合格'), (YANGH_MIN, 85, '不合格')]
}
# 车行道病害录入
CHEXD_DISEASE = [
	('liqlm', '沥青路面',
				[('lief', '裂缝'), ('suil', '碎裂'), ('songs', '松散'), ('tuop', '脱皮'),
				('kengc', '坑槽等'), ('jingkgc', '井框高差'), ('chez', '车辙'), ('chenx', '沉陷'),
				('yongb', '拥包'), ('cuobbl', '搓板或波浪'), ('fangj', '翻浆'), ('jij', '唧浆')]),
	('shuinlm', '水泥路面',
				[('lief', '裂缝'), ('suil', '碎裂'), ('duanl', '断裂'), ('tuop', '脱皮'),
				('kengc', '坑槽等'), ('jingkgc', '井框高差'), ('chenx', '沉陷'), ('jij', '唧浆'),
				('fenlss', '缝料散失'), ('cuot', '错台')])
]
# 车行道破损换算系统K值
CHEXD_DESTROY_K = {
	'liqlm' : {
		'lief' : 0.5,
		'suil' : 1,
		'songs' : 1,
		'tuop' : 1,
		'kengc' : 3,
		'jingkgc' : 3,
		'chez' : 0.5,
		'chenx' : 3,
		'yongb' : 2,
		'cuobbl' : 2,
		'fangj' : 6,
		'jij' : 6
	},
	'shuinlm' : {
		'lief' : 3,
		'suil' : 3,
		'duanl' : 10,
		'tuop' : 1,
		'kengc' : 3,
		'jingkgc' : 3,
		'chenx' : 3,
		'jij' : 6,
		'fenlss' : 2,
		'cuot' : 6,
	}
}
# 路龄系数
CHEXD_LULXS = [(0, 1, 1), (1, 5, 0.9), (6, 10, 0.8), (11, 15, 0.7)]

# 人行道养护状况评定等级标准
RENXD_YANGH = [(98, 100, '优'), (96, 98, '良'), (91, 96, '合格'), (YANGH_MIN, 91, '不合格')]
# 人行道病害录入
RENXD_DISEASE = [('kengd', '坑洞'), ('cuot', '错台'), ('gongq', '拱起'), ('chenx', '沉陷')]

# 路基与排水设施养护状况评定等级标准
LUJPAIS_YANGH = [(90, 100, '优'), (75, 90, '良'), (60, 75, '合格'), (YANGH_MIN, 60, '不合格')]
# 路基和排水设施病害录入
LUJPAIS_DISEASE = [
	('luj', '路基', [('buzcg', '不整,冲沟'), ('bianpps', '边坡破损'), ('gouzwsh', '构筑物损坏')]),
	('pais', '排水设施', [('pos', '破损'), ('yus', '淤塞')])
]
# 路基和排水设施病害系数
LUJPAIS_YANGH_FACTOR = {
	'luj' : {
		'buzcg' : 5,
		'bianpps' : 5,
		'gouzwsh' : 10,
	},
	'pais' : {
		'pos' : 5,
		'yus' : 10
	}
}

# 其他设施养护状况评定等级标准
OTHER_YANGH = [(90, 100, '优'), (75, 90, '良'), (60, 75, '合格'), (YANGH_MIN, 60, '不合格')]
# 其他设施病害录入
OTHER_DISEASE = [
	('fusjgw', '附属结构物', [('bianx', '变形'), ('pos', '破损'), ('gongnsx', '功能失效')]),
	('fusss', '附属设施', [('pos', '破损'), ('gongnsx', '功能失效')])
]
# 其他设施养护状况病害系数
OTHER_YANGH_FACTOR = {
	'fusjgw' : {
		'bianx' : 5,
		'pos' : 5,
		'gongnsx' : 10,
	},
	'fusss' : {
		'pos' : 5,
		'gongnsx' : 10
	}
}

# 维修单价
WEIXIU_MONEY = {
	'铣刨补修4cm (单位: ㎡)': 143,
	'铣刨补修5cm (单位: ㎡)': 164,
	'铣刨补修5cm加多米克斯 (单位: ㎡)': 182,
	'铣刨补修10cm(6粗+4细) (单位: ㎡)': 296,
	'铣刨补修15cm(10粗+5细) (单位: ㎡)': 437,
	'铣刨补修20cm(15粗+5细) (单位: ㎡)': 540,
	'开槽补修40cm(35cm粗+5cm细) (单位: ㎡)': 796,
	'补死坑（冷拌料4cm+运输) (单位: ㎡)': 166,
	'补死坑（冷拌料5cm+运输) (单位: ㎡)': 203,
	'补死坑（冷拌料10cm+运输) (单位: ㎡)': 421,
	'封裂缝 (单位: ㎡)': 36,
	'修补井圈 (单位: ㎡)': 854,
	'铣铀包 (单位: ㎡)': 76,
	'调整路缘石（青石） (15*30*74+运输) (单位: m)': 13,
	'调整路缘石（混凝土）(15*30*74+运输) (单位: m)': 11,
	'更换路缘石（青石） (15*30*74+运输) (单位: m)': 92,
	'更换路缘石（混凝土）(15*30*74+运输) (单位: m)': 54,
	'更换路缘石（花岗岩）(15*30*74+运输) (单位: m)': 132,
	'更换路缘石（花岗岩）(25*30*100+运输）\中山路 (单位: m)': 194,
	'更换平石(花岗岩）  (10*30*74+运输) (单位: m)': 101,
	'更换平石(混凝土）  (10*30*74+运输) (单位: m)': 45,
	'便道翻修（翻修砖) (单位: ㎡)': 63,
	'便道翻修（15cm碎石+2cm砂垫层+6cm砖+运输) (单位: ㎡)': 134,
	'便道整修 (单位: ㎡)': 41,
	'泼油洒沙 (单位: ㎡)': 13
}
