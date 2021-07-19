import json
import os 
import mysql.connector
import datetime

def getIdRoomBYRoomName(nameRoom):
    bdd = connectBdd()
    
    mycursor = bdd.cursor(prepared=True)
    
    stmt = """SELECT id_room FROM room WHERE nameRoom = %s"""
    
    mycursor.execute(stmt, (nameRoom,))
    
    id_room = [{mycursor.description[index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]
    
    return id_room[0]['id_room']
    
def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start < y.stop and y.start < x.stop

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

    

def getJson():
    now = datetime.datetime.now()
    actualHour = now.hour
    bdd = connectBdd()

    mycursor = bdd.cursor(prepared=True)

    mycursor.execute("SELECT * FROM room") 

    Allrooms = [{mycursor.description [index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]

    for i in range(len(Allrooms)):

        stmt = "SELECT * FROM room INNER JOIN booking ON room.id_room = booking.id_room WHERE room.id_room = %s"
        mycursor.execute(stmt, (Allrooms[i]["id_room"],))
        roomInfo = [{mycursor.description [index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]

        if(len(roomInfo) > 0):

            for y in range(len(roomInfo)):
                if roomInfo[y]["start"] <= actualHour <= roomInfo[y]["end"]:
                    Allrooms[i]["isBooked"] = 1
                else:
                    Allrooms[i]["isBooked"] = 0

        else:
            Allrooms[i]["isBooked"] = 0

    bdd.close()
    return Allrooms


def bookARoom(nameSalle, start, end, studentMail):

    if isNotBook(nameSalle, start, end):

        bdd = connectBdd()

        mycursor = bdd.cursor(prepared=True)

        stmt = """INSERT INTO booking(id_room, start, end, studentEmail) VALUES(%s,%s,%s,%s)"""

        mycursor.execute(stmt, (getIdRoomBYRoomName(nameSalle),start, end, studentMail)) 

        bdd.commit()

        bdd.close()

        return mycursor.rowcount, "record(s) affected"
    else:
        return "room already booked"

def getBookingOfARoom(nameRoom):
    bdd = connectBdd()

    mycursor = bdd.cursor(prepared=True)

    stmt = "SELECT * FROM room INNER JOIN booking ON room.id_room = booking.id_room WHERE room.id_room = %s"
    
    mycursor.execute(stmt, (getIdRoomBYRoomName(nameRoom),))
    
    roomInfo = [{mycursor.description [index][0]:column for index, column in enumerate(value)} for value in mycursor.fetchall()]
    
    bdd.close()

    if len(roomInfo) == 0:
        return "no booking yet"

    return roomInfo