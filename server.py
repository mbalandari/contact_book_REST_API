from flask import Flask, request

app = Flask(__name__)


contacts = [
    {"name": "Maz", "phone": "123-456-7890", "id": "1"},
    {"name": "Sarah", "phone": "547-456-7890", "id": "2"},
    {"name": "John", "phone": "463-456-7890", "id": "3"},
    {"name": "Nancy", "phone": "999-456-7890", "id": "4"},
]

next_id = 5
