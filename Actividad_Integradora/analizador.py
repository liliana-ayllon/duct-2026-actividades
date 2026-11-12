from pathlib import Path

import matplotlib.pyplot as plt


def contar_frecuencias(texto):
    frecuencias = {}
    for palabra in texto.lower().split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def guardar_grafico(frecuencias, titulo, salida):
    top_10 = sorted(frecuencias.items(), key=lambda par: par[1], reverse=True)[:10]
    palabras = [palabra for palabra, cantidad in top_10]
    valores = [cantidad for palabra, cantidad in top_10]

    plt.figure(figsize=(9, 5))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(titulo)
    plt.xlabel("Cantidad de apariciones")
    plt.tight_layout()
    plt.savefig(salida, dpi=150)
    plt.close()
    print("Gráfico guardado en:", salida)


def main():
    ruta = Path(__file__).with_name("texto_integradora.txt")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print("No se encontró texto_integradora.txt.")
        return

    frecuencias = contar_frecuencias(texto)
    print("Palabras totales:", sum(frecuencias.values()))
    print("Palabras distintas:", len(frecuencias))

    guardar_grafico(
        frecuencias,
        "Las 10 palabras más frecuentes",
        ruta.with_name("grafico_frecuencias.png"),
    )

    palabras_vacias = {
        "a", "al", "con", "de", "del", "el", "ella", "en", "es", "la",
        "las", "lo", "los", "no", "o", "para", "por", "que", "se", "sin",
        "su", "sus", "un", "una", "uno", "unas", "unos", "y",
    }
    frecuencias_filtradas = {
        palabra: cantidad
        for palabra, cantidad in frecuencias.items()
        if palabra.strip(".,;:¡!¿?()«»\"'") not in palabras_vacias
    }

    guardar_grafico(
        frecuencias_filtradas,
        "Las 10 palabras más frecuentes sin palabras vacías",
        ruta.with_name("grafico_sin_palabras_vacias.png"),
    )


if __name__ == "__main__":
    main()