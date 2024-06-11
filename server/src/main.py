from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.services.pokemon_service import PokemonService

import io
import yaml

app = FastAPI()

pokemon_service = PokemonService()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
)

@app.get("/pokemons")
async def get_pokemons (
  offset: int = 0,
  limit: int = 20,
):
  return await pokemon_service.list_pokemons(offset, limit)

@app.get("/pokemons/details/{pokemon_name}")
async def get_pokemon_details(
  pokemon_name: str,
):
  return await pokemon_service.fetch_pokemons_details(pokemon_name)

@app.post("/pokemons/export")
async def export_pokemons(body: dict):
  pokemons = body['pokemons']

  yaml_string = yaml.dump(pokemons, allow_unicode=True)

  buffer = io.BytesIO()
  buffer.write(yaml_string.encode('utf-8'))
  buffer.seek(0)

  response = Response(content=buffer.read(), media_type='application/x-yaml')

  return response
