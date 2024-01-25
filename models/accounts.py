from omv.db import db
from dataclasses import dataclass

@dataclass
class Accounts(db.Model):
   id: int
   email: str
   encrypted_password: str

   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(256), unique=True)
   encrypted_password = db.Column(db.String(256), unique=True)