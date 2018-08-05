#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright  zzxjl1
#    +Author Wu_Eden
#    +Email  349888274@qq.com  zzxjl1@hotmail.com
#    +QQ     349888274
#    +Website https://www.ideabroker.tk
#    +twitter https://twitter.com/JohnShepard2000
#    Licensed under the MIT License, Version 2.0 (the "License");
__author__ = 'Wu_Eden'
from tkinter import *
import pygame
import socket
import time
import os
import sys
import hashlib
import threading
import requests
import urllib.request
#file=r'/home/pi/Desktop/1.mp3'

pygame.mixer.init()
#track = pygame.mixer.music.load(file)
a='1.mp3'##########！！！！！！！###################

#gui

root =Tk()
s2 = Scale(root,from_=-10,to=10,tickinterval=5,resolution=0.01,length=1400,orient=HORIZONTAL)  #orient=HORIZONTAL设置水平方向显示

s2.pack()

po=s2.get()
    #time.sleep(0.2)
pos=str(po)
file= open('4ca4fe09f77101be32b3dd90c48382f0.txt', 'w')
file.write(pos)
file.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
 
print ('你的内网ip:',ip)



def show():
###################################################################################3
   #md5 remote
    #data=0
    #server_socket.close()
   ## PORT = 40005
   # server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # try:
         # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         # s.connect(('8.8.8.8', 80))
         # ip = s.getsockname()[0]
   # finally: s.close() 

        #print (ip)
    #address = (ip, PORT)
    #server_socket.bind(address)
    #receive_data, client_address = server_socket.recvfrom(1024)
    #data=receive_data.decode()
    #print(data)
    
    #time=data.split('*')
    #print(time)
    #time=time[-2]
    #print(time)
   # md5_01=data.split('@')
    #print('time:',time)
    #print(md5_01)
    #md5_01=md5_01[-2]
    #print('md5:',md5_01)






        
           #md5 local
    



    
    #md5=None
    #md5_01=0
    #md5_02=0
    #f = open(r'1.MP3','rb')
    #md5_obj = hashlib.md5()
    #md5_obj.update(f.read())
    #hash_code = md5_obj.hexdigest()
    #f.close()
   # md5 = str(hash_code).lower()
    
   # md5_02 = md5
    #print('md5:',md5_02)

         #md5 compare
   # if md5_01!=md5_02:
          #print('DETECTED MD5 CHANGE !')


      #md5 compare
###################################################################################



    
    
    print("准备播放音乐")


    po=s2.get()
    #time.sleep(0.2)
    pos=str(po)
    file= open('4ca4fe09f77101be32b3dd90c48382f0.txt', 'w')
    file.write(pos)
    file.close()
    
    


    
    print('当前偏移量：',po)
    data=0
    #server_socket.close()
    PORT = 40005
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(('8.8.8.8', 80))
      ip = s.getsockname()[0]
    finally: s.close() 

    print (ip)
    address = (ip, PORT)
    server_socket.bind(address)
    receive_data, client_address = server_socket.recvfrom(1024)
    data=receive_data.decode()
    #print(data)
    
    time=data.split('*')
    #print(time)
    time=time[-2]
    #print(time)
    #md5_01=data.split('@')
    #print('time:',time)
    #print(md5_01)
    #md5_01=md5_01[-2]
    #print('md5:',md5_01)
    
    print('SUCCESSFULLY received all data')
    time=float(time)
    
    time=time+po
    
    track = pygame.mixer.music.load('1.mp3')
    #print (time)
    pygame.mixer.music.play(start=time)
    server_socket.close()

    global launcher

    launcher=1

       
Button(root,text='发送位置',command=show).pack()
#mainloop()
################################subprocess

def loop():
  
  a=1
  
  while a==1 :
    import time
    time.sleep(0.5)

    f=open('4ca4fe09f77101be32b3dd90c48382f0.txt','r')
    po=f.readline()
    po=float(po)
    #print('当前偏移量:',po)
####################################
   # url = 'http://103.94.185.36/1.mp3' 
   # f = urllib.request.urlopen(url) 
   # data = f.read() 
   # with open('1.mp3', "wb") as code:     
       #  code.write(data)#下载完成
        

######################################








    



    
    data=0
    #server_socket.close()
    #PORT = 40005
    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
 

    #print ('ip:',ip)
    PORT = 40006
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (ip, PORT)

    


    
    server_socket.bind(address)
    
    receive_data, client_address = server_socket.recvfrom(1024)
    data=receive_data.decode()
    time=data.split('*')
    #print(time)
    time=time[-2]
    time=float(time)
    
    #print(time)
    time=time+po#####################################################!!!!!!!!
    #print(time)
    server_socket.close()

    busy=pygame.mixer.music.get_busy()
    if busy==0:

        if os.path.exists('1.mp3'):
            #print('yes')
            track = pygame.mixer.music.load('1.mp3')
            pygame.mixer.music.play(start=time)
        else:
            

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            PORT = 40006
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
            address = (ip, PORT)
            server_socket.bind(address)
            receive_data, client_address = server_socket.recvfrom(1024)
            data=receive_data.decode()
  #print (data)
            musicurl=data.split('^')
            musicurl=musicurl[-2]
            server_socket.close()
            print('文件不存在，下载中')
            #Button(root,text='发送位置').pack()  ########
            f = requests.get(musicurl) 
        #data = f.read() 
            with open('1.mp3', "wb") as code:     
              code.write(f.content)#下载完成
            print('下载成功')
           # Button(root,text='发送位置',command=show).pack()

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
 

    #print ('ip:',ip)
            PORT = 40006
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (ip, PORT)

            server_socket.bind(address)
    
            receive_data, client_address = server_socket.recvfrom(1024)
            data=receive_data.decode()
            time=data.split('*')
    #print(time)
            time=time[-2]
            time=float(time)
    
    #print(time)
            time=time+po#####################################################!!!!!!!!
    #print(time)
            server_socket.close()
            track = pygame.mixer.music.load('1.mp3')


            pygame.mixer.music.play(start=time)


    
    
    md5_01=data.split('@')
    
    #print(md5_01)
    md5_01=md5_01[-2]
    #print('md5:',md5_01)
    

           #md5 local
 
    md5 = None

    f = open('1.mp3','rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    
    md5_02=md5 
    #print('md5:',md5_02)
        
    #time.sleep(2)#test
   # pygame.mixer.music.stop()
    
    
    #print(busy)
    
 
         
    if md5_01!=md5_02:##############################################
        pygame.mixer.music.stop()
        #print('暂不支持自动更换音乐!')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        PORT = 40006
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
        address = (ip, PORT)
        server_socket.bind(address)
        receive_data, client_address = server_socket.recvfrom(1024)
        data=receive_data.decode()
  #print (data)
        musicurl=data.split('^')
        musicurl=musicurl[-2]
        server_socket.close()
        print('检测到歌曲变更，正在请求服务器提供的下载地址：',musicurl)
        if os.path.exists('1.mp3'):
          pygame.mixer.music.stop()
          pygame.mixer.quit()
          
          os.remove('1.mp3')
          pygame.mixer.init()
          
          #pygame.mixer.music.play()
          

          
          
        
        f = requests.get(musicurl) 
        #data = f.read() 
        with open('1.mp3', "wb") as code:     
            code.write(f.content)#下载完成
        print('下载成功')
        track = pygame.mixer.music.load('1.mp3')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
 

    #print ('ip:',ip)
        PORT = 40006
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = (ip, PORT)

    


    
        server_socket.bind(address)
    
        receive_data, client_address = server_socket.recvfrom(1024)
        data=receive_data.decode()
        time=data.split('*')
    #print(time)
        time=time[-2]
        time=float(time)
    
    #print(time)
        time=time+po#####################################################!!!!!!!!
    #print(time)
        server_socket.close()
        
        pygame.mixer.music.play(start=time)

        


    



t = threading.Thread(target=loop, name='LoopThread')

t.start()


mainloop()


