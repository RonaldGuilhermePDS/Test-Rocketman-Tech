from src.application.usecases.get_pokemons_usecase import GetPokemonsUseCase

class GetPokemonsController:
  def __init__(self, get_pokemon_usecase: GetPokemonsUseCase):
    self.get_pokemon_usecase = get_pokemon_usecase

  async def handle(self, offset, limit):
    return await self.get_pokemon_usecase.execute(offset, limit)
