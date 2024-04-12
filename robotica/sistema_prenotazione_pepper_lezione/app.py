from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista per memorizzare le prenotazioni
bookings = []

@app.route('/booking', methods=['POST'])
def handle_booking():
    # Ricezione e decodifica dei dati JSON inviati dalla pagina HTML
    data = request.get_json()
    # Aggiunta della prenotazione alla lista
    bookings.append(data)
    # Stampa di conferma nel log del server
    print("Prenotazione ricevuta:", data)
    # Risposta JSON di successo inviata al client
    return jsonify({"message": "Prenotazione effettuata con successo!"}), 200

if __name__ == '__main__':
    # Avvio del server Flask sulla porta 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
