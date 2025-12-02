# Utilise une image Python légère comme base
FROM python:3.9-slim

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Copie le fichier de dépendances et installe les librairies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code source de l'application
COPY hello_world.py .

# Expose le port 4049 (celui défini dans votre code Flask)
EXPOSE 4049

# Commande pour démarrer l'application
CMD ["python", "hello_world.py"]