# Pasos para crear un paquete

- [Tutorial oficial de python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

- [Keywords de setuptools](https://setuptools.pypa.io/en/latest/references/keywords.html)

- [Gestión de dependencias](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#declaring-dependencies)

- [Gestión de archivos de datos](https://packaging.python.org/en/latest/guides/using-manifest-in/)

- [Configurar setuptools usando setup.cfg](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)

### Crear el archivo pyproject.toml (si usas setuptools no es necesario crearlo)

pyproject.toml le dice a las herramientas de build (como pip y build) que se necesita para construir el paquete.

### Configuración de la metadata del paquete

Existen 2 archivos [setup.cfg](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html) (estático) y setup.py (dinámico). Se puede colocar toda la metadata en el archivo setup.py a pesar de que sea metadata estática debido a que antes era la única manera de hacerlo, pero ahora se recomienda separar la metadata estática de la dinámica.

### Configuración del manejo de archivos de datos

Al agregar el keyword `includ_package_data` dentro del archivo setup.py, se va agregar al paquete todos los archivos de datos. Si deseamos agregar ciertos archivos se debe crear el archivo `MANIFEST.in`.

### Construir el paquete

Instalar el paquete de `build` con el comando `python -m pip install --upgrade build`. Una vez terminemos de configurar el archivo setup.py se ejecuta el siguiente comando `python -m build` para construir el paquete y el wheel que se subirá al repositorio.

### Subir el proyecto a pypi

Instalar el paquete de `twine` con el comando `pip install twine`. Ejecutamos el siguiente comando `twine check dist/*` para verificar que los archivos estén bien configurados. Finalmente ejecutamos `twine upload dist/*` para subir el paquete a pypi. Al subir este proyecto te pedirá tu usuario y contraseña, para evitar colocarlo a cada rato crea el archivo `.pypirc` con la siguiente configuración:

```
[pypi]
username = __token__
password = <PyPI token>
```

### Actualizar algún cambio en el proyecto

Para actualizar un cambio en el paquete, luego de haber realizado los cambios se debe actualizar la versión del paquete. Para ello se utilizar la herramienta de `bumpversion`. Primero la instalamos `pip install bumpversion` y luego ejecutamos `bumpversion --current-version 1.0.0 minor setup.py reader/__init__.py`.

Finalmente, se debe eliminar los archivos de la carpeta dist y ejecutar el comando `python -m build` nuevamente.
