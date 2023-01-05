#--------------做准备工作的地方-----------------
import pygame #导入pygame ==>python game
from pygame.locals import * #从pygame本地导入所有函数或者对象
from sys import exit #sys-->system 从系统中导入退出方法
import time #导入时间对象
import random #导入随机数对象

pygame.init() #初始化pygame,告诉程序下面可以使用pygame的东西了
screen=pygame.display.set_mode((480,800)) #创建一个窗口
#screen=其他的东西
#女朋友=创建一个女朋友
#screen英文-->中文是窗口的意思,在这里就是一个名字
pygame.display.set_caption('飞机大战') #在窗口显示游戏名称‘飞机大战’

background=pygame.image.load('background.png')
#背景=加载一个背景图片
hero=pygame.image.load('hero0.png') #加载英雄机0图片
hero1=pygame.image.load('hero1.png') #加载英雄机1图片
hero_down=pygame.image.load('hero_down.png') #加载英雄机爆炸的图片
num=0 #num-->number 计数器

heroX=200 #英雄飞机的X坐标
heroY=400 #英雄飞机的Y坐标

enemy1=pygame.image.load('enemy1.png') #加载普通敌机图片
#加载三张普通敌机爆炸的造型图
enemy1_down1=pygame.image.load('enemy1_down1.png')
enemy1_down2=pygame.image.load('enemy1_down2.png')
enemy1_down3=pygame.image.load('enemy1_down3.png')
enemy1_x=[] #创建普通敌机的X坐标列表
enemy1_y=[] #创建普通敌机的Y坐标列表
enemy2=pygame.image.load('enemy2.png') #加载高级敌机图片
#加载三张高级敌机爆炸的造型图
enemy2_down1=pygame.image.load('enemy2_down1.png')
enemy2_down2=pygame.image.load('enemy2_down2.png')
enemy2_down3=pygame.image.load('enemy2_down3.png')
enemy2_x=[] #创建高级敌机的X坐标列表
enemy2_y=[] #创建高级敌机的Y坐标列表
enemy2_blood=[] #创建高级敌机血量的列表
enemy3=pygame.image.load('enemy3.png') #加载超级敌机图片
#加载三张超级敌机爆炸的造型图
enemy3_down1=pygame.image.load('enemy3_down1.png')
enemy3_down2=pygame.image.load('enemy3_down2.png')
enemy3_down3=pygame.image.load('enemy3_down3.png')
enemy3_x=[] #创建超级敌机的X坐标列表
enemy3_y=[] #创建超级敌机的Y坐标列表
enemy3_blood=[] #创建超级敌机血量的列表
bullet=pygame.image.load('bullet.png') #加载子弹图片
bulletX=[] #创建空的子弹X坐标列表
bulletY=[] #创建空的子弹Y坐标列表

flag=0 #子弹模式标记，当flag为0时，出现单子弹；当flag为1时，出现双子弹

isgameover=0 #是否游戏结束的标记，当isgameover为0时，游戏不结束；当isgameover为1时，游戏结束
gameover=pygame.image.load('gameover.png') #加载游戏结束图片
gameover=pygame.transform.scale(gameover,(480,800))

font=pygame.font.Font('simsun.ttc',40) #创建一种字体
text=font.render('得分:',True,(255,0,0)) #创建文本
score=0 #分数初始化为0

#index=[]

#-------------主循环体，这是程序真正实现效果的地方----------
while True:
    screen.blit(background,(0,0)) #将背景图片贴到窗口中
    screen.blit(text,(10,10)) #将文本贴到窗口中
    text_score=font.render(str(score),True,(255,0,0))
    screen.blit(text_score,(120,10)) #将分数贴到窗口中
    #游戏正常运行
    if isgameover==0:
        #---------实现英雄飞机喷气
        #计数器=0 显示英雄机图片0
        #计数器加1 计数器=1 显示英雄机图片1
        #计数器加1 计数器=2 显示英雄机图片0
        #计数器加1 计数器=3 显示英雄机图片1
        #......
        if num%2==0: #计数器对2求余，余数为零就代表为偶数
            screen.blit(hero,(heroX,heroY)) #将英雄机图片0贴到窗口中
        else: #else==>否则 判定为奇数
            screen.blit(hero1,(heroX,heroY))
        time.sleep(0.01) #每次循环体执行时等待0.01
        num=num+1 #计数器加1        
        #---------英雄飞机的移动
        pos=pygame.mouse.get_pos() #获取鼠标坐标
        heroX=pos[0]-hero.get_width()/2 #get_width()获取宽度的方法
        heroY=pos[1]-hero.get_height()/2 #get_height()获取高度的方法
        #---------普通敌机的功能
        #每隔30个计数num往普通敌机坐标列表里添加一个坐标
        if num%30==0:
            enemy1_x.append(random.randint(0,480-enemy1.get_width()))
            enemy1_y.append(0)
        #贴所有普通敌机的方法
        for i in range(len(enemy1_x)): #range==>范围 len==>length长度
            screen.blit(enemy1,(enemy1_x[i],enemy1_y[i]))
        #实现普通敌机下落的方法
        for i in range(len(enemy1_x)):
            enemy1_y[i]=enemy1_y[i]+2
            if enemy1_y[i]>800:
                del enemy1_y[i] #del==>delete删除
                del enemy1_x[i]
                break
        #----------高级敌机的功能
        #每隔120个计数num往高级敌机坐标列表里添加一个坐标
        if num%120==0:
            enemy2_x.append(random.randint(0,480-enemy2.get_width()))
            enemy2_y.append(0)
            enemy2_blood.append(10) #增加高级敌机血量
        #贴所有高级敌机的方法
        for i in range(len(enemy2_x)): #range==>范围 len==>length长度
            screen.blit(enemy2,(enemy2_x[i],enemy2_y[i]))
        #实现高级敌机下落的方法
        for i in range(len(enemy2_x)):
            enemy2_y[i]=enemy2_y[i]+2
            if enemy2_y[i]>800:
                del enemy2_y[i] #del==>delete删除
                del enemy2_x[i]
                del enemy2_blood[i]
                break

        #----------超级敌机的功能
        #每隔360个计数num往超级敌机坐标列表里添加一个坐标
        if num%360==0:
            enemy3_x.append(random.randint(0,480-enemy3.get_width()))
            enemy3_y.append(0)
            enemy3_blood.append(20) #增加超级敌机血量
        #贴所有超级敌机的方法
        for i in range(len(enemy3_x)): #range==>范围 len==>length长度
            screen.blit(enemy3,(enemy3_x[i],enemy3_y[i]))
        #实现超级敌机下落的方法
        for i in range(len(enemy3_x)):
            enemy3_y[i]=enemy3_y[i]+2
            if enemy3_y[i]>800:
                del enemy3_y[i] #del==>delete删除
                del enemy3_x[i]
                del enemy3_blood[j]
                break

        #每隔10个计数出现一颗子弹
        if num%10==0:
            if flag==0: #产生单子弹
                bulletX.append(heroX+hero.get_width()/2-bullet.get_width()/2)
                bulletY.append(heroY-bullet.get_height())
            elif flag==1: #elif==>else if 产生双子弹
                #子弹1
                bulletX.append(heroX+hero.get_width()/4-bullet.get_width()-5)
                bulletY.append(heroY+hero.get_height()/4)
                #子弹2
                bulletX.append(heroX+3*hero.get_width()/4+5)
                bulletY.append(heroY+hero.get_height()/4)
        #实现贴所有子弹的方法
        for i in range(len(bulletX)):
            screen.blit(bullet,(bulletX[i],bulletY[i]))
        #让子弹飞
        for i in range(len(bulletX)):
            bulletY[i]=bulletY[i]-10
            if bulletY[i]<0:
                del bulletX[i]
                del bulletY[i]
                break
        #for i in range(len(index)):
            #del bulletX[index[i]]
            #del bulletY[index[i]]
            #index.remove(index[i])
            #break;
        #---------------普通敌机被打死
        for i in range(len(bulletX)): #遍历每一颗子弹
            for j in range(len(enemy1_x)): #遍历每一个普通敌机
                #判断子弹是否打中普通敌机
                #先判断子弹的X坐标是否在打中敌机的范围内
                if bulletX[i]>enemy1_x[j]-bullet.get_width() and bulletX[i]<enemy1_x[j]+enemy1.get_width():
                    #判断子弹的Y坐标是否在打中敌机的范围内
                    if bulletY[i]>enemy1_y[j]-bullet.get_height() and bulletY[i]<enemy1_y[j]+enemy1.get_height():
                        #index.append(i)
                        score=score+1
                        #显示爆炸的效果
                        screen.blit(enemy1_down1,(enemy1_x[j],enemy1_y[j]))
                        screen.blit(enemy1_down2,(enemy1_x[j],enemy1_y[j]))
                        screen.blit(enemy1_down3,(enemy1_x[j],enemy1_y[j]))
                        #删除普通敌机
                        del enemy1_x[j]
                        del enemy1_y[j]
                        break
            
        #----------------高级敌机被打死
        for i in range(len(bulletX)): #遍历每一颗子弹
            for j in range(len(enemy2_x)): #遍历每一个高级敌机
                #判断子弹是否打中高级敌机
                #先判断子弹的X坐标是否在打中敌机的范围内
                if bulletX[i]>enemy2_x[j]-bullet.get_width() and bulletX[i]<enemy2_x[j]+enemy2.get_width():
                    #判断子弹的Y坐标是否在打中敌机的范围内
                    if bulletY[i]>enemy2_y[j]-bullet.get_height() and bulletY[i]<enemy2_y[j]+enemy2.get_height():
                        #index.append(i)
                        enemy2_blood[j]=enemy2_blood[j]-1
                        if enemy2_blood[j]<=0:
                            score=score+2
                            #显示爆炸的效果
                            screen.blit(enemy2_down1,(enemy2_x[j],enemy2_y[j]))
                            screen.blit(enemy2_down2,(enemy2_x[j],enemy2_y[j]))
                            screen.blit(enemy2_down3,(enemy2_x[j],enemy2_y[j]))
                            #删除高级敌机
                            del enemy2_x[j]
                            del enemy2_y[j]
                            del enemy2_blood[j]
                            break
        #---------------超级敌机被打死
        for i in range(len(bulletX)): #遍历每一颗子弹
            for j in range(len(enemy3_x)): #遍历每一个超级敌机
                #判断子弹是否打中超级敌机
                #先判断子弹的X坐标是否在打中敌机的范围内
                if bulletX[i]>enemy3_x[j]-bullet.get_width() and bulletX[i]<enemy3_x[j]+enemy3.get_width():
                    #判断子弹的Y坐标是否在打中敌机的范围内
                    if bulletY[i]>enemy3_y[j]-bullet.get_height() and bulletY[i]<enemy3_y[j]+enemy3.get_height():
                        #index.append(i)
                        enemy3_blood[j]=enemy3_blood[j]-1
                        if enemy3_blood[j]<=0:
                            score=score+3
                            #显示爆炸的效果
                            screen.blit(enemy3_down1,(enemy3_x[j],enemy3_y[j]))
                            screen.blit(enemy3_down2,(enemy3_x[j],enemy3_y[j]))
                            screen.blit(enemy3_down3,(enemy3_x[j],enemy3_y[j]))
                            #删除超级敌机
                            del enemy3_x[j]
                            del enemy3_y[j]
                            del enemy3_blood[j]
                            break    
        #英雄机被撞死的方法
        #撞上普通敌机
        for i in range(len(enemy1_x)):
            if enemy1_x[i]>heroX-enemy1.get_width() and enemy1_x[i]<heroX+hero.get_width():
                if enemy1_y[i]>heroY-enemy1.get_height() and enemy1_y[i]<heroY+hero.get_height():
                    isgameover=1
                    #出现爆炸的图片
                    screen.blit(hero_down,(heroX,heroY))
        #撞上高级敌机
        for i in range(len(enemy2_x)):
            if enemy2_x[i]>heroX-enemy2.get_width() and enemy2_x[i]<heroX+hero.get_width():
                if enemy2_y[i]>heroY-enemy2.get_height() and enemy2_y[i]<heroY+hero.get_height():
                    isgameover=1
                    #出现爆炸的图片
                    screen.blit(hero_down,(heroX,heroY))
        #撞上超级敌机
        for i in range(len(enemy3_x)):
            if enemy3_x[i]>heroX-enemy3.get_width() and enemy3_x[i]<heroX+hero.get_width():
                if enemy3_y[i]>heroY-enemy3.get_height() and enemy3_y[i]<heroY+hero.get_height():
                    isgameover=1
                    #出现爆炸的图片
                    screen.blit(hero_down,(heroX,heroY))
                    
    #游戏结束
    elif isgameover==1:
        screen.blit(gameover,(0,0))
    else:
        num=0 #num-->number 计数器重新初始化
        heroX=200 #英雄飞机的X坐标重新初始化
        heroY=400 #英雄飞机的Y坐标重新初始化
        enemy1_x=[] #普通敌机的X坐标列表重新初始化
        enemy1_y=[] #普通敌机的Y坐标列表重新初始化
        enemy2_x=[] #高级敌机的X坐标列表重新初始化
        enemy2_y=[] #高级敌机的Y坐标列表重新初始化
        enemy3_x=[] #超级敌机的X坐标列表重新初始化
        enemy3_y=[] #超级敌机的Y坐标列表重新初始化
        bulletX=[] #子弹X坐标列表重新初始化
        bulletY=[] #子弹Y坐标列表重新初始化
        flag=0 #子弹标记重新初始化
        score=0 #分数清零
        isgameover=0 #重新回到正常运行的标记---必须写在最后
        
    pygame.display.update() #将屏幕更新
    #实现窗口退出
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
        #双等于==代表判断，单个等于=代表赋值
            pygame.quit()
            exit()
        if event.type==KEYDOWN: #键盘按下事件
            if event.key==K_a:  #键盘按钮是否为a
                flag=1
            if event.key==K_s:  #键盘按钮是否为s
                flag=0
            if event.key==K_SPACE: #键盘按钮是否为空格
                if isgameover==1:
                    isgameover=2  #2代表游戏重新开始
        




















        
    
