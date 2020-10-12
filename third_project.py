print("Estes resultados abaixo são relativos à funções apenas")


def Fator_Parcelamento(taxa_de_juros, numero_de_parcelas):
    FP = (((1 + taxa_de_juros)**numero_de_parcelas) - 1)/(((1 + taxa_de_juros)**numero_de_parcelas) * taxa_de_juros)
    return FP


def Total_a_pagar(valor_a_vista, x, y, func):
    Valor_parcela = valor_a_vista/func(x, y)
    total_pagar = Valor_parcela * y
    print(Valor_parcela)
    return total_pagar


print(Fator_Parcelamento(2/100, 30))
teste = Total_a_pagar(2, 2/100, 30, Fator_Parcelamento)
print(teste)
print("#" * 30)

print("Estes resultados abaixo são relativos à uma classe")


class Pagamento:
    def __init__(self, taxa_de_juros, numero_de_parcelas, valor_a_vista):
        self.taxa_de_juros = taxa_de_juros
        self.numero_de_parcelas = numero_de_parcelas
        self.valor_a_vista = valor_a_vista

    def fator_de_parcelamento(self):
        fp = (((1 + self.taxa_de_juros) ** self.numero_de_parcelas) - 1) / (
                    ((1 + self.taxa_de_juros) ** self.numero_de_parcelas) * self.taxa_de_juros)
        return fp

    def valor_parcela(self):
        vp = self.valor_a_vista/self.fator_de_parcelamento()
        return vp

    def valor_total(self):
        vt = self.valor_parcela() * self.numero_de_parcelas
        return vt


Lucas = Pagamento(2/100, 30, 2)
print(Lucas.fator_de_parcelamento())
print(Lucas.valor_parcela())
print(Lucas.valor_total())





