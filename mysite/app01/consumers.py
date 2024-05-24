# 编写处理websocket的业务逻辑
import json
import os
import pickle
from datetime import datetime

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.http import JsonResponse

users=[]
chatHistory = {}
onlineHistory={}
userList={}#roomNum:[在线的人]
channel_name_list={}
room_list = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()
        #获取群号
        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        users.append(username)######


        '''每次重新建立socket连接的时候，都会把原来的close'''
        userList.setdefault(group, []).append(username)
        if group not in chatHistory:
            chatHistory[group] = []
        channel_name_list[username] = self.channel_name#为了在一个group里面找到@的人
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)#加入group
        async_to_sync(self.channel_layer.group_send)(group, {"type": "exit", "name": userList[group]})#更新group的用户列表
        async_to_sync(self.channel_layer.send)(self.channel_name,{"type":"getHistory",'message':chatHistory[group]})



    def websocket_receive(self, message):
        m = (json.loads(message['text']))
        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if m['kind'] == 'message':
            text =  m['text']
            data = {
                'username': username,
                'message': text,
                'timestamp': timestamp,
            }

            for i in range(len(text)):
                if text[i] == '@':
                    j = i + 1
                    while j < len(text) and text[j] != ' ':
                        j += 1
                    if text[i + 1:j] in userList[group]:
                        async_to_sync(self.channel_layer.send)(channel_name_list[text[i + 1:j]],
                                                               {"type": "personal", 'message': data})
                        # self.channel_layer.send(channel_name_list[text[i+1:j]], {"kind":"@",'message':data})

            chatHistory.setdefault(group, []).append(data)
            print(chatHistory)
            # 通知“1”组内所有的客户端，执行XX.oo方法，在此方法内可以执行任意的功能
            async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", "message": data})

        elif m['kind'] == 'createRoom':
            roomName = m['room']
            if roomName not in room_list:
                room_list.append(roomName)
                chatHistory[roomName] = []
                userList[roomName] = []

        else:
            roomName = m['room']
            del chatHistory[roomName]
            del userList[roomName]
            room_list.remove(roomName)

    def websocket_disconnect(self, message):
        group = self.scope['url_route']['kwargs'].get("group")
        username = self.scope['url_route']['kwargs'].get("username")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # onlineHistory[group][username].append(timestamp)
        '''删除聊天室之后，再加入新的聊天室的时候都会close，此时group不存在了'''
        users.remove(username)
        if group in userList:
            userList[group].remove(username)
            async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
            async_to_sync(self.channel_layer.group_send)(group, {"type": "exit", "name": userList[group]})





    def getHistory(self,event):
        self.send(json.dumps({
            'kind': "history",
            'message': event['message'],
        }))

    def deleteRoom(self,event):
        res = []
        for i in range(len(room_list)):
            res.append({"value": room_list[i]})
        self.send(json.dumps({
            'kind': "deleteroom",
            'message': res,
            'room':event['room']
        }))

    def Room(self,event):
        res=[]
        for i in range(len(room_list)):
            res.append({"value": room_list[i]})
        self.send(json.dumps({
            'kind': "room",
            'message':res
        }))
    def personal(self,event):
        self.send(json.dumps({
            'kind':"@",
            "message":event['message']
        }))

    def xx_oo(self,event):
        self.send(json.dumps({'kind':"message",
            'message': event['message']}))#给组内所有人回复

    # def websocket_disconnect(self, message):
    #     group = self.scope['url_route']['kwargs'].get("group")
    #     username = self.scope['url_route']['kwargs'].get("username")
    #     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     # onlineHistory[group][username].append(timestamp)
    #     '''删除聊天室之后，再加入新的聊天室的时候都会close，此时group不存在了'''
    #     users.remove(username)
    #     if group in userList:
    #         userList[group].remove(username)
    #         async_to_sync(self.channel_layer.group_discard)(group,self.channel_name)
    #         async_to_sync(self.channel_layer.group_send)(group, {"type": "exit", "name": userList[group]})

    def exit(self,event):
        self.send(json.dumps({'kind': "user",
                              'name': event['name']}))  # 给组内所有人回复



def login(request):
    print(users)
    print(userList)
    username = request.POST.get('userName')
    if username not in users:
        return JsonResponse({'status': 'success', 'exist': "no"})
    else:

        return JsonResponse({'status': 'success', 'exist': "yes"})
