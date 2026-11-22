class player : 
    sport='football'
    def __init__(self,name):
        self.name=name
        self.goals=0
        self.stamina=100

    def train(self):
        if self.stamina>=20:
          self.stamina=self.stamina-20
          print(f'you have {self.stamina}stamina left\t')
        else:
            print('your player need rest \t')

    def rest(self):
    
        if self.stamina<=60:
            self.stamina=self.stamina+20
            print(f'your player has just rested , he has {self.stamina} stamina now!\t')
        else:
            print('your player already can keep pushing')            
    def score(self):
        if self.stamina>=50:
            self.goals=self.goals+1
            self.stamina=self.stamina-35
            print(f'i just scored ! , i have {self.goals} goals now !\t')
        else:
            print(f'your player barely can pass his stamina is {self.stamina}')    
    def defend(self):
        if self.stamina>=30:
            print('what a tackle !\t ')
            self.stamina-=10
        else:
            print(' i almost do wrong passes i am tired cannot tackle Mbappe !!')
    
    def show_player_status(self):
        print(f'stamina : {self.stamina} , goals {self.goals}')
p1=player(input('what do you want to name your player ? : '))
print('''====welcome to BOLBOL's sport game====\n ''')
print(player.sport)
while True:
        print('what do you want to do ? (choose by numbers)')
        print(f''' 1 show {p1.name} status
        2 let him rest 
        3 score a goal!
        4 defend 
        5 train him 
        6 exit ''')
        q=input('')
        if q=='1':
            p1.show_player_status()
        elif q=='2':
            p1.rest()
        elif q=="3":
            p1.score()
        elif q=="4":
            p1.defend()
        elif q=="5":
            p1.train()    
        elif q=="6":   
         break 
        else:
            print('you enterd a wrong number or you entered a sentence , please make sure to enter a number from 1 to 6 ')
                  
            