import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IPokemon } from '../../domain/pokemon.model';

@Injectable({
  providedIn: 'root',
})
export class PokemonService {
  private apiUrl = 'http://localhost:4300';

  constructor(private http: HttpClient) {}

  listPokemons(offset: number, limit: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/pokemons?offset=${offset}&limit=${limit}`);
  }

  getPokemonDetails(pokemonName: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/pokemons/details/${pokemonName}`);
  }

  exportPokemons(pokemons: IPokemon[]): Observable<any> {
    return this.http.post(`${this.apiUrl}/pokemons/export`, { pokemons }, { responseType: 'blob' });
  }
}
