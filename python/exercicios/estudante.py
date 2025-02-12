def registrar_alunos():
    alunos = []  

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break

        notas = []
        while True:
            try:
                nota = float(input(f"Digite uma nota para {nome} (ou -1 para finalizar): "))
                if nota == -1:
                    break
                elif 0 <= nota <= 10:
                    notas.append(nota)
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        if notas:
            media = sum(notas) / len(notas)
            alunos.append({"nome": nome, "notas": notas, "media": media})

    return alunos

def exibir_resultados(alunos):
    if not alunos:
        print("Nenhum aluno registrado.")
        return

    maior_media = max(alunos, key=lambda aluno: aluno['media'])

    print("\nResultados:")
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']}, Notas: {aluno['notas']}, Média: {aluno['media']:.2f}")

    print(f"\nAluno com a maior média: {maior_media['nome']} ({maior_media['media']:.2f})")


if __name__ == "__main__":
    alunos = registrar_alunos()
    exibir_resultados(alunos)
