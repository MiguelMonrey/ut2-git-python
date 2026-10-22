# Guía de Contribución: Ejercicios UT2 (Python)

Este repositorio contiene los 8 ejercicios de estructuras de control en Python correspondientes a la práctica de Git de la UT2.

## Flujo de trabajo y ramas
- La rama `main` contiene el código estable. **Nunca se trabaja directamente sobre `main`.**
- Para modificar un ejercicio existente o añadir uno nuevo, crea siempre una rama descriptiva a partir de `main`:
  `git switch -c mejoras`

## Mensajes de Commit
Es obligatorio seguir el formato `tipo: descripción`. Tipos utilizados en este proyecto:
- `feat`: Nuevos ejercicios o funcionalidades (ej. *feat: ejercicio 8 contraseña*).
- `fix`: Corrección de errores.
- `docs`: Cambios en la documentación (`README.md` o este mismo archivo).
- `style`: Mejoras visuales (alineación, sangrías, textos en los `print`).

## Pasos para proponer un cambio (Pull Request)
1. Asegúrate de estar al día: `git switch main` y `git pull`.
2. Crea tu rama temporal: `git switch -c mejoras`.
3. Haz tus cambios, prepáralos (`git add`) y confírmalos (`git commit`).
4. Sube la rama a GitHub: `git push -u origin mejoras`.
5. Ve a GitHub y abre una **Pull Request** hacia `main`. 
6. Espera la revisión de un compañero antes de fusionar.

## Cómo ejecutar el proyecto en local (Windows)
1. Clona el repositorio en tu equipo mediante SSH:
   `git clone git@github.com:MiguelMonrey/ut2-git-python.git`
2. Entra en la carpeta del repositorio:
   `cd ut2-git-python`
3. Ejecuta cualquiera de los archivos llamando a `python` desde la terminal:
   `python ej01_par_impar.py`