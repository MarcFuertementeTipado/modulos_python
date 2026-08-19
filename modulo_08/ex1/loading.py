import sys
import importlib
import importlib.metadata
from typing import Dict, List, Tuple, Any

# Añadimos tipos estrictos para Mypy
REQUIRED_PACKAGES: Dict[str, str] = {
    'pandas': 'Data manipulation ready',
    'numpy': 'Numerical computation ready',
    'matplotlib': 'Visualization ready'
}


def check_dependencies() -> Tuple[Dict[str, Tuple[str, str]], List[str]]:
    """Comprueba las dependencias requeridas instaladas y faltantes."""
    installed: Dict[str, Tuple[str, str]] = {}
    missing: List[str] = []

    for pkg, desc in REQUIRED_PACKAGES.items():
        try:
            version = importlib.metadata.version(pkg)
            installed[pkg] = (version, desc)
        except importlib.metadata.PackageNotFoundError:
            missing.append(pkg)

    return installed, missing


def print_instructions(missing_pkgs: List[str]) -> None:
    """Muestra las instrucciones de instalación y sale del programa."""
    missing_str = ', '.join(missing_pkgs)
    print(f"Error: Missing dependencies: {missing_str}\n")
    print("Please install the required packages to run this program.")
    print("Using pip:")
    print("  $> pip install -r requirements.txt")
    print("Using Poetry:")
    print("  $> poetry install")
    print("  $> poetry run python loading.py")
    sys.exit(1)


def main() -> None:
    """Función principal que ejecuta el análisis de datos de Matrix."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    installed, missing = check_dependencies()

    if missing:
        print_instructions(missing)

    for pkg, (version, desc) in installed.items():
        print(f"[OK] {pkg} ({version}) - {desc}")

    # EL "MECANISMO SECRETO": Importación dinámica asignada a Any
    # Evita que Flake8 y Mypy fallen si el linter corre en un entorno limpio
    np: Any = importlib.import_module('numpy')
    pd: Any = importlib.import_module('pandas')
    plt: Any = importlib.import_module('matplotlib.pyplot')

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    # Simulación de datos Matrix
    x = np.linspace(0, 10, 1000)
    y = np.sin(x) + np.random.normal(0, 0.1, 1000)

    # almaceno los datos creados en un DataFrame
    df = pd.DataFrame({
        'Time': x,
        'Signal': y
    })

    print("Generating visualization...")

    # creo el lienzo en blanco donde poner los datos
    plt.figure(figsize=(10, 6))

    # Dividimos los argumentos para respetar los 79 caracteres de Flake8
    plt.plot(
        df['Time'],
        df['Signal'],
        color='#00FF41',
        linewidth=1.5,
        label='Matrix Signal'
    )

    plt.style.use('dark_background')
    plt.title('Matrix Data Analysis - Signal Fluctuation')
    plt.xlabel('Time Sequence')
    plt.ylabel('Signal Output')
    plt.grid(True, color='#003B00', linestyle='--', alpha=0.7)
    plt.legend()

    plt.savefig('matrix_analysis.png')
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
