from fastapi import FastAPI, Depends

from infrastructure.services.pokemon_service import PokemonService

app = FastAPI()

pokemon_service = PokemonService()

@app.get("/pokemons")
async def get_pokemons (
  offset: int = 0,
  limit: int = 20,
  pokemon_service: PokemonService = Depends()
):
  return await pokemon_service.list(offset, limit)
