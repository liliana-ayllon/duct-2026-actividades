# Actividad 4 – Analizador de frecuencias con pruebas automatizadas

Diplomatura en Competencias Técnicas para Profesionales de Idiomas: genIA, Data y Programación – Universidad Nacional de Córdoba (2026).

## Archivos del proyecto

- `analizador.py`: contiene la función `contar_frecuencias()`.
- `test_analizador.py`: contiene las pruebas automatizadas.
- `Informe_Actividad_4_Liliana_Ayllon_Hernandez.docx`: informe de la actividad.

## Pruebas automatizadas

Se implementaron cuatro pruebas para verificar:

1. Conteo básico de frecuencias.
2. Procesamiento de texto vacío.
3. Tratamiento de mayúsculas y minúsculas.
4. Manejo de espacios adicionales.

### Cómo ejecutar las pruebas

Desde la carpeta `Actividad_4`, ejecutar:

```bash
python -m pytest -v test_analizador.py
```

### Resultado de la ejecución

**4 passed in 0.12s**

Las cuatro pruebas se ejecutaron correctamente utilizando pytest.
