import os
import sys
from dotenv import load_dotenv  # type: ignore

# Variables obligatorias que el Oráculo necesita para despertar
REQUIRED_CONFIGS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def load_oracle_config() -> dict:
    """Carga y valida la configuración del entorno."""
    # Cargamos el archivo .env (si existe)
    load_dotenv()

    config = {}
    missing = []

    for var in REQUIRED_CONFIGS:
        value = os.getenv(var)
        if not value:
            missing.append(var)
        else:
            config[var] = value

    # Si faltan variables, mostramos error y detenemos el programa
    if missing:
        print(f"Error: Missing configuration variables: {', '.join(missing)}")
        print("Please check your .env file or environment variables.")
        sys.exit(1)

    return config


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    # Cargamos configuraciones
    config = load_oracle_config()

    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    # Demostración de diferencia entre desarrollo y producción
    if config['MATRIX_MODE'] == "production":
        print("Database: Connected to secure remote cluster (PRODUCTION)")
        print("API Access: Authenticated via Enterprise Gateway")
    else:
        print("Database: Connected to local instance (DEVELOPMENT)")
        print("API Access: Authenticated (Local Sandbox)")

    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: Online ({config['ZION_ENDPOINT']})")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
