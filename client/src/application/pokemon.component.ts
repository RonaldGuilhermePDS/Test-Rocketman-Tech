import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgFor } from '@angular/common';
import { IPokemon } from '../domain/pokemon.model';
import { PokemonService } from '../infrastructure/services/pokemon_service';
import { saveAs } from 'file-saver';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NgFor],
  templateUrl: './pokemon.component.html',
})
export class PokemonsComponent implements OnInit {
  pokemons: IPokemon[] = [];
  offset: number = 0;
  limit: number = 20;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.fetchPokemons();
  }

  fetchPokemons(): void {
    this.pokemonService.listPokemons(this.offset, this.limit).subscribe(
      (data: any) => {
        this.pokemons = data;
      },
      (error: any) => {
        console.error("Error on fetch pokemons:", error);
      }
    );
  }

  getPokemonDetails(pokemonName: string): void {
    this.pokemonService.getPokemonDetails(pokemonName).subscribe(
      (data: any) => {
        console.log("Pokemon Details: ", data);
      },
      (error: any) => {
        console.error("Error on get pokemon details:", error);
      }
    );
  }

  exportPokemons(): void {
    this.pokemonService.exportPokemons().subscribe(
      (response: any) => {
        const blob = new Blob([response], { type: 'application/xml' });
        saveAs(blob, 'pokemons.xml');
      },
      (error: any) => {
        console.error("Error on Export Pokemons", error);
      }
    );
  }

  nextPage(): void {
    this.offset += this.limit;
    this.fetchPokemons();
  }

  previousPage(): void {
    if (this.offset > 0) {
      this.offset -= this.limit;
      this.fetchPokemons();
    }
  }
}
