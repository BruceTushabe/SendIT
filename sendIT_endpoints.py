from flask import Flask, jsonify, request
app = Flask(__name__)

# Empty list where parcels are to be POSTED OR GOT

parcels = []
    
# Creating the END POINT for USER can add a parcel order
 

@app.route('/api/v1/parcels', methods=['POST'])
def create_parcel_delivery_order():
    parcel = {
        'parcelId': len(parcels)+1,
        'name': request.json['name'],
        'price':  request.json['price'],
        'pickup':request.json['pickup'],
        'destination':request.json['destination']
        }

    parcels.append(parcel)
    return jsonify({'parcel': parcel})

    # This is the END POINT for USER can get all parcels

@app.route('/api/v1/parcels', methods =['GET'])
def get_all():
    return jsonify({'parcels':parcels})


    # In this endpoint, a user is able to get one specific parcel order 

@app.route('/api/v1/parcels/<int:parcelId>', methods = ['GET'])
def get_specific_order(parcelId):
    for parcel_order in parcels:
        if parcel_order['parcelId'] == parcelId:
            return jsonify({'parcel_order': parcel_order})
    return jsonify({'message': 'There are no parcel orders'})





if __name__ == '__main__':
    app.run(debug=True)


