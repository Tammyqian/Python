# -*- coding:utf-8 -*-
"""
    author comger@gmail.com
    利用深度学习评估监测数据
"""
import os
import csv
import cPickle
import numpy as np

from kpages import app_path,get_context
from keras.models import Sequential,model_from_json
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

from nameko.dependency_providers import Config
from nameko.rpc import rpc
from mongo_util import MongoIns

class AiService:
    name = "aiService"

    # 配置文件
    config = Config()

    @rpc
    def create_mode(self, mode_name, train_x, train_y, input_num, output_num, check_rate=0.1):
        model = Sequential()
        
        o = input_num*output_num
        model.add(Dense(o, input_dim=input_num,activation='tanh'))
        model.add(Dense(o, init='uniform'))
        model.add(Activation('tanh'))
        #model.add(Dense(output_num, input_dim=o, activation='linear'))
        if output_num>1:
            model.add(Dense(output_num, input_dim=o, activation='linear'))
        else:
            model.add(Dense(output_num, input_dim=o, activation='sigmoid'))

        sgd = SGD(lr=0.5, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='mse', optimizer=sgd,metrics=["accuracy"])

        total = len(train_x)
        c_s = int(total*check_rate)
        t_s = total-c_s

        model.fit(train_x[0:t_s,:], train_y[0:t_s,:], nb_epoch=1000,validation_split=check_rate*100, batch_size=32, verbose=1)

        score = model.evaluate(train_x[t_s:total,:], train_y[t_s:total,:], batch_size=c_s)

        gfs = get_context().get_gfs()
        gfs.delete(mode_name)
        gfs.put(cPickle.dumps(model),_id=mode_name)
        #fpath = app_path('static/ai/{0}'.format(mode_name))
        #cPickle.dump(model,open(fpath,"wb"))

        '''    
        open(fpath,'w').write(model.to_json()) 
        model.save_weights('my_model_weights.h5') 
        '''
        return score,model

    @rpc
    def create_feature_mode(self):
        path = 'static/ai/files/feature.csv'
        reader = csv.reader(open(path, "rb"))
        inputs = []
        outputs  =[]

        for arr in reader:
            arr = map(float,arr)
            inputs.append(arr[0:4])
            outputs.append(arr[4:5])
        

        score, m =  create_mode('ai_feature_mode', np.asarray(inputs), np.asarray(outputs), 4, 1)
        return score,m

    @rpc
    def train(self, code_name, mode,input_num,output_num):
        try: 
            mode = 'ai-{0}'.format(mode)
            if code_name:
                mode = 'ai-{0}-{1}'.format(code_name,mode)
            
            mode_data = 'data-{}'.format(mode)
            gfs = get_context().get_gfs()
            f = gfs.get(mode_data)
            
            inputs = []
            outputs = []
            for i,arr in enumerate(f.read().split('\r\n')):
                arr = arr.split(',')
                try:
                    arr = map(float,arr)
                    inputs.append(arr[0:input_num])
                    outputs.append(arr[input_num:(input_num+output_num)])
                except:
                    pass

            score,m= create_mode(mode, np.asarray(inputs), np.asarray(outputs), input_num, output_num)
            return score,m
        except Exception as e:
            print '训练',mode,e
            return False,e.message

    @rpc
    def classify(self, code_name, mode, inputs):
        gfs = get_context().get_gfs()
        mode = 'ai-{0}'.format(mode)
        if code_name:
            pmode = 'ai-{0}-{1}'.format(code_name, mode)
            if gfs.exists(pmode):
                mode = pmode

        f = gfs.get(mode)
        if f:
            body = f.read()
            m = cPickle.loads(body)
        else:
            return ()

        return m.predict(np.asarray(inputs)).tolist()



    @rpc
    def feature_classify(self, inputs):
        """
            特征评估
        """
        gfs = get_context().get_gfs()
        mode = 'ai_feature_mode'
        if gfs.exists(mode):
            f = gfs.get(mode)
            m = cPickle.loads(f.read())
        else:
            score,m = create_feature_mode()

        return m.predict(np.asarray(inputs)).tolist()
