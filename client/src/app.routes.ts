import { Routes } from '@angular/router';
import { PokemonDetailsComponent } from './application/pokemon.details.component';
import { PokemonsComponent } from './application/pokemon.component';

export const routes: Routes = [
  { path: "pokemon/:name", component: PokemonDetailsComponent },
  { path: 'pokemons', component: PokemonsComponent },
];
