#from sp_motor.sp_motor.game_classes.player import player
#STATE
#=0 NON UTILISE
#=1 EN ATTENTE
#=2 ACCEPTER
#=3 REFUSER


class Players_interraction:
    lastId = 0
    def __init__(self, player1,player2, type_pi, state=0):
        self.player1=player1
        self.player2=player2
        self.state=state
        self.type_pi=type_pi
        self.id = Players_interraction.lastId
        Players_interraction.lastId += 1

    def is_sended(self):
        self.state=1

    def is_accepted(self):
        self.state=2

    def is_declined(self):
        self.state=3

    def execute(self):
        if self.state==2:
            if self.type_pi_pi==1: #alliance
                #ajout mutuel des joueurs dans les listes d'alliés
                self.player1.add_ally(self.player2)
                self.player2.add_ally(self.player1)
            if self.type_pi==2: #ennemies
                #ajout mutuel des joueurs dans les listes d'ennemis
                self.player1.add_enemy(self.player2)
                self.player2.add_enemy(self.player1)
            if self.type_pi==3: #retirer alliance
                self.player1.remove_ally(self.player2)
                self.player2.remove_ally(self.player1)
            if self.type_pi==4: #retirer ennemis
                self.player1.remove_enemy(self.player2)
                self.player2.remove_enemy(self.player1)
            if self.type_pi==5: #echange commercial
                print("echange commercial")

    def to_front(self):
        dic = {
        "id":self.id,
        "player1":self.player1,
        "player2":self.player2,
        "state":self.state,
        "type":self.type_pi,
        }
        return dic









