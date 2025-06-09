# Crear entorno virtual

```bash
python3 -m venv venv
```

# Activar virtual env

```bash
source venv/bin/activate
```

# Instalar depencias

```bash
pip install -r requirements.txt
```

# Ejecutar
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
