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
    vertices = [linhas.pop(0) for _ in range(num_v)]

    # Lê as faces
    faces = [linhas.pop(0) for _ in range(num_f)]

    # Inicializa as tabelas
    verticesTable = ""
    facesTable = ""

    # Mapeia os vértices para suas respectivas faces
    for x in range(len(vertices)):
        facesVT = []
        for j in range(len(faces)):
            face_data = faces[j].split()
            face_type = int(face_data[0])  # Número de vértices na face
            vertex_indices = face_data[1:]  # Índices dos vértices

            # Verifica se o vértice faz parte da face
            if str(x) in vertex_indices:
                facesVT.append(f"F{j}")

        # Adiciona os dados do vértice à tabela
        if facesVT:
            verticesTable += f"('V{x}:', [{vertices[x]}], {facesVT})\n"
        else:
            verticesTable += f"('V{x}:', [{vertices[x]}])\n"

    # Monta a tabela de faces com a verificação de formato
    for i, face in enumerate(faces):
        face_data = face.split()
        num_vertices = int(face_data[0])  # Primeiro número indica quantos vértices a face possui
        vertex_indices = face_data[1:]  # Índices dos vértices

        # Verifica se a face é triangular ou quadrilátera
        if num_vertices not in {3, 4}:
            print(f"⚠️ Erro: A face F{i} contém {num_vertices} vértices. Apenas triângulos e quadriláteros são permitidos.")
            return

        # Converte índices para formato "Vx"
        faceVT = ", ".join(f"V{v}" for v in vertex_indices)
        facesTable += f"('F{i}', [{faceVT}])\n"

    # Exibe as tabelas
    print('TABELA DE VÉRTICES')
    print(verticesTable)

    print('TABELA DE FACES')
    print(facesTable)


if __name__ == '__main__':
    main()
