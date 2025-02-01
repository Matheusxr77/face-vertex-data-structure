# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np

# Função principal
def main():
    # Solicita ao usuário o nome do arquivo OFF (sem extensão)
    filename = input('Arquivo OFF: ')
    
    # Lê o conteúdo do arquivo
    with open(filename + '.off', 'r') as f:
        linhas = f.read().split('\n')

    # Remove a primeira linha, que contém "OFF"
    del linhas[0]

    # Obtém o número de vértices e faces
    num_v, num_f, _ = map(int, linhas[0].split())
    del linhas[0]

    # Exibe o número de vértices e faces
    print(f"Número de Vértices: {num_v}")
    print(f"Número de Faces: {num_f}\n")

    # Lê os vértices
    vertices = [list(map(float, linhas.pop(0).split())) for _ in range(num_v)]
    vertices = np.array(vertices)

    # Lê as faces
    faces = [list(map(int, linhas.pop(0).split()[1:])) for _ in range(num_f)]

    # Inicializa as tabelas
    verticesTable = ""
    facesTable = ""

    # Mapeia os vértices para suas respectivas faces
    for x in range(len(vertices)):
        facesVT = []
        for j in range(len(faces)):
            if x in faces[j]:
                facesVT.append(f"F{j}")

        # Adiciona os dados do vértice à tabela
        if facesVT:
            verticesTable += f"('V{x}:', {vertices[x].tolist()}, {facesVT})\n"
        else:
            verticesTable += f"('V{x}:', {vertices[x].tolist()})\n"

    # Monta a tabela de faces com a verificação de formato
    for i, face in enumerate(faces):
        num_vertices = len(face)

        # Verifica se a face é triangular ou quadrilátera
        if num_vertices not in {3, 4}:
            print(f"⚠️ Erro: A face F{i} contém {num_vertices} vértices. Apenas triângulos e quadriláteros são permitidos.")
            return

        # Converte índices para formato "Vx"
        faceVT = ", ".join(f"V{v}" for v in face)
        facesTable += f"('F{i}', [{faceVT}])\n"

    # Exibe as tabelas
    print('TABELA DE VÉRTICES')
    print(verticesTable)

    print('TABELA DE FACES')
    print(facesTable)

    # Plotando a malha
    fig, ax = plt.subplots()
    for face in faces:
        polygon = vertices[face]
        polygon = np.vstack([polygon, polygon[0]])  # Fechando a forma
        ax.plot(polygon[:, 0], polygon[:, 1], 'k-')

    # Plotando os vértices
    ax.scatter(vertices[:, 0], vertices[:, 1], color='red')
    ax.set_title("Visualização da Malha")
    plt.show()

# Executa a função principal
if __name__ == '__main__':
    main()