import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule, NgOptimizedImage } from '@angular/common';
import { IPokemon } from '../domain/pokemon.model';
import { PokemonService } from '../infrastructure/services/pokemon_service';
import { saveAs } from 'file-saver';

import { HlmSpinnerComponent } from '@spartan-ng/ui-spinner-helm';

@Component({
  standalone: true,
  imports: [CommonModule, NgOptimizedImage, HlmSpinnerComponent],
  selector: 'app-pokemons',
  templateUrl: './pokemon.component.html',
})
export class PokemonsComponent implements OnInit {
  pokemons: IPokemon[] = [];
  offset: number = 0;
  limit: number = 20;
  loading: boolean = false;

  constructor(
    private route: Router,
    private pokemonService: PokemonService,
  ) {}

  ngOnInit(): void {
    this.fetchPokemons();
  }

  fetchPokemons(): void {
    this.loading = true
    this.pokemonService.listPokemons(this.offset, this.limit).subscribe(
      (data: any) => {
        this.pokemons = [...this.pokemons, ...data];
        this.loading = false;
      },
    );
  }

  getPokemonDetails(pokemonName: string): void {
    this.pokemonService.getPokemonDetails(pokemonName).subscribe(
      (data: any) => {
        console.log("Pokemon Details: ", data);
      },
    );
  }

  exportPokemons(): void {
    this.pokemonService.exportPokemons(this.pokemons).subscribe(
      (response: any) => {
        const blob = new Blob([response], { type: 'application/xml' });
        saveAs(blob, 'pokemons.xml');
      },
    );
  }

  loadMore(): void {
    this.offset += this.limit;
    this.fetchPokemons();
  }

  viewPokemonDetails(name: string): void {
    this.route.navigate(['/pokemon', name]);
  }
}
