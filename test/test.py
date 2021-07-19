import mysql.connector
import datetime



def connectBdd():
    config = {
    'user': 'root',
    'password': 'root',
    'port': 8889,
    'host': '127.0.0.1',
    'database': 'iot_nexus',
    }

    cnx = mysql.connector.connect(**config)

    return cnx

def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start < y.stop and y.start < x.stop


def isNotBook(nameSalle, start, end):
    #get data
    bdd = connectBdd()

    mycursor = bdd.cursor(prepared=True)
    
    stmt = """SELECT * FROM room INNER JOIN booking ON room.id_room = booking.id_room WHERE room.nameRoom = %s"""

    mycursor.execute(stmt, (nameSalle,))

    columns = mycursor.description 

    allReservation = [{columns[index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]

    bdd.close()

    

    for i in range(len(allReservation)):
        isOverlap = range_overlapping(range(allReservation[i]["start"], allReservation[i]["end"]), range(int(start), int(end)))
        if isOverlap:
            return False

        
    return True
    # if(myresult[0]["isReserve"] == 0):
    #     return True
    # else: 
    #     isOverlap = range_overlapping(range(myresult[0]["start"], myresult[0]["end"]), range(int(start), int(end)))
    #     if isOverlap:
    #         return False
    #     else:
    #         return True

        
        
def getIdRoomBYRoomName(nameRoom):
    bdd = connectBdd()
    
    mycursor = bdd.cursor(prepared=True)
    
    stmt = """SELECT id_room FROM room WHERE nameRoom = %s"""
    
    mycursor.execute(stmt, (nameRoom,))
    
    id_room = [{mycursor.description[index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]
    
    return id_room[0]['id_room']
    
    


print(getIdRoomBYRoomName("A105"))