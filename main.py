print("=== Sistema de Triagem de PDVs ===")

pdvs_totais = int(input("Quantos PDVs a filial possui? "))

while pdvs_totais < 0:
    print("Quantidade Inválida! Tente Novamente.")
    pdvs_totais = int(input("Quantos PDVs a filial possui? "))

pdvs_com_defeito = int(input("Quantos PDVs estão com problema? "))

while pdvs_com_defeito > pdvs_totais or pdvs_com_defeito < 0:
    print("Quantidade Inválida! Tente Novamente.")
    pdvs_com_defeito = int(input("Quantos PDVs estão com problema? "))


if pdvs_com_defeito >= 3:
    classificacao = "Impacto Alto!"
elif pdvs_com_defeito >= 1:
    classificacao = "Impacto Baixo!"
else:
    classificacao = "Nenhum Impacto!"


print(f"Total de PDVs: {pdvs_totais}")
print(f"PDVs afetados: {pdvs_com_defeito}")
print(f"Classificação: {classificacao}")
