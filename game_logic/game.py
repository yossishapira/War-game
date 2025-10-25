from utils import deck


def create_player(name="Ai") -> dict:
    player = {"name":"","hand":[],"won_pile":[]}
    player["name"] = name
    return player

print(create_player())


def init_game()->dict:
    p1 = create_player("yossi")
    p2 = create_player()
    p1["hand"] = deck.shuffle(deck.create_deck("deck"[:26]))
    p2["hand"] = deck.shuffle(deck.create_deck("deck"[26:]))
    print(p1)
    print(p2)


def play_round(p1:dict,p2:dict):

    return


