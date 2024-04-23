print("starting")
### sugestion, dry: conn.close with a raise error

from typing import Union
import hashlib
import random

import logging


logger = logging.getLogger("logging.conf")


from fastapi import FastAPI, HTTPException#, Response
#from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="api")


# import time
# from pydantic import BaseModel
deck = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r1', 'r2',
        'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'rs', 'rr', 'r+2', 'rs', 'rr',
        'r+2', 'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g1',
        'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'gs', 'gr', 'g+2', 'gs',
        'gr', 'g+2', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'bs', 'br', 'b+2',
        'bs', 'br', 'b+2', 'y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8',
        'y9', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'ys', 'yr', 
        'y+2', 'ys', 'yr', 'y+2', 'B-', 'B+4', 'B-', 'B+4', 'B-', 'B+4', 'B-', 'B+4',
]

# maximum number of games
MAX_GID = 256
# maximum number of players
MAX_UID = 4


table = "uno2"


def pswd_hash(pswd):
    salt = b"salt"  # very salty
    hash_object = hashlib.sha256(salt + pswd.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


import mysql.connector
import mysql.connector.pooling
from mysql.connector import Error


import secure

# conn = create_db_connection("localhost", secure.user,secure.pw,'games')
# conn.autocommit=True

conn_pool = mysql.connector.pooling.MySQLConnectionPool(
    host="localhost",
    user=secure.user,
    passwd=secure.pw,
    database="games",
    pool_name="onu_pool",
    pool_size=4,
)


def get_conn_from_pool():
    try:
        connection = conn_pool.get_connection()
        connection.autocommit = True
        if connection.is_connected():
            return connection
        else:
            connection.reconnect()
            return connection
    except Error as err:
        print(f"Error: '{err}'")
        logger.error(f"MySQL Database connection errrrr -------- {err}")
        print(f"MySQL Database connection errrrr -------- {err}")
        return None


def exec_query(connection, query, val):  # connection#
    cursor = connection.cursor()
    try:
        cursor.execute(query, val)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")
        logger.error(f"MySQL Database connection errrrr -------- {err}")
    finally:
        # used for re conn every query
        #cursor.close()
        #connection.close()
        pass


def read_query(connection, query, commit=False):  # connection
    if not connection:
        raise Exception("INVALDI PIEP DATABASE COONECNKLTION EROROR")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if commit:
            connection.commit()
        return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
        logger.error(f"MySQL Database connection errrrr -------- {err}")
    finally:
        # used for re conn every query
        #cursor.close()
        #connection.close()
        pass



# cross site origin

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redirect http to https
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# app.add_middleware(HTTPSRedirectMiddleware)


# print(dir(app))


def hand2str (handlist):
    return ',t'.join(handlist)

def hand2list (handstr):
    return handstr.split(',')



@app.get("/names")
def names():

    #
    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    result = read_query(connection, f"""SELECT game_name,game_num,player_count,game_pswd FROM {table};""")
    name_list = []
    index_list = []
    player_count = []
    game_pswd = []
    for row in result:
        name_list.append(row[0])
        index_list.append(row[1])
        player_count.append(row[2])
        # game_pswd.append(row[3])
        game_pswd.append(row[3]!='63479ad69a090b258277ec8fba6f99419a2ffb248981510657c944ccd1148e97')

    connection.close()
    return {"names": name_list, "index": index_list, 'player_count':player_count,'game_pswd':game_pswd}


def public_internal(connection, ID):

    result = read_query(
        connection,
        f"""\
SELECT name0, name1, name2, name3, game_name, \
turn, direction, age, top_card, draw, player_count, winner, onu, kick, \
cards0, cards1, cards2, cards3 \
FROM {table} WHERE game_num LIKE {ID}""",
    )

    if len(result) == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="row not found")

    keys = [
        "name0",
        "name1",
        "name2",
        "name3",
        "game_name",
        "turn",
        "direction",
        "age",
        "top_card",
        "draw",
        "player_count",
        "winner",
        "onu",
        "kick",
    ]

    json = {}
    for i in range(len(keys)):
        json.update({keys[i]: result[0][i]})

    for i in range(4):
        if result[0][i + len(keys)]=='':
            length=0
        else:
            length = len(result[0][i + len(keys)].split(",")) #- 1 #list fix
        json.update({f"len{i}": length})

    return json


@app.get("/public/{ID}")
def public(ID: int):

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    json = public_internal(connection, ID)

    connection.close()
    return json


def private_internal(connection, ID, uid, upswd=""):
    check_id_uid_range(ID, uid)
    check_user_pswd(connection, ID, uid, upswd)
    cards = read_query(connection,
        f"""SELECT cards{uid} FROM {table} WHERE game_num LIKE {ID}"""
    )[0][0]
    return cards



@app.get("/private/{ID},{uid}")
def private(ID: int, uid: int, upswd: Union[str, None] = ""):
    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    cards = private_internal(connection, ID, uid, upswd)

    connection.close()
    return {"cards": cards}


@app.post("/new_game/{game_name},{user_name}", status_code=201)
def new_game(game_name: str, user_name: str, upswd: Union[str, None] = "",gpswd: Union[str, None] = "" ):

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    next_num = read_query(connection, "SELECT `next_num`() AS `next_num`;")[0][0]
    # print(pswd)

    # hand = "" #list fix
    hand=[]
    for i in range(7):
        card = random.choice(deck[:-8])

        hand.append(card)
        # hand += "," #list fix

    sql = (
        f"""INSERT INTO `{table}` ("""
        f"""`cards0`, `name0`, `psword0`, """
        # f"""`name1`, `psword1`, """
        # f"""`name2`, `psword2`, """ # defaulted in db
        # f"""`name3`, `psword3`, """
        f"""`game_num`, `game_name`, `game_pswd`, `top_card`"""
        f""") VALUES ("""
    )
    for i in range(7):
        sql += "%s, "
    sql = sql[:-2]
    sql += ")"

    #     return(sql)

    values = (
        ','.join(hand),
        f"{user_name}",
        f"{pswd_hash(upswd)}",
        # "None",
        # "None",
        # "None",
        # "None",
        # "None",
        # "None",
        f"{next_num}",
        f"{game_name}",
        pswd_hash(gpswd),
        random.choice(deck[:-8]),
    )

    exec_query(connection, sql, values)

    connection.close()

    return {"ID": next_num}  # ,read_query(connection,sql2)


@app.put("/join/{GID},{uname}")
def join(GID: str, uname: str, upswd: str = "", gpswd: str = ""):

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")
    check_game_pswd(connection,GID,gpswd) #check that your are allowed to join room
    
    pub = public_internal(connection, GID)
    unames = []
    for i in range(4):
        unames.append(pub["name" + str(i)])
    
    check_game_is_active(connection, pub, allow_notfull=False)
    

    if "None" not in unames:
        connection.close()
        raise HTTPException(status_code=429, detail="no space to join")
    
    index = unames.index("None")

    read_query(
        connection,
        f"""UPDATE `{table}` SET `player_count` = '{pub['player_count']+1}' WHERE game_num LIKE {GID}""",
        True)

    read_query(
        connection,
        f"""UPDATE `{table}` SET `name{index}` = '{uname}' WHERE game_num LIKE {GID}""",
        True)

    read_query(
        connection,
        f"""UPDATE `{table}` SET `psword{index}` = '{pswd_hash(upswd)}' WHERE game_num LIKE {GID}""",
        True)

    hand = "" #list fix
    hnad=[]
    for i in range(7):
        card = random.choice(deck[:-8])
        hand.append(card)
        # hand += ","

    read_query(
        connection,
        f"""UPDATE `{table}` SET `cards{index}` = '{','.join(hand)}' WHERE game_num LIKE {GID}""",
        True)

    connection.close()
    return index

@app.put("/fountain/{ID}")
def young(ID: int):

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    #     outp=[]
    ### posibly only deage if winner is 0
    pub = public_internal(connection, ID)

    if pub["winner"] != 0:
        connection.close()
        raise HTTPException(
            status_code=432, detail=f"game over player{pub['winner']} won"
        )
    else:
        read_query(
            connection,
            f"""UPDATE `{table}` SET `age` = '0' WHERE game_num LIKE {ID}""",
            True,
        )
        connection.close()


def check_id_uid_range (GID, UID):
    if GID not in range(MAX_GID):
        # connection.close()
        raise HTTPException(status_code=422, detail="thats not a valid game ID")
    if UID not in range(MAX_UID):
        # connection.close()
        raise HTTPException(status_code=422, detail="thats not a valid user ID")

def check_game_is_active (connection, pub, allow_notfull=True):# trev thinks this shoud be =true not flase
    if pub["winner"] != 0:
        connection.close()
        raise HTTPException(
            status_code=432, detail=f"game over (player {pub['winner']}) won"
        )
    if allow_notfull and pub["player_count"] <= 1:
        connection.close()
        raise HTTPException(
            status_code=425, detail="bruh, you need some friends to play with"
        )

def check_pswd_internal (connection, GID, what, pswd):
    ps_hash ,= read_query(
        connection,
        f"""SELECT {what} FROM {table} WHERE game_num LIKE {GID}""",
    )[0]
    return pswd_hash(pswd) == ps_hash

def check_game_pswd (connection, GID, gpswd):
    if not check_pswd_internal(connection, GID,
                               "game_pswd", gpswd):
        connection.close()
        raise HTTPException(status_code=401, detail="passwd wrong")

def check_user_pswd (connection, GID, UID, upswd):
    if not check_pswd_internal(connection, GID,
                               f"psword{UID}", upswd):
        connection.close()
        raise HTTPException(status_code=401, detail="passwd wrong")

    


def valid_card(card, cards, draw, top_card, hand=False):
    # print(not (  # nand, only + cards can be played while an active stack
    #         draw  # draw stack >0
    #         and ("+" not in card # plus card is played
    #             or not card[2]>=top_card[2])  # playing a draw card
    #     ))
    # print(2, (  # and the card can be played
    #         card[0] == "B"  # if the card is wild
    #         or card[0] == top_card[0]  # if the color matches
    #         or card[1:] == top_card[1:]  # if the value matches
    #         or (  # card matches top card
    #             top_card[0] == "B"  # if the top card is wild
    #             and card[0] == top_card[-1]
    #         )  # the color matches
    #     ))
    valid = (
        (
            card in cards  # and the card is in your hand
            or hand  # or we already know it's in your hand
        )
        and not (  # nand, only + cards can be played while an active stack
            draw  # draw stack >0
            and ("+" not in card # plus card is played
                or not card[2]>=top_card[2])  # playing a draw card
        )
        and (  # and the card can be played
            card[0] == "B"  # if the card is wild
            or card[0] == top_card[0]  # if the color matches
            or card[1:] == top_card[1:]  # if the value matches
            or (  # card matches top card
                top_card[0] == "B"  # if the top card is wild
                and card[0] == top_card[-1]
            )  # the color matches
        )
    )

    # print(
    #     "valid",valid,
    #     "draw",draw,
    #     "top_card",top_card,
    #     "card",card,
    #      )

    return valid


@app.put("/draw/{ID},{uid}")
def draw(ID: int, uid: int, pswd: Union[str, None] = ""):
    check_id_uid_range(ID, uid)

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    check_user_pswd(connection, ID, uid, pswd)

    pub = public_internal(connection, ID)

    check_game_is_active(connection, pub)

    if uid != pub["turn"]:
        connection.close()
        raise HTTPException(status_code=425, detail="bruh, you can't play yet")
    else:

        hand = read_query(
            connection, f"""SELECT cards{uid} from `{table}` WHERE game_num LIKE {ID}"""
        )[0][0]

        hand = hand.split(",")
        # hand.remove("") #list fix
        for card in hand:
            if valid_card(card, hand, pub["draw"], pub["top_card"], hand=True):
                connection.close()
                raise HTTPException(
                    status_code=428, detail="bruh, you have cards you can play"
                )

        card = random.choice(deck)

        # cards += card
        # cards += ","
        hand.append(card)
        # hand.append("") #list fix

        # cards = ",".join(sorted(cards.split(",")))

        hand = ",".join(hand)
#         return cards,card

        read_query(
            connection,
            f"""UPDATE `{table}` SET `cards{uid}` = '{hand}' WHERE game_num LIKE {ID}""",
            True,
        )

        if not valid_card(card, cards, pub["draw"], pub["top_card"], hand=True):
            new_turn = (pub["turn"] + (pub["direction"] * 2 - 1)) % pub["player_count"]
            read_query(
                connection,
                f"""UPDATE `{table}` SET `turn` = '{new_turn}' WHERE game_num LIKE {ID}""",
                True,
            )

        # reset onu variable
        pub = public_internal(connection, ID)

        user_card_count = []
        for i in range(1, 5):
            user_card_count.append(pub["len" + str(i)])
            # print(user_card_count)

        onu_bin = bin(pub["onu"] + 16)[2:]
        onu_bin = list(onu_bin)

        # print(1,onu_bin)
        for user in range(4):
            if user_card_count[user] >= 2:
                # print(user)
                onu_bin[-user - 1] = "0"
                # print(2,onu_bin)

        onu = (
            int("".join(onu_bin), 2) - 16
        )  # convert the list to the number we want to store
        # print("stored",onu)
        read_query(
            connection,
            f"""UPDATE `{table}` SET `onu` = '{onu}' WHERE game_num LIKE {ID}""",
            True,
        )

    #         return card
    #         return {'cards':read_query(connection,f"""SELECT cards{uid} FROM uno2 WHERE game_num LIKE {ID}""")[0][0]}
    connection.close()

@app.put("/place_card/{ID},{uid},{card}")
def place_card(
    ID: int,
    uid: int,
    card: str,
    pswd: Union[str, None] = "",
    color: Union[str, None] = "",
):
    check_id_uid_range(ID, uid)

    connection = get_conn_from_pool()

    check_user_pswd(connection, ID, uid, pswd)
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    cards = private_internal(connection, ID, uid, pswd)
    print(cards)
    pub = public_internal(connection, ID)
    check_game_is_active(connection, pub)
    
    # print(card,cards)
    # print(f"""UPDATE `{table}` SET `cards{uid}` = '{cards}' WHERE game_num LIKE {ID}""")


    # if uid != pub["turn"]:
    #     connection.close()
    #     raise HTTPException(status_code=425, detail="bruh, you can't play yet")

    # elif pswd_hash(pswd) != ps_hash:
    #     connection.close()
    #     raise HTTPException(status_code=401, detail="passwd wrong")

    if not valid_card(card, cards, pub["draw"], pub["top_card"]):
        connection.close()
        raise HTTPException(status_code=400, detail=f"that card can't be played {card}, { cards}, {pub['draw']}, {pub['top_card']}")

    #         cards=cards.replace(card+',','')
    # rm card
    # cards = "".join(cards.split(card + ",", maxsplit=1))  #list fix
    card=cards.split(',')
    cards.remove(card)
    cards=','.join(cards)

    read_query(
        connection,
        f"""UPDATE `{table}` SET `cards{uid}` = '{cards}' WHERE game_num LIKE {ID}""",
        True)

    # add color to wilds
    #         card+=color
    # second idea
    if color != "":
        card = color + card[1:]

    read_query(
        connection,
        f"""UPDATE `{table}` SET `top_card` = '{card}' WHERE game_num LIKE {ID}""",
        True)

    if cards == "":
        read_query(
            connection,
            f"""UPDATE `{table}` SET `winner` = '{uid}' WHERE game_num LIKE {ID}""",
            True,
        )
        read_query(
            connection,
            f"""UPDATE `{table}` SET `age` = '6' WHERE game_num LIKE {ID}""",
            True,
        )

        # print(cards)

    if card[1:] == "r":
        read_query(
            connection,
            f"""UPDATE `{table}` SET `direction` = '{int(not pub['direction'])}' WHERE game_num LIKE {ID}""",
            True,
        )
        pub["direction"] = int(not pub["direction"])

    elif card[1] == "🛇" or card[1] == "s":
        # print("skipin")
        new_turn = (
            pub["turn"] + (pub["direction"] * 2 - 1) % pub["player_count"]
        )
        read_query(
            connection,
            f"""UPDATE `{table}` SET `turn` = '{new_turn}' WHERE game_num LIKE {ID}""",
            True,
        )
        pub["turn"] = new_turn

    elif card[1] == "+":
        new_turn = (pub["turn"] + (pub["direction"] * 2 - 1)) % pub["player_count"]

        # print(new_turn)
        read_query(
            connection,
            f"""UPDATE `{table}` SET `turn` = '{new_turn}' WHERE game_num LIKE {ID}""",
            True,
        )
        pub["turn"] = new_turn
        # print(new_turn)
        # temp remove turn change 4 testing

        cards = read_query(
            connection,
            f"""SELECT cards{new_turn} FROM `{table}` WHERE game_num LIKE {ID}""",
        )[0][0]
        #             cards=read_query(connection,f"""SELECT `cards{new_turn}` from `{table}` WHERE game_num LIKE {ID}""")[0][0]
        if f"+{card[2]}" in cards or "+4" in cards:
            # print("stack")
            read_query(
                connection,
                f"""UPDATE `{table}` SET draw = draw + {card[2]} WHERE game_num LIKE {ID}""",
                True,
            )
            pass
        else:
            # print("not stack")
            #                 draw=read_query(connection,f"""SELECT draw FROM `{table}` WHERE game_num LIKE {ID}""")[0][0]
            read_query(
                connection,
                f"""UPDATE `{table}` SET `draw` = '0' WHERE game_num LIKE {ID}""",
                True)
            #                 draw+=int(card[2])
            for i in range(pub["draw"] + int(card[2])):

                card = random.choice(deck)

                cards += card
                cards += ","

            read_query(
                connection,
                f"""UPDATE `{table}` SET `cards{new_turn}` = '{cards}' WHERE game_num LIKE {ID}""",
                True,
            )
            # add cards to new_turn player

    # need to check if a plus card was played, then dont add to turn
    if card[1] != "+":
        new_turn = (pub["turn"] + (pub["direction"] * 2 - 1)) % pub["player_count"]
        read_query(
            connection,
            f"""UPDATE `{table}` SET `turn` = '{new_turn}' WHERE game_num LIKE {ID}""",
            True,
        )

    # reset onu variable

    pub = public_internal(connection, ID)

    user_card_count = []
    for i in range(1, 5):
        user_card_count.append(pub["len" + str(i)])
        # print(user_card_count)

    onu_bin = bin(pub["onu"] + 16)[2:]
    onu_bin = list(onu_bin)

    # print(1,onu_bin)
    for user in range(4):
        if user_card_count[user] >= 2:
            # print(user)
            onu_bin[-user - 1] = "0"
            # print(2,onu_bin)

    onu = (
        int("".join(onu_bin), 2) - 16
    )  # convert the list to the number we want to store
    # print("stored", onu)
    read_query(
        connection,
        f"""UPDATE `{table}` SET `onu` = '{onu}' WHERE game_num LIKE {ID}""",
        True)
    # temp remove turn change 4 testing
    connection.close()

        

@app.put("/onu/{ID},{uid}")
def onu(ID: int, uid: int):
    check_id_uid_range(ID, uid)

    connection = get_conn_from_pool()
    # if not connection:
    #     connection.close()
    #     raise HTTPException(status_code=429,
    #         detail="uhh, the connection had an error")

    pub = public_internal(connection, ID)

    check_game_is_active(connection, pub)

    user_card_count = []
    for i in range(1, 5):
        user_card_count.append(pub["len" + str(i)])
        # print(user_card_count)

    onu_bin = bin(pub["onu"] + 16)[2:]

    onu_bin = list(onu_bin)

    # print(1,onu_bin)
    for user in range(MAX_UID):  # reset onu values
        if user_card_count[user] >= 2:
            # print(user)
            onu_bin[-user - 1] = "0"
        # print(2,onu_bin)

    if user_card_count[int(uid) - 1] in (1, 2):
        
        onu_bin[-int(uid)] = "1"
    # print(3, onu_bin)

    for user in range(4):

        if user_card_count[user] == 1 and onu_bin[-int(user) - 1] == "0":
            print("punish user", user + 1)

            cards = read_query(
                connection,
                f"""SELECT cards{user+1} FROM `{table}` WHERE game_num LIKE {ID}""",
            )[0][0]
            for i in range(2):

                card = random.choice(deck)

                cards += card
                cards += ","

            read_query(
                connection,
                f"""UPDATE `{table}` SET `cards{user+1}` = '{cards}' WHERE game_num LIKE {ID}""",
                True,
            )

        # print(onu_bin) # the onu values seperated to a list with a leading 1

    onu = (
        int("".join(onu_bin), 2) - 16
    )  # convert the list to the number we want to store
    # print("stored",onu)
    read_query(
        connection,
        f"""UPDATE `{table}` SET `onu` = '{onu}' WHERE game_num LIKE {ID}""",
        True,
    )

    #     onu_bin=bin(self.onu+16)[2:]
    # print(onu_bin)
    #     for user in range(3,0-1,-1):

    #         # onu=sonu//(user+1)==1
    #         count=self.user_card_count[user]
    # print(user+1,count,onu_bin[user])
    #         if onu_bin[user]==0 and count==1:
    #             press=True

    connection.close()
    pass

@app.put("/restart/{GID}")
def restart(GID,upswd: Union[str, None] = ""):
    check_id_uid_range(int(GID),0)
    connection = get_conn_from_pool()
    
    check_user_pswd(connection, GID, 0, upswd)

    result = list(read_query(
        connection,
        f"""\
SELECT cards0, cards1, cards2, cards3, player_count \
FROM {table} WHERE game_num LIKE {GID}""")[0])

    for uid in range(int(result[-1])):
        # result[uid] = ""  #list fix
        result[uid] = []
        for i in range(7):
            card = random.choice(deck[:-8])
            result[uid].append(card)
            # result[uid] += ","  #list fix
    # subQuerry= ', '.join([f"`cards{uid}` = '{result[uid]}'" for uid in range(4)])

    read_query(
        connection,
        f"""UPDATE `{table}` SET {', '.join(f"`cards{uid}` = '{result[uid]}'" for uid in range(4))} WHERE game_num LIKE {GID}""",
        True,
    )
    read_query(
        connection,
        f"""UPDATE `{table}` SET `turn` = 0, `direction` = 1, `winner` = 0, `draw` = 0, `onu` = 0, `top_card` = '{random.choice(deck[:-8])}' WHERE game_num LIKE {GID}""",
        True,
    )
    connection.close()
    

def removeUser(ID, uid):
    check_id_uid_range(ID, uid)
    connection = get_conn_from_pool()
    
    result = read_query(
        connection,
        f"""\
SELECT name0, name1, name2, name3, \
cards0, cards1, cards2, cards3 \
player_count, winner, onu, kick, \
FROM {table} WHERE game_num LIKE {ID}""",
    )

    if len(result) == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="row not found")

    keys = [
        "name0",
        "name1",
        "name2",
        "name3",
        "cards0",
        "cards1",
        "cards2",
        "cards3",
        "player_count",
        "winner",
        "onu",
        "kick",
    ]

    json = {}
    for i in range(len(keys)):
        json.update({keys[i]: result[0][i]})

    names = json[:4]
    cards = json[4:8]
    values = [int(i) for i in json[8:12]]

    names.pop(uid)
    names.append("None")

    cards.pop(uid)
    names.append("")

    values[0] -= 1
    values[1] = max(values[1] - 1, 0)

    l = list(bin(values[2])[3:])
    l.pop(uid)
    values[2] = int("".join(l + ["0"]), 2)

    values[3] = 0
    # json['player_count']-=1
    # json['winner']=max(json['winner']-1,0)
    # # json['uno']=
    # # how to chop a bit - ? 4 max
    # json['kick']=0

    connection.close()


def leave(ID: int, uid: int, pswd: Union[str, None] = ""):
    pass


def voteKick(ID: int, uid: int, target: int, pswd: Union[str, None] = ""):
    check_id_uid_range(ID, uid)
    connection = get_conn_from_pool()
    check_user_pswd(connection, ID, uid, pswd)
    
    if target not in (1, 2, 3, 4):
        connection.close()
        raise HTTPException(status_code=422, detail="thats not a valid target")

    pub = public_internal(connection, ID)

    # print(card,cards)
    # print(f"""UPDATE `{table}` SET `cards{uid}` = '{cards}' WHERE game_num LIKE {ID}""")

    # onu_bin = bin(pub["onu"] + 16)[2:]

    # onu_bin = list(onu_bin)
    kick = int(pub["kick"])

    _stored = kick // 8 + 1
    if uid == target:
        connection.close()
        raise HTTPException(status_code=422, detail="you can't vote 4 yourself")

    elif _stored == target:
        # increase vote count

        place = uid - (uid > target)

        kick |= 0b1 << (place - 1)
        # print(bin(kick))
        if kick % 8 == 0b111:
            removeUser(ID, _stored)
        else:
            read_query(
                connection,
                f"""UPDATE `{table}` SET `kick` = '{kick}' WHERE game_num LIKE {ID}""",
                True,
            )

        pass

    elif (
        _stored != uid or kick == 0
    ):  # your not the current person stored as targeted
        kick = target * 8 - 8  # target is set
        # place=[1,2,3,4]
        # place.remove(target)
        # place=place.index(uid)
        # print(place)
        place = uid - (uid > target)
        # print(type(bin(kick+32)))
        # new=list(bin(kick+32)[3:])

        # new[-place]='1'
        # # and vote is now 1

        # kick = (
        #     int("".join(new), 2)
        # )
        kick |= 0b1 << (place - 1)
        # print(bin(kick))
        read_query(
            connection,
            f"""UPDATE `{table}` SET `kick` = '{kick}' WHERE game_num LIKE {ID}""",
            True,
        )
        pass

    else:
        connection.close()
        raise HTTPException(status_code=422, detail="you're curentley voted on")
    connection.close()
    return



@app.get("/ping")
def ping():
    return "i'm alive"


app.mount("/", StaticFiles(directory="./static"), name="favicon.ico")


print("finished start")


# uvicorn main:app --reload --host 0.0.0.0 --port 8096 --ssl-keyfile ~/Documents/lets/pk.pem --ssl-certfile ~/Documents/lets/ce.pem --log-config logging.conf
#
