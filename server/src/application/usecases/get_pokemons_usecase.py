from src.infrastructure.services.pokemon_service import PokemonService

class GetPokemonsUseCase:
  def __init__(self, pokemon_service: PokemonService):
    self.pokemon_service = pokemon_service

  async def execute(self, offset, limit):
    return await self.pokemon_service.list_pokemons(offset, limit)
