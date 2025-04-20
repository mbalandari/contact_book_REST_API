from flask import Flask, request

app = Flask(__name__)


contacts = [
    {"name": "Maz", "phone": "123-456-7890", "id": "1"},
    {"name": "Sarah", "phone": "547-456-7890", "id": "2"},
    {"name": "John", "phone": "463-456-7890", "id": "3"},
    {"name": "Nancy", "phone": "999-456-7890", "id": "4"},
]

next_id = 5


@app.route("/")
def home():
    print("I've received a request on the homepage endpoint!")
    return "<h1 style='color:green'>Contact List</h1> <hr> </br> <a href='/contacts'>The list</a>"


# Read of cRud
@app.get("/contacts")
def list_contacts():
    return contacts


# Read of cRud
@app.get("/contacts/<id>")
def read_single_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact

    return "That contact does not exist!"


# Create of Crud
@app.post("/contacts")
def create_contact():
    global next_id
    new_contact = {
        "name": request.json["name"],
        "phone": request.json["phone"],
        "id": f"{next_id}",
    }
    contacts.append(new_contact)
    next_id += 1
    return new_contact


# Update of crUd
@app.put("/contacts/<id>")
def update_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contact["name"] = (
                request.json["name"] if "name" in request.json else contact["name"]
            )
            contact["phone"] = (
                request.json["phone"] if "phone" in request.json else contact["phone"]
            )
            return contact
    return "There is no contact with that id!"


# Delete of cruD
@app.delete("/contacts/<id>")
def delete_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            contacts.remove(contact)
            return contact
    return "There is no contact with that id!"


if __name__ == "__main__":
    app.run(debug=True)
