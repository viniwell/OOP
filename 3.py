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
            self.channel=50
    def channel_up(self):
        if self.channel<50:
            self.channel+=1
        else:
            self.channel=0
    def __str__(self):
        ans=f'Текущие данные:\n Громкость-{self.loud},\nКанал-{self.channel}'
        return ans
def main():
    tv=Tv()
    
    choice=-1
    while choice!=0:
        sleep(1.0)
        print('Выберите операцию:\n0-Выход\n1-Громкость вверх\n2-Громкость вниз\n3-Канал вверх\n4-Канал вниз')
        choice=input()
        sleep(1.0)
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
