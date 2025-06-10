1. Instala dependencias de Python:

```bash
sudo apt update
sudo apt install -y python3-pip python3-dev python3-venv python3-wheel
```

2. Clona el repositorio y crea el entorno virtual:

```bash
mkdir -p ~/project
cd ~/project
git clone <URL_REPOSITORIO>
cd <nombre_repositorio>
python3 -m venv env
source env/bin/activate
```


3. Instala las dependencias del proyecto:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```