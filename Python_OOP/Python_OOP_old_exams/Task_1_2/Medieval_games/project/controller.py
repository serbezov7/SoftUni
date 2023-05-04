class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):

        current_added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                current_added.append(player.name)
        return f"Successfully added: {', '.join(current_added)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if not player:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."
        
        supply = self.__find_supply_by_type(sustenance_type)

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__find_player_by_name(first_player_name)
        player2 = self.__find_player_by_name(second_player_name)

        result = self.__check_valid_stamina(player1, player2)
        if result:
            return '\n'.join(result)

        attack_player, defend_player = self.__find_player_with_low_stamina(player1, player2)

        winner = self.__attack(attack_player, defend_player)

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

    def __find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __find_supply_by_type(self, supply_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == supply_type:
                return self.supplies.pop(i)
        raise Exception(f"There are no {supply_type.lower()} supplies left!")

    @staticmethod
    def __check_valid_stamina(player1, player2):
        result = []
        if player1.stamina == 0:
            result.append(f"Player {player1.name} does not have enough stamina.")
            if player2.stamina == 0:
                result.append(f"Player {player2.name} does not have enough stamina.")
        elif player2.stamina == 0:
            result.append(f"Player {player2.name} does not have enough stamina.")

        return result

    @staticmethod
    def __find_player_with_low_stamina(player1, player2):
        if player1.stamina < player2.stamina:
            return player1, player2
        return player2, player1

    @staticmethod
    def __attack(attack_player, defend_player):
        if defend_player.stamina - attack_player.stamina / 2 < 0:
            defend_player.stamina = 0
            return attack_player
        else:
            defend_player.stamina -= attack_player.stamina / 2

        if attack_player.stamina - defend_player.stamina / 2 < 0:
            attack_player.stamina = 0
            return defend_player
        else:
            attack_player.stamina -= defend_player.stamina / 2

        if attack_player.stamina > defend_player.stamina:
            return attack_player
        return defend_player


