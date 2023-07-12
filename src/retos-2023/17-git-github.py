### Reto #17: GIT Y GITHUB
#### Publicación: 24/04/23 | DIFÍCIL

#¿Sabías que puedes leer información de Git y GitHub desde la gran mayoría de lenguajes de programación?
#Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#- Hash
#- Autor
#- Mensaje
#- Fecha y hora
#
#Ejemplo de salida:
#Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
# 
#Se permite utilizar librerías que nos faciliten esta tarea.


#python -m pip install gitpython
import git

def getLastCommits(limit: int = 10):
    return list(git.Repo(".").iter_commits())[:limit]

if __name__ == '__main__':
    print("Reto #17: GIT Y GITHUB")
    for index, commit in enumerate(getLastCommits()):
        print(f"Commit {index} | {commit.hexsha} | {commit.author.name} | {commit.message} | {commit.authored_datetime}".replace("\n", ""))
