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
import winreg
import requests
import urllib.request
import time
import pygame
import socket
import hashlib
import os
import threading

#file=r'C:\Users\zzxjl\Desktop\1.mp3'








#桌面路径+下载	
	
def get_desktop():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')#利用系统的链表
        return winreg.QueryValueEx(key, "Desktop")[0] #返回的是Unicode类型数据
if __name__=='__main__':
  z=str(get_desktop())#Unicode转化为str
   

        #print(z)#生成桌面路径
  k=z+'\ 1.mp3'
    
  print('临时文件目录：',k)
    
 
print ("downloading with urllib")
url = 'http://103.94.185.36/1.mp3' 
f = urllib.request.urlopen(url) 
data = f.read() 
with open(k, "wb") as code:     
      code.write(data)#下载完成

#md5对比
      

def get_md5_01(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
  return md5
 
if __name__ == "__main__":
  file_path = k
  md5_01 = get_md5_01(file_path)
  print('md5:',md5_01)

















      
pygame.mixer.init()
print("准备播放音乐")
file=k
track = pygame.mixer.music.load(file)

b=float(0)

pygame.mixer.music.play(start= float(b))




#network config


IP = "192.168.31.212" #服务器端可以写"localhost"，可以为空字符串""，可以为本机IP地址

port = 40005 #端口号

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((IP,port))



print('listen at port :',port)



#print('connected by',addr)



    
a=1
while a==1 :
   #print (pygame.mixer.music.get_pos())
   c=pygame.mixer.music.get_pos()
   #print(c)
   d=c/1000
   e=d+b
   e="%.2f" % e
   e='*'+e+'*'
   #print(e)
   #st=str(e)
   #md5对比
      

   def get_md5_01(file_path):
      md5 = None
      if os.path.isfile(file_path):
        f = open(file_path,'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
      return md5
 
   if __name__ == "__main__":
    file_path = k
    md5_01 = get_md5_01(file_path)
    #print('md5:',md5_01)
    md5_01 = '@'+md5_01+'@'




   

  # 播放结束则从新开始并清零计时器
   launcher=pygame.mixer.music.get_busy()
   if launcher==0:
        pygame.mixer.init()
        pygame.mixer.music.play()
        


  

   send = str(e+md5_01)#python27要写raw_input,python3.X可写input
   print(send)
   send=bytes(send, "gbk")
   s.sendto(send, ('192.168.31.190', 40006))
   s.sendto(send, ('192.168.31.190', 40005))
   s.sendto(send, ('192.168.31.3', 40006))
   s.sendto(send, ('192.168.31.3', 40005))
#再编码发送
      
   time.sleep(0.1)#small number may cause crash
  









































