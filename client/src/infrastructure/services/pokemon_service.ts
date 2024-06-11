import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PokemonService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  listPokemons(offset: number, limit: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/pokemons/?offset=${offset}&limit=${limit}`);
  }

  getPokemonDetails(pokemonName: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/pokemons/details/${pokemonName}`);
  }

  exportPokemons(): Observable<any> {
    return this.http.get(`${this.apiUrl}/pokemons/export`, {
      responseType: 'blob',
    });
  }
}
