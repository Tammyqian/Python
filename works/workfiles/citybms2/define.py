#encoding=utf-8

#MQTT 报警 topic
ALARM_MSG = lambda uto: "MQTT/ALARM/{}".format(uto)
BRIDGE_TYPE = [
    {'name':u'默认类型(BCI评分)','key':'other_b','index':0,'desc':'梁式桥、桁架桥、刚构桥、悬臂+挂梁'},
    {'name':'拱桥(BCI评分)','key':'arch_b','index':1,'desc':'拱桥'},
    {'name':u'人行天桥(BCI评分)','key':'pedt_b','index':2,'desc':'人行天桥'},
    {'name':u'人行地下通道(PUCI评分)','key':'under_way','index':3,'desc':'人行地下通道'}
    ]
BRIDGE_TYPE_DESC = {0:'梁式桥、桁架桥、刚构桥、悬臂+挂梁',1:'拱桥',2:'人行天桥',3:'人行地下通道'}
STRUCT_TYPE = [("desk", "桥面系"), ("span", "桥跨"), ("pier", "桥墩"), ("abutment", "桥台")]
LOCATION = {'0': '桥面系','1':'上部结构','2':'下部结构','3':'主体构造物','4':'出入口','5':'道面','6':'排水设施','7':'附属设施'}
LOCNORMAL = {'0': '桥面系','1':'上部结构','2':'下部结构'}
LOCSUB = {'3':'主体构造物','4':'出入口','5':'道面','6':'排水设施','7':'附属设施'}
LOCATIONS = [{'k':'0','v':'桥面系'},{'k':'1','v':'上部结构'},{'k':'2','v':'下部结构'}]
DILOCATIONS = [{'k':'3','v':'主体构造物'},{'k':'4','v':'出入口'},{'k':'5','v':'道面'},{'k':'6','v':'排水设施'},{'k':'7','v':'附属设施'}]
#BCI 评级
YANGHLB = {(90, 100.000000001):   {'text': u"A级", 'status': u'完好',  'class': 'badge badge-success'},
            (80, 90): {'text': u"B级", 'status': u'良好', 'class': 'badge badge-info'},
            (66, 80): {'text': u"C级", 'status': u'合格', 'class': 'badge badge-warning'},
            (50, 66): {'text': u"D级", 'status': u'不合格', 'class': 'badge badge-primary'},
            (-100, 50): {'text': u"E级", 'status': u'危险', 'class': 'badge badge-danger'}}

BCI_LB = [u'A级', u'B级', u'C级', u'D级', u'E级', u'合格', u'不合格', u'无评级']
#需要进行养护的工程类别
GONGCLB = ['养护维修(小修)', '大中修', '改扩建']

XUNJ_LEVEL = ['轻','中','重']

XUNJ_COUNT = 30
XUNJZQ = {'1': '1天一巡', '3': '3天一巡', '7': '7天一巡'}

BRIDGE_MARK = {'0': '长大桥梁', '1': '特殊结构', '2': '高危桥梁'}

DISEASE_STATUS = [('0', '病害发生'), ('1', '已处置'), ('2', '已维修')]

#0到6，星期天为0
WEEK = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '0': '日'}

# 缩略图设置
IMG_SIZE = {'0': (80, 80), '1': (150, 150), '2': (300, 300)}
IMG_SCOPE = {'0': '桥梁文件档案', '1': '病害描述'}
'''
                    ('qlsbjg','梁桥和拱桥上部结构',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('duntai','墩台',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('zbyq','锥坡、翼墙',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('lsds','拉索/吊索',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('qiaotagong','桥面以上的塔、拱',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('qiaobmz','桥面铺装',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('shengszz','伸缩装置',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('paisss','排水设施',['完整', '不完整'],'缺损 (块)', 'n'),
                    ('qiaoqsg', '桥、桥区施工', ['无', '有'], '是否违章', '*'),
                    ('qiaolaq', '桥梁安全运行情况', ['良好', '一般', '较差', '很差'], '', ''),
'''

XUNJIAN_PROJECT_TIME = 1407910620.874131
XUNJIAN_PROJECT = [
                    ('qiaomp','桥名牌', ['完整', '不完整'], '缺损(块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('duntai','墩台',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('zbyq','锥坡、翼墙',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('lsds','拉索/吊索',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('xiangpzp','限高牌、限载牌', ['完整', '不完整'], '缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaotagong','桥面以上的塔、拱',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaobmz','桥面铺装',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('chexd','车行道', ['平整', '不平整'], '坑塘(m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('renxd','人行道', ['平整', '不完整'], '坑塘(m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('shensf','伸缩缝', ['完整', '不完整'], '缺损(m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('shengszz','伸缩装置',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('lang','栏杆', ['完整', '不完整'], '缺损(m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('paisss','排水设施', ['完整', '不完整'], '缺损(块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('duanz', '端柱',  ['完整', '不完整'], '缺损 (只)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('xianzp', '限载牌',  ['完整', '不完整'], '缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaoluljwz','桥路连接位置',['完整', '不完整'],'缺损(m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('jifeigll','机非隔离栏', ['完整', '不完整'], '缺损(m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('qlsbjg','梁桥和拱桥上部结构',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('shangbujg', '上部结构',['完整', '不完整'],'缺损(处)','n', "损坏类型", "损坏程度", "损坏位置"),
                    ('xiabujg','下部结构',['完整', '不完整'],'缺损(处)','n', "损坏类型", "损坏程度", "损坏位置"),
                    ('zhizuo','支座',['完整', '不完整'],'缺损(m²)','n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('jifgll', '机非隔离栏',  ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('xiesk', '泄水孔',  ['畅通', '不畅通'], '堵塞(只)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('fut', '扶梯', ['完整', '不完整'], '缺损 (m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('shipz', '声屏障', ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('baohuqushg','桥梁保护区施工', ['无', '有'], '是否违章', '*', "损坏类型", "损坏程度",'施工位置'),
                    ('qiaoqsg', '桥、桥区施工', ['无', '有'], '是否违章', '*', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaolaq', '桥梁安全运行情况', ['良好', '一般', '较差', '很差'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('meiqg_gaoyx', '桥上架设煤气管线或高压线', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('guangp_qita', '设广告牌或者其它挂浮物', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('jiansjzw', '桥梁保护区内建设建筑物、构筑物', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('other','其他危及行车、行船、行人安全的病害', ['无', '有'], '', '*', "损坏类型", "损坏程度", '病害位置'),
                    ('wajjk', '桥梁保护区内挖掘基坑、建筑打桩、地下管道顶进、河道疏浚、爆破、堆载等', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ]

XUNJIAN_PROJECT_OLD = [
                    ('qlsbjg','梁桥和拱桥上部结构',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('duntai','墩台',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('zbyq','锥坡、翼墙',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('lsds','拉索/吊索',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaotagong','桥面以上的塔、拱',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaobmz','桥面铺装',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('shengszz','伸缩装置',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('paisss','排水设施',['完整', '不完整'],'缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaomp', '桥名牌',  ['完整', '不完整'], '缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('xianzp', '限载牌',  ['完整', '不完整'], '缺损 (块)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('lang', '栏杆',  ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('duanz', '端柱',  ['完整', '不完整'], '缺损 (只)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('renxd', '人行道',  ['平整', '不平整'], '坑塘(m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('chexd', '车行道',  ['平整', '不平整'], '坑塘(m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('jifgll', '机非隔离栏',  ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('shensf', '伸缩缝',  ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('xiesk', '泄水孔',  ['畅通', '不畅通'], '堵塞(只)', 'n', "损坏类型", "损坏程度", "损坏位置"),
                    ('fut', '扶梯', ['完整', '不完整'], '缺损 (m²)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('shipz', '声屏障', ['完整', '不完整'], '缺损 (m)', 'n|/^(\d*\.)?\d+$/', "损坏类型", "损坏程度", "损坏位置"),
                    ('wajjk', '桥梁保护区内挖掘基坑、建筑打桩、地下管道顶进、河道疏浚、爆破、堆载等', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('jiansjzw', '桥梁保护区内建设建筑物、构筑物', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('meiqg_gaoyx', '桥上架设煤气管线或高压线', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('guangp_qita', '设广告牌或者其它挂浮物', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaoqsg', '桥、桥区施工', ['无', '有'], '是否违章', '*', "损坏类型", "损坏程度", "损坏位置"),
                    ('qiaolaq', '桥梁安全运行情况', ['良好', '一般', '较差', '很差'], '', '', "损坏类型", "损坏程度", "损坏位置"),
                    ('other', '其他危及行车、行船、行人安全的病害', ['无', '有'], '', '', "损坏类型", "损坏程度", "损坏位置")
                    ]

Template_QingKuang = {
        u"地区": "postcode_name",
        u"特大桥": "tedq",
        u"大桥": "daq",
        u"中桥": "zhongq",
        u"小桥": "xiaoq",
        u"总桥长": "zongqc",
        u"合格": "heg",
        u"不合格": "buhg",
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        u"发现隐患数": "disease_count",
        u"消除隐患数": "done_disease_count"
}


Template_Bridge_YiLanBiao = {
        u"编号": "no",
        u"桥名": 'name',
        u"地点": "postcode_name",
        u"全长": "qiaolzc",
        u"净宽": "qiaolzk",
        u"跨径": "zuidkj",
        u"孔数": "span",
        u"面积": "qiaommj",
        u"设计荷载": "shejhz_name",
        u"梁底标高": "liangdbg",
        u"建造年代": "jianzny",
        u"是否通航": "",
        u"上部结构": "zhulxs",
        u"下部结构": ['qiaodxs_name', 'qiaotxs_name'],
        u"备注": "remark",
}

SORT_COLUMN = ['postcode', 'yanghlb', "qiaolzt","kuajfl","yongtfl", "yanghdj","daoldj", "xunjzq", "jiansdw","shejdw","jianldw","shigdw","jianzny","bridgetype", "guanldw", "shejhz", "kangzld","yanghdw","span","tonghdj","qiaommj","qiaolzc","qiaolzk", 'bci_score','bci_score_level','no']

SEARCH_COLUMN = [
    ("桥梁识别数据", [
        (u"桥梁名称", "name", "input", {"datatype":"*"}),
        (u"地区", "postcode", "select", {}),
        (u"桥梁状态", "qiaolzt", "select", {}),
        (u"特殊标注","mark", "select", {}),
        (u"跨径分类", "kuajfl", "select", {}),
        (u"用途分类", "yongtfl", "select", {}),
        (u"运营期限", "yunyqx", "select", {}),
        (u"所在路名", "suozlm", "input", {}),
        (u"所跨地物名称", "suokdwmc", "input", {}),
        (u"道路等级", "daoldj", "select", {}),
        (u"养护类别","yanghlb", "select", {}),
        (u"养护等级","yanghdj", "select", {}),
        (u"巡检周期","xunjzq", "select", {}),
        (u"最大跨径","zuidkj", "input", {}),
        (u"设计单位","shejdw", "input", {}),
        (u"桥梁跨数","span", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"个"}),
        (u"通航等级","tonghdj", "select", {}),
        (u"管理单位","guanldw", "select", {}),
        (u"结构类型","bridgetype", "select", {}),
        (u"建造年月","jianzny", "input", {}),
        (u"养护单位","yanghdw", "select", {}),
        (u"抗震烈度","kangzld", "select", {}),
        (u"设计荷载","shejhz", "select", {}),
        (u"监理单位","jianldw", "input", {}),
        (u"跨径组合","kuajzh", "input", {}),
        (u"桥梁总宽","qiaolzk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"施工单位","shigdw", "input", {}),
        (u"桥面面积","qiaommj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m²"}),
        (u"桥梁总长","qiaolzc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"建设单位","jiansdw", "input", {}),
        (u"车行道净宽","chexdjk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限宽","chexdxk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限高","chexdxg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限重","chexdxz", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"吨"}),
        (u"人行道净宽","renxdjk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        #(u"结构简图","jiegjt", "input", {}),
        #(u"实景照片","shijzp", "input", {}),
        (u"桥梁编号","no", "input", {})
    ]),
    ("上部结构与桥面系", [
        (u"主梁型式","zhulxs", "input", {}),
        (u"主梁尺寸","zhulcc", "input", {"datatype":"/^(\d+\.\d+)\,(\d+\.\d+)\,(\d+\.\d+)$/", "placeholder":"长，宽，高"}),
        (u"主梁数量","zhulsl", "input", {"datatype":"n"}),
        (u"横梁型式","henglxs", "input", {}),
        (u"支座型式","zhizxs", "input", {}),
        (u"行车道铺装材料","xingcdpzcl", "input", {}),
        (u"桥面结构","qiaomjg", "input", {}),
        (u"伸缩缝型式","shensfxs", "input", {}),
        (u"伸缩缝数量","shensfsl", "input",{"datatype":"n", "unit":"条"}),
        (u"桥面标高","qiaombg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"梁底标高","liangdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"主桥纵坡","zhuqzp", "input", {"unit":"%"}),
        (u"主桥横坡","zhuqhp", "input", {"unit":"%"}),
        (u"引桥纵坡","yinqzp", "input", {"unit":"%"})
    ]),

    ("下部结构(桥墩)", [
        (u"桥墩型式","qiaodxs", "input", {}),
        (u"桥墩标高","qiaodbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"盖梁尺寸","qiaodglcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基底标高","qiaodjdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"底板尺寸","qiaoddbcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基桩尺寸","qiaodjzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
    ]),
    ("下部结构(桥台)", [
        (u"桥台型式","qiaotxs", "input", {}),
        (u"桥台标高","qiaotbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基底标高","qiaotjdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"台帽尺寸","qiaottmcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"底板尺寸","qiaotdbcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基桩尺寸","qiaotjzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"挡土板厚度","qiaotdtbhd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"翼墙型式","qiaotyqxs", "input", {}),
        (u"翼墙长度","qiaotyqcd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
    ]),

    # 新添加:

    ("人行天桥", [
        (u"人行天桥净空", "renxtqjk", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"人行天桥限重", "renxtqxz", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "吨"}),
        (u"支座型式", "zhizxs", "input", {}),
        (u"支座数量", "zhizsl", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "个"}),
        (u"梯道侧面及顶面外装", "tidcmjdmbz", "input", {}),
        (u"引道及踏步", "yindjtb", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"排水管", "paosg", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"管线位置", "guanxwz", "input", {}),
        (u"主跨及立柱外装", "zhukjlzwg", "input", {}),
        (u"梯道防滑条", "tidfht", "input", {})
    ]),

    ("人行地下通道", [
        (u"出入口限高", "churkxg", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"出入口数量", "churksl", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "个"}),
        (u"通道长度", "tongdcd", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"通道宽度", "tongdkd", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"主通道结构", "zhutdjg", "input", {}),
        (u"梯道结构", "tidjg", "input", {}),
        (u"衬砌结构", "chenqjg", "input", {}),
        (u"挡墙结构", "dangqjg", "input", {}),
        (u"板间铰缝", "banjjf", "input", {}),
        (u"通道板间铰缝", "tongdbjjf", "input", {}),
        (u"侧墙间伸缩缝", "ceqjssf", "input", {}),
        (u"道面数", "decknum", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "个"}),
        (u"踏步（平台）", "tab", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"坡道", "pod", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"内墙装饰", "neiqzs", "input", {}),
        (u"外墙装饰", "waiqzs", "input", {}),
        (u"集水井", "jisj", "input", {}),
        (u"通道内照明", "tongdnzm", "input", {}),
        (u"帽石", "maos", "input", {}),
        (u"雨棚", "yup", "input", {}),
    ]),


    ("附属工程", [
        (u"栏杆总长","langzc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"栏杆结构","langjg", "input", {}),
        (u"端柱尺寸","duanzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"护岸类型","hualx", "input", {}),
        (u"引坡挡墙类型","yinpdqlx", "input", {})
    ]),
    ("附挂管线", [
        (u"桥左侧附挂管线","jisg", "input", {}),
        (u"中分带附挂管线","ranqg", "input", {}),
        (u"右侧附挂管线","dianll", "input", {}),
        #(u"给水管","jisg", "input", {}),
        #(u"燃气管","ranqg", "input", {}),
        #(u"电力缆","dianll", "input", {}),
        #(u"通讯电缆","tongxdl", "input", {})
    ]),
    ("技术状况(BCI)", [
        (u'桥面系', 'bsi_deck', "text", {}),
        (u'桥面系等级', 'bsi_deck_level', "text", {}),
        (u'上部结构', 'bsi_upside', "text", {}),
        (u'上部结构等级', 'bsi_upside_level', "text", {}),
        (u'下部结构', 'bsi_substruction', "text", {}),
        (u'下部结构等级', 'bci_substruction_level', "text", {}),
        (u'全桥', 'bci_score', "text", {}),
        (u'全桥评级', 'bci_score_level', "text", {}),
        (u'完好状况', 'bci_score_status', "text", {}),
    ]),
    ("技术状况(BSI)", [
        (u'桥面系', 'bsi_deck', "text", {}),
        (u'桥面系等级', 'bsi_deck_level', "text", {}),
        (u'上部结构', 'bsi_upside', "text", {}),
        (u'上部结构等级', 'bsi_upside_level', "text", {}),
        (u'下部结构', 'bsi_substruction', "text", {}),
        (u'下部结构等级', 'bsi_substruction_level', "text", {}),
        (u'全桥', 'bsi_score', "text", {}),
        (u'全桥评级', 'bsi_score_level', "text", {}),
        (u'完好状况', 'bsi_score_status', "text", {})
    ]),("技术状况(PUCI)", [
        (u'全桥PUCI评分', 'puci_score', "text", {}),
        (u'全桥PUCI评级', 'puci_score_level', "text", {}),
        (u'PUCI完好状况', 'puci_score_status', "text", {})
    ])
]

SEARCH_COLUMN_PUCI = [
    ("桥梁识别数据", [
        (u"桥梁名称", "name", "input", {"datatype":"*"}),
        (u"地区", "postcode", "select", {}),
        (u"桥梁状态", "qiaolzt", "select", {}),
        (u"特殊标注","mark", "select", {}),
        (u"跨径分类", "kuajfl", "select", {}),
        (u"用途分类", "yongtfl", "select", {}),
        (u"运营期限", "yunyqx", "select", {}),
        (u"所在路名", "suozlm", "input", {}),
        (u"所跨地物名称", "suokdwmc", "input", {}),
        (u"道路等级", "daoldj", "select", {}),
        (u"养护类别","yanghlb", "select", {}),
        (u"养护等级","yanghdj", "select", {}),
        (u"巡检周期","xunjzq", "select", {}),
        (u"最大跨径","zuidkj", "input", {}),
        (u"设计单位","shejdw", "input", {}),
        (u"桥梁跨数","span", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"个"}),
        (u"通航等级","tonghdj", "select", {}),
        (u"管理单位","guanldw", "select", {}),
        (u"结构类型","bridgetype", "select", {}),
        (u"建造年月","jianzny", "input", {}),
        (u"养护单位","yanghdw", "select", {}),
        (u"抗震烈度","kangzld", "select", {}),
        (u"设计荷载","shejhz", "select", {}),
        (u"监理单位","jianldw", "input", {}),
        (u"跨径组合","kuajzh", "input", {}),
        (u"桥梁总宽","qiaolzk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"施工单位","shigdw", "input", {}),
        (u"桥面面积","qiaommj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m²"}),
        (u"桥梁总长","qiaolzc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"建设单位","jiansdw", "input", {}),
        (u"车行道净宽","chexdjk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限宽","chexdxk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限高","chexdxg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"车行道限重","chexdxz", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"吨"}),
        (u"人行道净宽","renxdjk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        #(u"结构简图","jiegjt", "input", {}),
        #(u"实景照片","shijzp", "input", {}),
        (u"档案编号","no", "input", {}),

    ]),
    ("上部结构与桥面系", [
        (u"主梁型式","zhulxs", "input", {}),
        (u"主梁尺寸","zhulcc", "input", {"datatype":"/^(\d+\.\d+)\,(\d+\.\d+)\,(\d+\.\d+)$/", "placeholder":"长，宽，高"}),
        (u"主梁数量","zhulsl", "input", {"datatype":"n"}),
        (u"横梁型式","henglxs", "input", {}),
        (u"支座型式","zhizxs", "input", {}),
        (u"行车道铺装材料","xingcdpzcl", "input", {}),
        (u"桥面结构","qiaomjg", "input", {}),
        (u"伸缩缝型式","shensfxs", "input", {}),
        (u"伸缩缝数量","shensfsl", "input",{"datatype":"n", "unit":"条"}),
        (u"桥面标高","qiaombg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"梁底标高","liangdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"主桥纵坡","zhuqzp", "input", {"unit":"%"}),
        (u"主桥横坡","zhuqhp", "input", {"unit":"%"}),
        (u"引桥纵坡","yinqzp", "input", {"unit":"%"})
    ]),

    ("下部结构(桥墩)", [
        (u"桥墩型式","qiaodxs", "input", {}),
        (u"桥墩标高","qiaodbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"盖梁尺寸","qiaodglcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基底标高","qiaodjdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"底板尺寸","qiaoddbcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基桩尺寸","qiaodjzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
    ]),
    ("下部结构(桥台)", [
        (u"桥台型式","qiaotxs", "input", {}),
        (u"桥台标高","qiaotbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基底标高","qiaotjdbg", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"台帽尺寸","qiaottmcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"底板尺寸","qiaotdbcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"基桩尺寸","qiaotjzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"挡土板厚度","qiaotdtbhd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"翼墙型式","qiaotyqxs", "input", {}),
        (u"翼墙长度","qiaotyqcd", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"})
    ]),
    ("人行地下通道", [
        (u"出入口限高", "churkxg", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"出入口数量", "churksl", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "个"}),
        (u"通道长度", "tongdcd", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"通道宽度", "tongdkd", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"主通道结构", "zhutdjg", "input", {}),
        (u"梯道结构", "tidjg", "input", {}),
        (u"衬砌结构", "chenqjg", "input", {}),
        (u"挡墙结构", "dangqjg", "input", {}),
        (u"板间铰缝", "banjjf", "input", {}),
        (u"通道板间铰缝", "tongdbjjf", "input", {}),
        (u"侧墙间伸缩缝", "ceqjssf", "input", {}),
        (u"道面数", "decknum", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "个"}),
        (u"踏步（平台）", "tab", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"坡道", "pod", "input", {"datatype": "/^-?\d+\.\d+$/|n", "unit": "m"}),
        (u"内墙装饰", "neiqzs", "input", {}),
        (u"外墙装饰", "waiqzs", "input", {}),
        (u"集水井", "jisj", "input", {}),
        (u"通道内照明", "tongdnzm", "input", {}),
        (u"帽石", "maos", "input", {}),
        (u"雨棚", "yup", "input", {}),
    ]),


    ("附属工程", [
        (u"栏杆总长","langzc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"栏杆结构","langjg", "input", {}),
        (u"端柱尺寸","duanzcc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"护岸类型","hualx", "input", {}),
        (u"引坡挡墙类型","yinpdqlx", "input", {})
    ]),
    ("附挂管线", [
        (u"桥左侧附挂管线","jisg", "input", {}),
        (u"中分带附挂管线","ranqg", "input", {}),
        (u"右侧附挂管线","dianll", "input", {}),
        #(u"给水管","jisg", "input", {}),
        #(u"燃气管","ranqg", "input", {}),
        #(u"电力缆","dianll", "input", {}),
        #(u"通讯电缆","tongxdl", "input", {})
    ]),
    ("技术状况(PUCI)", [
        (u'主体构造物', 'puci_zhutigzw', "text", {}),
        (u'主体构造物等级', 'puci_zhutigzw_level', "text", {}),
        (u'排水设施', 'puci_paishuiss', "text", {}),
        (u'排水设施等级', 'puci_paishuiss_level', "text", {}),
        (u'附属设施', 'puci_fushuss', "text", {}),
        (u'附属设施等级', 'puci_fushuss_level', "text", {}),
        (u'道面', 'puci_daom', "text", {}),
        (u'道面等级', 'puci_daom_level', "text", {}),
        (u'出入口', 'puci_churuk', "text", {}),
        (u'出入口等级', 'puci_churuk_level', "text", {}),
        (u'全桥', 'puci_score', "text", {}),
        (u'全桥评级', 'puci_score_level', "text", {}),
        (u'完好状况', 'puci_score_status', "text", {})
    ])#
]


BASE_BRIDGE_INFO = [
        (u"地区", "postcode", "select", {}),
        (u"所在路名", "suozlm", "input", {}),
        (u"所跨地物名称", "suokdwmc", "input", {}),
        (u"设计荷载","shejhz", "select", {}),
        (u"建造年月","jianzny", "input", {}),
        (u"桥梁总长","qiaolzc", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"桥梁总宽","qiaolzk", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m"}),
        (u"桥面面积","qiaommj", "input", {"datatype":"/^-?\d+\.\d+$/|n", "unit":"m²"}),
        (u"最大跨径","zuidkj", "input", {}),
        (u"结构类型","bridgetype", "select", {}),
        (u"桥梁规模","qiaolgm", "input", {}),
        (u"养护类别","yanghlb", "select", {}),
        (u"养护等级","yanghdj", "select", {}),
        (u"巡检周期","xunjzq", "select", {}),
        (u"管理单位","guanldw", "select", {}),
        (u"养护单位","yanghdw", "select", {})
    ]

#多桥自定义表单
DOUBLE_BRIDGE_1 = SEARCH_COLUMN[0][1]
DOUBLE_BRIDGE_2 =[(u"桥梁编号", "no", "input", {"datatype":"*"}), (u"桥梁名称", "name", "input", {"datatype":"*"})]+ SEARCH_COLUMN[1][1]
DOUBLE_BRIDGE_3 = [(u"桥梁编号", "no", "input", {"datatype":"*"}), (u"桥梁名称", "name", "input", {"datatype":"*"})]+ SEARCH_COLUMN[2][1] + SEARCH_COLUMN[3][1] + SEARCH_COLUMN[4][1] + SEARCH_COLUMN[5][1]
DOUBLE_BRIDGE_4 = [(u"桥梁编号", "no"),
                    (u"桥梁名称", "name"),
                    (u'定期检查时间', 'end'),
                    (u'检测单位', 'company_name'),
                    (u'桥面系BCI', 'bci_deck'),
                    (u'桥面系等级', 'bci_deck_level'),
                    (u'上部结构BCI', 'bci_upside'),
                    (u'上部结构等级', 'bci_upside_level'),
                    (u'下部结构BCI', 'bci_substruction'),
                    (u'下部结构等级', 'bci_substruction_level'),
                    (u'全桥BCI', 'bci_score'),
                    (u'全桥评级', 'bci_score_level'),
                    (u'完好状况', 'bci_score_status'),
                    (u'需要进行养护的工程类别', 'gongclb')]

DOUBLE_BRIDGE_5 = [(u'桥梁编号', 'no'),
                    (u'桥梁名称', 'bridge_name'),
                    (u'病害类型', 'diseasetype_name'),
                    (u'病害描述', 'content'),
                    (u'维修时间', 'weixrq'),
                    (u'维修类型', 'type_name'),
                    (u'维修单位', 'company_name'),
                    (u'维修内容', 'weixnr'),
                    (u'处置情况', 'chuzqk'),
                    (u'维护费用', 'weihfy'),
                    (u'质量状况', 'zhilzk'),
                    (u'观测责任人', 'guanczrr')
                    ]


INIT_CONSOLE = ['module-card-0', 'module-qiaolgy', 'module-dingjgz', 'module-xunjgz']
MODULE_CONSOLE = [('module-card-0', '大信息卡'),
                    ('module-card-1', '小信息卡'),
                    ('module-qiaolgy', '桥梁管养工作统计'),
                    ('module-qiaolfb', '桥梁分布情况 '),
                    ('module-dingjgz', '定检工作统计 '),
                    ('module-xunjgz', '巡检工作统计 ')]


COLORS = ['#D03434','#248BC7','#323B48',
          '#22B190' ,'#a842ca','#5FAB0C',
          '#E65E0E','#4252ca','#CAAC1E',
          '#95a5d8' ,'#42cab8','#ca9542',
          '#42ca82','#42ca5f','#6fca42',
          '#4282ca' ,'#bcca42','#cab542',
          '#83BDAD','#ca7f42','#000',
          '#95d8a2' ,'#42a8ca','#8f0091',
          '#ca429f','#d895be','#d8d195',
          '#ca4275','#3f4340','#8e320d']
