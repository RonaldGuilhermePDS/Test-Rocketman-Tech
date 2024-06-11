export interface IPokemon {
  name: string;
  height: number;
  weight: number;
  types: string[];
  abilities: string[];
  sprites: {
    other: {
      'official-artwork': {
        front_default: string;
      };
    };
  };
}
