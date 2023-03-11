
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros

def regra_de_tres (n1):

    x = (100 * n1)/total
    print(f'O porcentual do Estado é "{x}%')

regra_de_tres(SP);
regra_de_tres(RJ);
regra_de_tres(MG);
regra_de_tres(ES);
regra_de_tres(Outros);
