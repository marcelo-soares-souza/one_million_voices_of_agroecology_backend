from omv.db import db
from dataclasses import dataclass

@dataclass
class Practices(db.Model):
  id: int
  name: str

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(256), unique=True)