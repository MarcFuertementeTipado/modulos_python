#!/usr/bin/env python3
from pydantic import BaseModel, Field  # type: ignore
from datetime import datetime
from modulo_09.ex2.data_generator import DataConfig, SpaceStationGenerator


class space_station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)

    crew_size: int = Field(ge=1, le=20)

    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    last_maintenance: datetime

    is_operational: bool = Field(default=True)

    notes: str | None = Field(max_length=200)

    def show(self) -> None:
        print("\nStation information:")
        print(f"ID: {self.station_id}\n"
              f"  Name: {self.name}\n"
              f"  Crew: {self.crew_size}\n"
              f"  Power: {self.power_level}%\n"
              f"  Oxygen: {self.oxygen_level}%\n"
              f"  Last Maintenance: {self.last_maintenance}\n"
              f"  Operational: {self.is_operational}"
              )


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 60)
    config = DataConfig()
    generator = SpaceStationGenerator(config)

    datos_crudos = generator.generate_station_data(5)

    for i, datos in enumerate(datos_crudos, 1):
        print(f"Datos a introducir: {datos}\n")
        try:
            # Desempaquetamos el diccionario directamente
            ship = space_station(**datos)
            print(
                f"✅ Estación {i} ({ship.station_id}) validada correctamente:"
            )
            ship.show()
        except Exception as e:
            print(f"❌ Error de validación en la estación {i}: {e}")
        print()


if __name__ == "__main__":
    main()
