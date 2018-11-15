from flask import Flask, jsonify, request
app = Flask(__name__)

# Empty lists where delivery orders are to be POSTED OR GOT

parcels = []    

# Creating the END POINT for User can create a delivery
 
@app.route('/api/v1/parcels', methods=['POST'])
def create_parcel_order():

    parcel_order = {
        'parcelId': len(parcels)+1,
        'name': request.json['name'],
        'pickup': request.json['pickup'],
        'destination': request.json['destination'],
        'price': request.json['price'],
        'status': request.json['status']
        }

    parcels.append(parcel_order)
    return jsonify({'parcel_order': parcel_order})

@app.route('/api/v1/parcels/<int:parcelId>', methods = ['GET'])
def get_specific_order(parcelId):
    for parcel_order in parcels:
        if parcel_order['parcelId'] == parcelId:
            return jsonify({'parcel_order': parcel_order})
    return jsonify({'message': 'There are no parcel orders'})

   


# This is the END POINT for USER can get all parcels

@app.route('/api/v1/parcels', methods =['GET'])
def get_all():
    return jsonify({'parcels':parcels})

# This is the PUT endpoint for user can Cancel/update status of parcel

@app.route('/api/v1/parcels/<int:parcelId>', methods = ['PUT'])
def update_order(parcelId):
    for parcel_order in parcels:
        if parcel_order['parcelId'] == parcelId:
           parcel_order['status'] = request.json['status']
           return jsonify({'message': 'list been updated succesfully'})
        



if __name__ == '__main__':
    app.run(debug=True)

