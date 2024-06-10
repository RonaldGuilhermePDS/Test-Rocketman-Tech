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

@app.get("/pokemons/details/{pokemon_name}")
async def get_pokemon_details(
  pokemon_name: str,
  pokemon_service: PokemonService = Depends()
):
  return await pokemon_service.get_details(pokemon_name)

@app.get("/pokemons/export")
async def export_pokemons(
   pokemon_service: PokemonService = Depends()
):
    from xml.etree import ElementTree as ET

    root = ET.Element("Pokemons")

    pokemons = await pokemon_service.list(0, 20)

    for pokemon in pokemons:
        details = await pokemon_service.get_details(pokemon['name'])

        pokemon_elem = ET.SubElement(root, "Pokemon")

        ET.SubElement(pokemon_elem, "Name").text = details["name"]
        ET.SubElement(pokemon_elem, "Height").text = str(details["height"])
        ET.SubElement(pokemon_elem, "Weight").text = str(details["weight"])
        ET.SubElement(pokemon_elem, "Types").text = ", ".join(details["types"])
        ET.SubElement(pokemon_elem, "Abilities").text = ", ".join(details["abilities"])

    tree = ET.ElementTree(root)

    with open("pokemons.xml", "wb") as f:
        tree.write(f)

    return {"message": "Export Successful"}
