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
import requests, json, os, platform
from cmd import Cmd
#from get import get
#from play import *
#from mvplay import mvplay
from system import system
import urllib.request
import time
import pygame
import socket
import hashlib
import threading





Version = '0.3.2'
Platform = platform.system()
Headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#IP = "192.168.31.212" #服务器端可以写"localhost"，可以为空字符串""，可以为本机IP地址
s.connect(('8.8.8.8', 80))
IP = s.getsockname()[0]
s.close()


print(IP)
time.sleep(1)
port = 40005 #端口号

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((IP,port))

print('listen at port :',port)

class Commands(Cmd):

        intro = 'WholeRoomAudio control panel by Wu_Eden \33[0m\n\33[1;37;46m目前可以使用的命令如下：\33[0m\n\33[1;37;46mplay 【id】| search 【name】|                                | about| exit|'
        prompt = '>'

        def __init__(self):
                Cmd.__init__(self)
                system.check_network('Init')
                try:
                        if os.path.exists('Download/Music') == False:
                                os.makedirs('Download/Music')
                        if os.path.exists('Download/Lyric') == False:
                                os.makedirs('Download/Lyric')
                        if os.path.exists('Download/MV') == False:
                                os.makedirs('Download/MV')
                        if os.path.exists('Download/cache.mp3') == True:
                                os.remove('Download/cache.mp3')
                except:
                        print(print('\33[1;37;41m创建下载目录失败。\33[0m'))
                        exit()
                global VLCPlayer
                try:
                        import vlc
                        VLCPlayer = vlc.libvlc_hex_version()
                        if VLCPlayer == 0:
                                VLCPlayer = False
                        else:
                                from mvplay import mvplay
                                VLCPlayer = True
                except:
                        VLCPlayer = False
                system.clear(Platform)
                
        
                
        def do_search(self, arg):
                
                if not arg:
                        print('\33[1;37;41m请指定对象。\33[0m')
                else:
                        PostData = {'s':arg, 'offset':0, 'limit':15, 'type':'1'}
                        SearchResult = requests.post('http://music.163.com/api/search/pc', data = PostData)
                        SearchResultProcessed = json.loads(SearchResult.text)
                        SearchResultNumber = 0
                        try:
                                print('\33[1;37;42m曲目\33[0m\33[1;37;44m艺术家\33[0m\33[1;37;45mID\33[0m')
                                while SearchResultNumber < 15:
                                        print('\33[1;37;42m' + SearchResultProcessed['result']['songs'][SearchResultNumber]['name'] + '\33[0m\33[1;37;44m' + SearchResultProcessed['result']['songs'][SearchResultNumber]['artists'][0]['name'] + '\33[0m' + '\33[1;37;45m' + str(SearchResultProcessed['result']['songs'][SearchResultNumber]['id']) + '\33[0m')
                                        SearchResultNumber += 1
                        except:
                                print('\33[1;37;41m没有更多结果。\33[0m')
                        PostData = {'s':arg, 'offset':0, 'limit':15, 'type':'1004'}
                        SearchResult = requests.post('http://music.163.com/api/search/pc', data = PostData)
                        SearchResultProcessed = json.loads(SearchResult.text)
                        SearchResultNumber = 0
                        try:
                                #print(Comlete    -Wu_Eden)
                                print('\n\33[1;37;42mMV\33[0m\33[1;37;44m艺术家\33[0m\33[1;37;45mID\33[0m')
                                print(Comlete    -Wu_Eden)
                                #while SearchResultNumber < 15:
                                        #print('\33[1;37;42m' + SearchResultProcessed['result']['mvs'][SearchResultNumber]['name'] + '\33[0m\33[1;37;44m' + SearchResultProcessed['result']['mvs'][SearchResultNumber]['artists'][0]['name'] + '\33[0m\33[1;37;45m' + str(SearchResultProcessed['result']['mvs'][SearchResultNumber]['id']) + '\33[0m')
                                        #SearchResultNumber += 1
                        except:
                                print('')



##########################################################！！！！！！！！！！！
        def do_play(self, arg):
                if not arg:
                        print('\33[1;37;41m请指定对象。\33[0m')
                else:
                        Download = 'M'
                        if Download == 'M':
                                TargetMusicURL = 'http://music.163.com/song/media/outer/url?id=' + arg + '.mp3'
                                #DetailResultProcessed = get.get_detail(arg)
                                
                                try:
                                   DetailTarget = 'http://music.163.com/api/song/detail/?id=' + str(arg) + '&ids=%5B' + str(arg) + '%5D'
                                   DetailResult = requests.get(DetailTarget, headers = Headers)
                                   DetailResultProcessed = json.loads(DetailResult.text)
                                
                                except:
                                   print('FAILED')
                                
                                
                                print('SUCCESSFULLY PROCSSED DATA')
                                try:
                                   print('\33[1;37;44m正在下载：' + DetailResultProcessed['songs'][0]['name'] + '...\33[0m')
                                   SongExists = True
                                except:
                                   print('\33[1;37;41m没有找到歌曲。\33[0m')
                                   SongExists = False
                                if SongExists == True:
                                     try:
                                          RequestDownload = requests.get(TargetMusicURL)
                                          global idc
                                          idc=TargetMusicURL
                                          FileName = '1.mp3'
                                          with open(FileName,'wb') as File:
                                                  File.write(RequestDownload.content)
                                          print('\33[1;37;42m文件已保存')
                                          pygame.mixer.init()
                                          print("准备播放音乐")

                                          track = pygame.mixer.music.load('1.mp3')

                                          b=float(0)

                                          pygame.mixer.music.play(start=float(b))
                                          #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                          #s.connect(('8.8.8.8', 80))
                                          #IP = s.getsockname()[0]
                                          #print(IP)
                                          #port=40005
                                         # s.bind((IP,port))
                                          #print('listen at port:',port)
                                          a=1
                                          while a==1:
                                                  
                                                  
                                                  md5=None
                                                  if os.path.isfile('1.mp3'):
                                                     f=open('1.mp3','rb')
                                                     md5_obj = hashlib.md5()
                                                     md5_obj.update(f.read())
                                                     hash_code = md5_obj.hexdigest()
                                                     f.close()
                                                     md5_01 = str(hash_code).lower()
                                                  
                                                  md5_01='@'+md5_01+'@'
                                                  md5_01=str(md5_01)

                                                  trans=idc 
                                                  trans='^'+trans+'^'
                                                  trans=str(trans)


                                                  

                                                  
                                                  c=pygame.mixer.music.get_pos()
                                                  d=c/1000
                                                  global l
                                                  e=b+d
                                                  
                                                  e="%.2f"% e
                                                  e='*'+e+'*'
                                                  
                                                  send = str(e+md5_01+trans)#python27要写raw_input,python3.X可写input
                                                  print(send)
                                                  send=bytes(send, "gbk")
                                                  s.sendto(send, ('192.168.31.190', 40006))
                                                  s.sendto(send, ('192.168.31.190', 40005))
                                                  #s.sendto(send, ('192.168.31.3', 40006))
                                                 # s.sendto(send, ('192.168.31.3', 40005))
                                                  launcher=pygame.mixer.music.get_busy()
                                                  if launcher==0:
                                                    pygame.mixer.init()
                                                    pygame.mixer.music.play()
#再编码发送
      
                                                  time.sleep(0.5)#small number may cause crash
  

                                                  
                                                  
                                                  
                                                  
                                                  

































                                          
                                          
                                     except PermissionError:
                                          print('\33[1;37;41m写入文件失败。\33[0m')
                                     #except:
                                          #print('\33[1;37;41m下载失败。\33[0m')
                                     else:
                                          pass
                                
                                
                                        

                                
#####################################################################
        def do_about(self, arg):
                print('\33[1;37;46mWholeRoomAudio ' + Version + '\33[0m')
                print('\33[1;37;46mA sync tool that allows PCs to offer the same audio playback \33[0m')
                print('\33[1;37;46m作者：Wu_Eden\33[0m')
                print('\33[1;37;46m开源许可证：MIT License\33[0m')
                print('\33[1;37;46m平台：' + Platform + '\33[0m')
                if VLCPlayer == True:
                        print('\33[1;37;46mVLC状态：\33[0m\33[1;37;42m可用\33[0m')
                elif VLCPlayer == False:
                        print('\33[1;37;46mVLC状态：\33[0m\33[1;37;41m不可用\33[0m')
                Delay = system.check_network(0)
                if not Delay:
                        print('\33[1;37;46m连接状态：\33[0m\33[1;37;41m无法连接\33[0m')
                else:
                        print('\33[1;37;46m连接状态：\33[0m\33[1;37;42m连接有效，延迟约' + Delay + '\33[0m')

        def do_exit(self, arg):
                system.clear(Platform)
                exit()

        def do_EOF(self, arg):
                system.clear(Platform)
                exit()

        def default(self, line):
                print('\33[1;37;41m找不到命令：' + line + '\33[0m')

        def emptyline(self):
                pass

if __name__ == '__main__':
        try:
                Commands().cmdloop()
        except KeyboardInterrupt:
                system.clear(Platform)
                exit()
                                
                                
                                
                
                                
                                
                                
