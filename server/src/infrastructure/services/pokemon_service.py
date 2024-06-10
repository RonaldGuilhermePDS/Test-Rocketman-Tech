from fastapi import HTTPException
from httpx import AsyncClient

class PokemonService:
  def __init__(self):
    self.pokemon_list = []

  async def fetch(self, offset=0, limit=20):
    async with AsyncClient() as client:
      response = await client.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}")

      if response.status_code != 200:
          raise HTTPException(status_code=400, detail="Error on fetch pokemons")

      data = response.json()

      return data["results"]

  async def list(self, offset: int = 0, limit: int = 20):
    data = await self.fetch(offset, limit)

    self.pokemon_list = sorted(data, key=lambda x: x["name"])

    return self.pokemon_list

  async def get_details(self, pokemon_name: str):
    async with AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        data = response.json()

        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]]
        }
