class Player():
  def __init__(self, name, score):
    self.name = name
    self.score =score
    self.team =None
    
  def show_stats(self):
      print("Player:", self.name)
      print("Average points", self.score)
      print("Team:", self.team)
      
  def select_team(self):
    team= input("Enter the team name:")
    self.team = team
    
player = Player("Virender Sehwag", 323)
player.show_stats()
player.select_team()
      
      
    