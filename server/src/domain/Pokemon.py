from pydantic import BaseModel
from typing import Dict

class IPokemon(BaseModel):
  name: str
  height: int
  weight: int
  types: Dict[str, Dict[str, str]]
  abilities: Dict[str, Dict[str, str]]
  sprites: Dict[str, Dict[str, Dict[str, str]]] = {
    'other': {
      'official-artwork': {
        'front_default': str()
      }
    }
  }
