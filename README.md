# Qute-Web

Pequeña web estática del grupo "Quantum Technologies Group". Contiene las páginas:

- `home.html`
- `research.html`
- `team.html`
- `news.html`
- `contact.html`

Cómo probar localmente

1. Asegúrate de estar en el directorio del proyecto:

```bash
cd /workspaces/Qute-Web
```

2. Arranca el servidor local con la utilidad incluida `serve.py` (usa Python 3):

```bash
python3 serve.py --bind 127.0.0.1 --port 8000
```

3. Abre tu navegador en `http://127.0.0.1:8000/home.html` o simplemente `http://127.0.0.1:8000/`.

Notas
- El script `serve.py` es un envoltorio mínimo sobre `http.server` que acepta `--bind` y `--port`.
- Si prefieres usar el servidor simple de Python sin el script, puedes ejecutar:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

¿Quieres que además:
- agregue un `index.html` que redirija a `home.html`?
- extraiga la barra de navegación a un fragmento común (`header.html`) y la incluya con JavaScript?
