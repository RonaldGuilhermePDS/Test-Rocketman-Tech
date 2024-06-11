from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.services.pokemon_service import PokemonService

app = FastAPI()

pokemon_service = PokemonService()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
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

@app.get("/pokemons/export")
async def export_pokemons():
    from xml.etree import ElementTree as ET

    root = ET.Element("Pokemons")

    pokemons = await pokemon_service.list_pokemons(0, 20)

    for pokemon in pokemons:
        pokemon_elem = ET.SubElement(root, "Pokemon")
        ET.SubElement(pokemon_elem, "Name").text = pokemon["name"]
        ET.SubElement(pokemon_elem, "Height").text = str(pokemon["height"])
        ET.SubElement(pokemon_elem, "Weight").text = str(pokemon["weight"])
        ET.SubElement(pokemon_elem, "Types").text = ", ".join(pokemon["types"])
        ET.SubElement(pokemon_elem, "Abilities").text = ", ".join(pokemon["abilities"])
        ET.SubElement(pokemon_elem, "sprites").text = ", ".join(pokemon["sprites"])

    tree = ET.ElementTree(root)

    with open("pokemons.xml", "wb") as f:
        tree.write(f)

    return {"message": "Export Successful"}
