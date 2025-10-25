import random

def create_card(rank:str,suite:str) -> dict:
    dicti = {"rank":"" ,"suite":"" ,"value":""}
    value_rank = {"2":2 ,"3":3 ,"4": 4,"5":5 ,"6": 6,"7":7,"8":8,
              "9":9 ,"10":10,"J":11,"Q":12,"K":13,"A":14}
    dicti["rank"] = rank.upper()
    dicti["suite"] = suite.upper()
    for i in value_rank:
        if  i == rank.upper():
            dicti["value"] = value_rank[i] 
    return dicti  

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "WAR" 

def create_deck() -> list[dict]:
    deck = []
    cards1 = {}
    suite = ["H","C","D","S"]
    rank = ["2","3","4","5","6","7",
     "8","9","10","J","Q","K","A"]
    
    for x in suite:
        for s,z in enumerate(rank):
            cards2 = {"rank":"","suite":"","value":""}
            cards2["rank"] = z
            cards2["suite"] = x
            cards2["value"] = s+2
            cards1 = cards2
            deck.append(cards1)
                
                
    return deck


import random
def shuffle(deck:list[dict]) -> list[dict]:
    my_deck = deck
    count = 0
    while count < 1000:
       count +=1
       random_index1 = random.randint(0,51)
       random_index2 = random.randint(0,51)
       if random_index1 == random_index2:
           continue
       else:
           my_deck[random_index1], my_deck[random_index2] = my_deck[random_index2], my_deck[random_index1]
    
    return my_deck
print(shuffle(create_deck()))


