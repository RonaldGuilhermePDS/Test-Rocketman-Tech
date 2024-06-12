from src.application.usecases.get_pokemon_details_usecase import GetPokemonDetailsUseCase

class GetPokemonDetailsController:
  def __init__(self, get_pokemon_details_usecase: GetPokemonDetailsUseCase):
    self.get_pokemon_details_usecase = get_pokemon_details_usecase

  async def handle(self, pokemon_name):
    return await self.get_pokemon_details_usecase.execute(pokemon_name)
