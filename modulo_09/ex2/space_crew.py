from pydantic import BaseModel, Field, model_validator  # type: ignore
from enum import Enum
from datetime import datetime
from data_generator import DataConfig, CrewMissionGenerator  # type: ignore


class crew_ranks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: crew_ranks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def show(self):
        print(f"--- 🧑‍🚀 Tripulante: {self.name} ---")
        print(f"  - ID: {self.member_id}")
        print(f"  - Rango: {self.rank}")
        print(f"  - Edad: {self.age} años")
        print(f"  - Especialización: {self.specialization}")
        print(f"  - Experiencia: {self.years_experience} años")
        print(f"  - Estado: {'🟢 Activo' if self.is_active else '🔴 Inactivo'}")
        print("-" * 35)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_missionrules(self):
        __is_commander: bool = False
        __is_experienced: int = 0
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'"
            )

        for member in self.crew:
            if member.rank == "commander":
                __is_commander = True
            if member.is_active is not True:
                raise ValueError(
                    "All members must be active!"
                )
            if member.years_experience > 5:
                __is_experienced += 1
        if __is_commander is not True:
            raise ValueError(
                "It is necessary at least 1 commander"
            )
        percent_experienced_crew = (100 * __is_experienced) / len(self.crew)
        if self.duration_days > 365 and percent_experienced_crew < 50:
            raise ValueError(
                "Long missions (> 365 days) \
                 need 50percent experienced crew (5+ years)"
            )
        return self

    def show(self):
        print(f"🚀 === MISIÓN ESPACIAL: {self.mission_name} ===")
        print(f"  - ID de Misión: {self.mission_id}")
        print(f"  - Destino: {self.destination}")
        print(f"  - Fecha de Lanzamiento: {self.launch_date}")
        print(f"  - Duración: {self.duration_days} días")
        print(f"  - Estado: {self.mission_status.upper()}")
        print(f"  - Presupuesto: ${self.budget_millions} millones")
        print(f"  - Tripulación ({len(self.crew)} miembros):")
        print("  " + "-" * 40)

        # Recorremos la lista de tripulantes y llamamos a su propio show()
        for miembro in self.crew:
            print("    ", end="")
            miembro.show()

        print("=" * 45)


def main() -> None:
    config = DataConfig()
    # Generate mission data
    mission_gen = CrewMissionGenerator(config)
    missions = mission_gen.generate_mission_data(1)

    # Datos erroneos para testear errores (ERROR "FALTA AL MENOS 1 COMANDANTE")
    mission_error = {'mission_id': 'MA2024_TITAN',
                     'mission_name': 'Solar Observatory Research Mission',
                     'destination': 'Solar Observatory',
                     'launch_date': '2024-03-30T00:00:00',
                     'duration_days': 451,
                     'crew': [{'member_id': 'CM001',
                               'name': 'Sarah Williams',
                               'rank': 'captain', 'age': 43,
                               'specialization': 'Mission Command',
                               'years_experience': 19, 'is_active': True},
                              {'member_id': 'CM002',
                               'name': 'James Hernandez',
                               'rank': 'captain',
                               'age': 43,
                               'specialization': 'Pilot',
                               'years_experience': 30,
                               'is_active': True},
                              {'member_id': 'CM003',
                               'name': 'Anna Jones',
                               'rank': 'cadet',
                               'age': 35,
                               'specialization': 'Communications',
                               'years_experience': 15,
                               'is_active': True}],
                     'mission_status': 'planned',
                     'budget_millions': 2208.1}
    missions.append(mission_error)

    print(f"\n🚀 Generated {len(missions)} space missions:")
    for mission in missions:
        try:
            print(mission)
            space_m = SpaceMission(**mission)
            space_m.show()
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    main()
