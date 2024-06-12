import { Routes } from '@angular/router';
import { PokemonDetailsComponent } from './presentation/pokemon.details.component';
import { PokemonsComponent } from './presentation/pokemon.component';

export const routes: Routes = [
  { path: "pokemon/:name", component: PokemonDetailsComponent },
  { path: 'pokemons', component: PokemonsComponent },
  { path: '', redirectTo: '/pokemons', pathMatch: 'full' }
];
