import os

try:
    os.mkdir('A',0o700)
    os.mkdir('A/B',0o355)
    os.mkdir('A/B/secret',0o555)
    os.chmod('A', 0o600)
except :
    print("Impossible de créer l'arborescence; un fichier de nom A existe déjà dans ce répertoire.")
