    def Margem(self):
        margem = self.salario * self.porcentagem
        return margem

    def EmprestimosAtivos(self, valor_emprestimo):
        porcentagem = valor_emprestimo / self.salario
        self.porcentagem -= porcentagem
        return self.porcentagem

    def FazerEmprestimo(self, valor_emprestimo):
        if 0 < valor_emprestimo <= self.Margem():
            porcentagem = valor_emprestimo / self.salario
            self.porcentagem -= porcentagem
            return self.porcentagem
        else:
            print("O valor do seu empréstimo tem que ser maior que 0 e menor ou igual que a sua margem. ")
            print("O valor da sua margem é {}".format(self.Margem()))

    def ValorFinanciado(self, j, n, p):
        q = ((1 - (1 + (j / 100)) ** (-n)) / (j / 100)) * p
        return q


Lucas = Emprestimo(6000, 35 / 100)
