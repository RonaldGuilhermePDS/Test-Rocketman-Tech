from src.infrastructure.services.pokemon_service import PokemonService

class GetPokemonDetailsUseCase:
  def __init__(self, pokemon_service: PokemonService):
    self.pokemon_service = pokemon_service

  async def execute(self, pokemon_name):
    return await self.pokemon_service.fet_pokemon_details(pokemon_name)
