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


# cRud
@app.get("/contacts")
def list_contacts():
    return contacts


# cRud
@app.get("/contacts/<id>")
def read_single_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact

    return "That contact does not exist!"


if __name__ == "__main__":
    app.run(debug=True)
