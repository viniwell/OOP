from tkinter import *
from time import sleep
class Tv:
    def __init__(self, loud=10, channel=1):
        print('Company Vini')
        self.loud=loud
        self.channel=channel

    def loud_down(self, step):
        if self.loud-step<0:
            self.loud=0
        else:
            self.loud-=step
    def loud_up(self, step):
        if self.loud+step>100:
            self.loud=100
        else:
            self.loud+=step
    def channel_down(self):
        if self.channel>1:
            self.channel-=1
        else:
            self.channel=2
    def channel_up(self):
        if self.channel<2:
            self.channel+=1
        else:
            self.channel=1
    def __str__(self):
        ans=f'Текущие данные:\nГромкость-{self.loud},\nКанал-{self.channel}'
        return ans


def main():
    tv=Tv()
    
    choice=-1
    while choice!=0:
        if tv.channel==1:
            root=Tk()
            c=Canvas(root, width=800, height=600, background='blue')
            c.grid()
            c.create_oval(385, 315, 415,285, fill='yellow')
            c.create_line(400,315,400,375,fill='#005500',width=5)
            c.create_oval(385,285,415,265,fill='red')
            c.create_oval(415,285,435,315,fill='purple')
            c.create_oval(385,315,415,335,fill='white')
            c.create_oval(385,285,365,315, fill='orange')
            c.create_text(750,10,text=f'Текущие данные:\nГромкость-{tv.loud},\nКанал-{tv.channel}')
            root.mainloop()
        if tv.channel==2:
            root=Tk()
            c=Canvas(root, width=800, height=600, background='blue')
            c.grid()
            c.create_rectangle(0,300,800,600,fill='yellow')
            c.create_line(400,250,400,350,fill='black',width=5)
            c.create_oval(388,225,412,250, fill='white',outline='black',)
            c.create_line(400,275,350,300,fill='black',width=5)
            c.create_line(400,275,450,300,width=5)
            c.create_line(400,350,375,375,fill='black',width=5)
            c.create_line(400,350,425,375,fill='black',width=5)
            c.create_text(450,25,text='ЗСУ звільнили Херсон!', fill='yellow')
            c.create_text(750,10,text=f'Текущие данные:\nГромкость-{tv.loud},\nКанал-{tv.channel}')
        print('Выберите операцию:\n0-Выход\n1-Громкость вверх\n2-Громкость вниз\n3-Канал вверх\n4-Канал вниз')
        choice=input()
        if choice=='1':
            step=int(input('Введите шаг-->'))
            tv.loud_up(step)
            print(tv)
        elif choice=='2':
            step=int(input('Введите шаг-->'))
            tv.loud_down(step)
            print(tv)
        elif choice=='3':
            tv.channel_up()
            print(tv)
        elif choice=='4':
            tv.channel_down()
            print(tv)
        else:
            print(tv)
            break
main()

