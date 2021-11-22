
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader 
        
    def top_scorers_by_nationality(self, nation):
        players = self.reader.get_players()
        national_players = []

        for player in players:
            if player.nationality == nation:
                national_players.append(player)
            
        national_players.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return national_players
        