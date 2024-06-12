from src.application.usecases.get_pokemons_usecase import GetPokemonsUseCase
from src.infrastructure.services.pokemon_service import PokemonService
from src.presentation.controllers.get_pokemons_controller import GetPokemonsController

def MakeGetPokemonsFactory():
  service = PokemonService()
  usecase = GetPokemonsUseCase(service)
  controller = GetPokemonsController(usecase)

  return controller
