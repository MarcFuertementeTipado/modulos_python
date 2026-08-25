from pydantic import BaseModel, Field, model_validator  # type: ignore
from datetime import datetime
from enum import Enum
from modulo_09.ex2.data_generator import AlienContactGenerator, DataConfig  # type: ignore


class contact_type(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: contact_type
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_attributes(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "ID must start with 'AC' name"
            )
        if self.contact_type == "physical" and self.is_verified == False:
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self

    def show(self):
        print(f"--- 👽 Reporte de Contacto: {self.contact_id} ---")
        # model_dump() convierte el modelo en un diccionario clave: valor
        for atributo, valor in self.model_dump().items():
            print(f"  {atributo}: {valor}")
        print("-" * 40)


def main() -> None:
    # Generate alien contact data
    config = DataConfig()
    contact_gen = AlienContactGenerator(config)
    contacts = contact_gen.generate_contact_data(6)
        
    print(f"\n👽 Generated {len(contacts)} alien contacts:")
    for contact in contacts:
        alien = AlienContact(**contact)
        verified = "✅ Verified" if contact["is_verified"] else "❓ Unverified"
        print(f"  {contact['contact_id']}: {contact['contact_type']} at {contact['location']} - {verified}")
        alien.show()


if __name__ == "__main__":
    main()
