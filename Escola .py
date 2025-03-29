turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = int(input("Digite a quantidade total de alunos: "))

media_alunos_por_turma = total_alunos / turmas

if media_alunos_por_turma > 40:
    print(f"A média de alunos por turma é {media_alunos_por_turma:.2f}, o que indica que algumas turmas podem ter mais de 40 alunos.")
else:
    print(f"A média de alunos por turma é {media_alunos_por_turma:.2f}.")

if total_alunos / turmas > 40:
    print("Aviso: Alguma turma tem mais de 40 alunos!")
