import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule, NgOptimizedImage } from '@angular/common';
import { IPokemon } from '../domain/pokemon.model';
import { PokemonService } from '../infrastructure/services/pokemon_service';
import { saveAs } from 'file-saver';

import { HlmSpinnerComponent } from '@spartan-ng/ui-spinner-helm';
import { firstValueFrom } from 'rxjs';

@Component({
  standalone: true,
  imports: [CommonModule, NgOptimizedImage, HlmSpinnerComponent],
  selector: 'app-pokemons',
  templateUrl: './pokemons.component.html',
})
export class PokemonsComponent implements OnInit {
  pokemons: IPokemon[] = [];
  offset: number = 0;
  limit: number = 20;
  globalLoading: boolean = false;
  loadMoreLoading: boolean = false;

  constructor(
    private route: Router,
    private pokemonService: PokemonService,
  ) {}

  async ngOnInit(): Promise<void> {
    this.globalLoading = true;
    await this.fetchPokemons()
    this.globalLoading = false
  }

  async fetchPokemons(): Promise<any> {
    const pokemons = await firstValueFrom(this.pokemonService.listPokemons(this.offset, this.limit));

    this.pokemons = this.pokemons.concat(pokemons);
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

  async loadMore(): Promise<void> {
    this.offset += this.limit;

    this.loadMoreLoading = true;
    await this.fetchPokemons();
    this.loadMoreLoading = false
  }

  viewPokemonDetails(name: string): void {
    this.route.navigate(['/pokemon', name]);
  }
}
