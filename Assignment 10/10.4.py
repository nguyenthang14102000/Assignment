from flask import Flask
import json
import mysql.connector
app = Flask(__name__)
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="your_username",
    password="your_password",
    autocommit=True
)
@app.route('/airport/<icao>')
def get_airport(icao):
    sql = "SELECT ident, name, municipality, iso_country FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    if result:
        response = {
            "icao": result[0],
            "name": result[1],
            "city": result[2],
            "country": result[3]
        }
        return json.dumps(response)
    else:
        error_message = {
            "error": "Airport not found"
        }
        return json.dumps(error_message), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)