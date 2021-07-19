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
        email: str
    }
	    apiURL/bookaroom

pour voir les reservation d'une salle

    method : get
        
        apiUrl/getAllBookingFromARoom/<str:nameRoom>
