from fastapi import HTTPException
from httpx import AsyncClient
from asyncio import Semaphore, gather

class PokemonService:
  def __init__(self):
    self.pokemon_list = []
    self.semaphore = Semaphore(20)

  async def fetch_pokemons_data(self, offset=0, limit=20):
    async with self.semaphore:
       async with AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}")

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error on fetch pokemons data")

        data = response.json()

        return data["results"]

  async def list_pokemons(self, offset: int = 0, limit: int = 20):
    pokemons = await self.fetch_pokemons_data(offset, limit)

    tasks = [self.fetch_pokemons_details(pokemon["name"]) for pokemon in pokemons]
    results = await gather(*tasks)

    self.pokemon_list = sorted(results, key=lambda x: x["name"])

    return self.pokemon_list

  async def fetch_pokemons_details(self, pokemon_name: str):
    async with self.semaphore:
      async with AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokemon not found")

        data = response.json()

        return data
