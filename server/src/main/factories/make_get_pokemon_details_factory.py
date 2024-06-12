from src.application.usecases.get_pokemon_details_usecase import GetPokemonDetailsUseCase
from src.infrastructure.services.pokemon_service import PokemonService
from src.presentation.controllers.get_pokemon_details_controller import GetPokemonDetailsController

def MakeGetPokemonDetailsFactory():
  service = PokemonService()
  usecase = GetPokemonDetailsUseCase(service)
  controller = GetPokemonDetailsController(usecase)

  return controller
