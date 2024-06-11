import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app.config';
import { PokemonsComponent } from './application/pokemon.component';

bootstrapApplication(PokemonsComponent, appConfig)
  .catch((err) => console.error(err));
