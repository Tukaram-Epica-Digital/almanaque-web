# almanaque-web

Version estatica del visor del almanaque: un unico `index.html` de canvas que
carga las 277 paginas en `.webp`, mas el envoltorio del simulador
(`simulador/index.html`).

Es la via rapida para ensenar el almanaque sin levantar Next.js.

Copiado de `C:\almanaque\web`.

## Servir en local

```bash
python servir.py 8080
```

`servir.py` es un servidor **multi-hilo**: `python -m http.server` atiende una
peticion a la vez y el visor pide muchas imagenes en paralelo, lo que corta
cargas y deja las texturas negras. Este sirve cada peticion en su propio hilo.

`index_v2_backup.html` es el backup de la version anterior del visor.
