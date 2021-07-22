# iot_lumino_api

## documentation

Pour lister les salle et voir lesquelles sont réservées à l'heure actuelle :

    method : get
	    apiURL/getAllRoom

Pour réserver une salle :

    method : post
    params = {
        nameRoom: str
        start: int
        end: int
        studentEmail: str
    }
	    apiURL/bookaroom

Pour voir les réservations d'une salle :

    method : get
        
        apiUrl/getAllBookingFromARoom/<str:nameRoom>
	
Pour supprimer une réservation :

    method : get
        
        apiUrl/removeABooking/<string:idBooking>

Pour avoir les plages horaires disponibles à la réservation pour une salle précise :

    method : get
        
        apiUrl/getBookingByRoomId/<string:idRoom>'

Pour avoir les informations d'une salle :
   
	method : get        
        	apiUrl//getRoomInfoByIdRoom/<string:idRoom>'



