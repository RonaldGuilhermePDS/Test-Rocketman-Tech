from pydantic import BaseModel
from typing import Dict

class IPokemon(BaseModel):
  name: str
  height: int
  weight: int
  types: list[str]
  abilities: list[str]
  sprites: Dict[str, Dict[str, Dict[str, str]]] = {
    'other': {
      'official-artwork': {
        'front_default': str
      }
    }
  }
