# iot_lumino_api

## documentation
pour lister les salle et voir lesquelles sont reserver a l'heure actuelle :

    method : get
	    apiURL/getAllRoom

pour reserver une salle :

    method : post
    params = {
        nameRoom: str
        start: int
        end: int
        studentEmail: str
    }
	    apiURL/bookaroom

pour voir les reservation d'une salle

    method : get
        
        apiUrl/getAllBookingFromARoom/<str:nameRoom>
pour sup un rerservation: 

    method : get
        
        apiUrl/removeABooking/<string:idBooking>


pour checker en detail les plage horaire dispo 

    method : get
        
        apiUrl/getBookingByRoomId/<string:idRoom>'

pour avoir les info d'une salle
   
	method : get        
        	apiUrl//getRoomInfoByIdRoom/<string:idRoom>'



