import { Component, OnInit } from '@angular/core';

import { IPokemon } from '../domain/pokemon.model';
import { PokemonService } from '../infrastructure/services/pokemon_service';
import { ActivatedRoute } from '@angular/router';
import { map } from 'rxjs';
import { CommonModule, NgOptimizedImage } from '@angular/common';

@Component({
  standalone: true,
    imports: [CommonModule, NgOptimizedImage],
    selector: 'app-pokemon-details',
    templateUrl: './pokemon.details.component.html',
})
export class PokemonDetailsComponent implements OnInit {
    pokemon: IPokemon = {} as IPokemon;
    notFound: boolean = false;

    constructor(
      private activatedRoute: ActivatedRoute,
      private pokemonService: PokemonService
    ) {}

    ngOnInit(): void {
      const name = this.activatedRoute.params.pipe(map((params) => params['name']));

      if (!name) {
        this.notFound = true;
      }

      name.subscribe((name: string) => this.getPokemonDetails(name));
    }

    getPokemonDetails(name: string): void {
      this.pokemonService
      .getPokemonDetails(name)
      .subscribe((pokemon) => {
        this.pokemon = pokemon;
      });
    }
}
