# construct_mspi_software
Este repositorio contiene una serie de script para dockerizar el proyecto [mspi-software](https://github.com/jjvargass/mspi-software)


## Especificaciones Técnica

### Tecnologías Implementadas y Versiones

- [python 2.7](https://www.python.org/download/releases/2.7/)

### Ejecución del Proyecto

```bash
# Descarga los repositorios necesarios
python2.7 get_repos.py

# Eliminar repo antiguo
rm -r -f extra-addons/odoo-idu-addons-publico/src/plan_mejoramiento_idu/

# correr odoo
docker-compose up
```
### Variables de Entorno
```shell
...
```

## Licencia

This file is part of construct_mspi_software.

construct_mspi_software is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
