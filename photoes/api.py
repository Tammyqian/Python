# -*- coding:utf-8 -*-
import tornado
from kpages import url, ContextHandler
import uuid, time,os

@url(r'/api/upload/img')
class UploadImgHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        self.render('test/photo.html')

    def post(self):
        '''
        上传图片
        '''
        files = self.request.files
        if not files: return
        # print files
        f = self.request.files['newImg'][0]
        body = f.pop('body')
        fid_name = f.pop('filename','')
        # fid = self.get_argument('fid',uuid.uuid1())
        new_fid = 'static/img/' + fid_name
        with open(new_fid,'wb') as f:
            f.write(body)

        self.write(dict(status = True,fid=fid_name))


@url(r'/api/delete/img')
class DeleteImgHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        self.render('test/delete_photo.html')

    def post(self):
        '''
        删除setting配置文件MONTH值之前的static/img目录下的图片
        1.找到所求目录
        2.遍历该目录下的文件，得到每个文件的生成时间
        3.与time.time()做比较（以相同的比较格式）
        '''
        ts = time.time()
        path_dir = 'static/img/'
        for fle in os.listdir(path_dir):
            if not fle: break
            fid_ts = os.path.getctime(path_dir+fle)
            if fid_ts < ts - 3600 * 24 * 30 * __conf__.MONTH:
                os.remove(path_dir+fle)

        self.write(dict(status=True))

@url(r'/api/getimg')
class GetimgHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        '''
        显示图片
        1.获取参数查询的文件名
        2.通过文件名找到文件
        3.读取文件内容
        4.输出文件
        '''
        fid = self.get_argument('fid','')
        if not fid: return
        path = 'static/img/' + fid
        with open(path,'rb')as f:
            res = f.read()
        self.set_header("Content-Type", "image/jpeg/png")
        self.write(res)

