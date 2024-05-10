# 编写处理websocket的业务逻辑
import json
import os
import pickle
import random
from datetime import datetime

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.http import JsonResponse

from app01.models import sc

users=[]
History = {'demo':[]}
userList={}#roomNum:[在线的人]
channel_name_list={}

class ChatConsumer1(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()
        #获取群号
        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        users.append(username)######
        if group not in History:
            History[group] = []
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        async_to_sync(self.channel_layer.send)(self.channel_name, {"type": "getHistory", 'message': History[group]})




    def websocket_receive(self, message):
        msg = message['text']
        msg = msg.split(',')

        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #教师开启白板了，通知学生端全部开启白板
        if msg[0] == 'open':
            async_to_sync(self.channel_layer.group_send)(group, {"type": "openBoard", "message": {'msg':msg[0]}})
        elif msg[0] == 'close':
            async_to_sync(self.channel_layer.group_send)(group, {"type": "closeBoard", "message": {'msg':msg[0]}})
        elif msg[0] == 'over':
            async_to_sync(self.channel_layer.group_send)(group, {"type": "classover", "message": {'msg':msg[0]}})
        elif msg[0] == 'dianming':
            one = randomSelect(group)
            async_to_sync(self.channel_layer.group_send)(group, {"type": "dianming", "message": {'msg':one}})
        else:

            if msg[0] == 'clear':
                History[group] = []

            data = {
                'username': username,
                'message': msg,
                'timestamp': timestamp,
            }
            print(msg)
            History.setdefault(group, []).append(data)
            # 通知“1”组内所有的客户端，执行XX.oo方法，在此方法内可以执行任意的功能
            async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", "message": data})


    def websocket_disconnect(self, message):
        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        users.remove(username)
        if group in userList:
            userList[group].remove(username)
            async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)





    def getHistory(self,event):
        self.send(json.dumps({
            'kind': "history",
            'message': event['message'],
        }))


    def xx_oo(self,event):
        self.send(json.dumps({'kind':"message",
            'message': event['message']}))#给组内所有人回复

    def exit(self,event):
        self.send(json.dumps({'kind': "user",
                              'name': event['name']}))  # 给组内所有人回复

    def openBoard(self,event):
        self.send(json.dumps({'kind': "open",
                              'msg': event['message']}))  # 给组内所有人回复
    def closeBoard(self,event):
        self.send(json.dumps({'kind': "close",
                              'msg': event['message']}))  # 给组内所有人回复

    def classover(self,event):
        self.send(json.dumps({'kind': "over",
                              'msg': event['message']}))  # 给组内所有人回复

    def dianming(self,event):
        self.send(json.dumps({'kind': "dianming",'msg': event['message']['msg']}))  # 给组内所有人回复

def randomSelect(cid):
    students = sc.objects.filter(cid=cid)
    people=[]
    for i in students:
        people.append(i.stuName)
    one = random.sample(people,1)
    return one