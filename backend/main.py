from flask import request, jsonify
from config import app, db 
from models import Contact 

@app.route("/contacts", methods=["GET"])    #decorator 
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "Must include first_name, last_name, and email"}), 400
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try: 
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e: 
        return jsonify({"message": str(e)}), 400    #didn't work
    
    return jsonify({"message": "Contact created successfully"}), 201    #201 success

#update contact 
@app.route("/update_contact/<int:contact_id>", methods=["PATCH"])
def update_contact(contact_id): 
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404   #404 not found
    
    data = request.json
    contact.first_name = data.get("firstname", contact.first_name) #modify contact firstname to new data otherwise return original
    contact.last_name = data.get("lastname", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "Contact updated successfully"}), 201


#delete contact
@app.route("/delete_contact/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)