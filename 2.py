class Football:
    def __init__(self, name,num, pos):
        self.num=num
        self.pos=pos
        self.name=name
    def __str__(self):
        ans=str(self.name)+','+str(self.num)+','+str(self.pos)+'\n'
        return ans
def main():
    player1=Football('Ronaldo', '7', 'St')
    print(player1)
    player2=Football('Messi', '30', 'Lw')
    print(player2)
    player3=Football('Neymar', '10', 'Lw')
    print(player3)
    player4=Football('Modric', '10', 'Cdm')
    print(player4)
    player5=Football('Pogba', '10', 'Cdm')
main()