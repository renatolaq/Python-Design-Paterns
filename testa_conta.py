from datetime import datetime

class Cliente:

    def __init__(self):
        pass


class Transacao:
    def gera_transacao(self, dt, operacao, valor):
        a = 0
        return {'data': dt, 'operacao': operacao, 'valor':valor}



class ContaBanco:
    # Aqui insere atributos globais

    quantidade = 0
    def data_atual(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self):
        self.contas = []
        self.extrato = []
        self.hora_atual = []
        ContaBanco.quantidade# utilizado em treinamento




    def conta_saldo(self):
        print("===================================================")
        print("BANCO ACME - CONSULTA SALDOS    "+self.data_atual())
        print("=================================================== ")
        print("")
        selecao = input("INFORME SUA CONTA ")
        for info  in self.contas:
            agencia = info['agencia']
            conta = info['conta']
            nome = info['nome']
            saldo = info['saldo']
            limite = info['limite']
            saldo_total = info['saldo_total']
            if selecao == conta:
                print("")
                print("")
                print("===================================================")
                print("BANCO ACME - CONSULTA SALDOS    "+c.data_atual())
                print("=================================================== ")
                print("AGENCIA "+agencia+"/"+conta)
                print(nome.upper())
                print("=================================================== ")
                print("SALDO DISPONIVEL R$ " +  "{:.2f} ".format(saldo) )
                print("LIMITE CREDITO   R$ " + "{:.2f} ".format(limite))
                print("SALDO TOTAL      R$ " + "{:.2f} ".format(saldo_total))

                print("=================================================== ")
                input("PRESSIONE < ENTER > PARA CONTINUAR")
                print("")
                print("")

    def conta_extrato(self):
        print("===================================================")
        print(" BANCO ACME - EXTRATO CONTA  " + self.data_atual())
        print("=================================================== ")
        print("")
        selecao = input("INFORME SUA CONTA ")
        chave = 0
        for info in self.contas:
            agencia = info['agencia']
            conta = info['conta']
            nome = info['nome']
            saldo = info['saldo']
            limite = info['limite']
            transacao = info['transacao']
            if selecao == conta:
                print("")
                print("")
                print("===================================================")
                print("BANCO ACME - DEPOSITO EM CONTA - " + self.data_atual())
                print("=================================================== ")
                print("AGENCIA " + agencia + "/" + conta)
                print(nome.upper())
                print("=================================================== ")
                print("            EXTRATO DE MOVIMENTAÇÕES")
                print("=================================================== ")
                if len(transacao) == 0:
                    print("  *** NÃO EXISTE MOVIMENTAÇÕES NA CONTA ***")
                else:
                    for registro in transacao:
                        print(registro['data'] + " " + registro['operacao'] + " " + "{:.2f} ".format(registro['valor']))
                print("")
                print("=================================================== ")
                print("SALDO DISPONIVEL R$ " + "{:.2f} ".format(saldo))
                print("LIMITE CREDITO   R$ " + "{:.2f} ".format(limite))
                print("SALDO TOTAL      R$ " + "{:.2f} ".format(saldo + limite))

                print("=================================================== ")
                print("")
                input("PRESSIONE < ENTER > PARA CONTINUAR")
                print("")
                print("")
                return
            chave += 1
        input("CONTA NAO IDENTIFICADA < ENTER > PARA CONTINUAR")

    def conta_deposito(self):
        print("===================================================")
        print(" BANCO ACME - DEPOSITO CONTA  "+self.data_atual())
        print("=================================================== ")
        print("")
        selecao = input("INFORME SUA CONTA ")
        chave = 0
        for info in self.contas:
            agencia = info['agencia']
            conta = info['conta']
            nome = info['nome']
            saldo = info['saldo']
            limite = info['limite']
            if selecao == conta:
                print("")
                print("")
                print("===================================================")
                print("BANCO ACME - DEPOSITO EM CONTA - "+self.data_atual())
                print("=================================================== ")
                print("AGENCIA " + agencia + "/" + conta)
                print(nome.upper())
                print("=================================================== ")
                print("SALDO DISPONIVEL R$ " + "{:.2f} ".format(saldo))
                print("=================================================== ")
                deposito = input("INFORME VALOR DEPOSITO ")
                valor_deposito = float(deposito)
                saldo_atualizado = saldo + float(deposito)
                print("=================================================== ")
                print("SALDO ANTERIOR R$ " + "{:.2f} ".format(saldo))
                print("VALOR DEPOSITO R$ " + "{:.2f} ".format(valor_deposito))
                print("SALDO ATUAL    R$ " + "{:.2f} ".format(saldo_atualizado))
                print("=================================================== ")
                # atualiza saldo da conta
                self.contas[chave]['saldo'] = saldo_atualizado
                self.contas[chave]['saldo_total'] = saldo_atualizado + limite
                # Gravar a Transacao
                registro = Transacao.gera_transacao(self ,self.data_atual(),"(+) DEPOSITO ", valor_deposito)
                self.contas[chave]['transacao'].append(registro)
                a = 0

                input("PRESSIONE < ENTER > PARA CONTINUAR")
                print("")
                print("")
                return
            chave+=1
        input("CONTA NAO IDENTIFICADA < ENTER > PARA CONTINUAR")

    def conta_saque(self):
        print("===================================================")
        print(" BANCO ACME - SAQUE CONTA -    " + self.data_atual())
        print("=================================================== ")
        print("")
        selecao = input("INFORME SUA CONTA ")
        chave = 0
        for info in self.contas:
            agencia = info['agencia']
            conta = info['conta']
            nome = info['nome']
            saldo = info['saldo']
            limite = info['limite']
            if selecao == conta:
                print("")
                print("")
                print("===================================================")
                print("BANCO ACME - SAQUE CONTA -   " + self.data_atual())
                print("=================================================== ")
                print("AGENCIA " + agencia + "/" + conta)
                print(nome.upper())
                print("=================================================== ")
                print("SALDO DISPONIVEL R$ " + "{:.2f} ".format(saldo))
                print("=================================================== ")
                saque = input("INFORME VALOR SAQUE ")
                # VALIDAR O VALOR DO SAQUE
                valor_saque = float(saque)
                saldo_mais_limite = saldo + limite
                autoriza = self.autoriza_saque(valor_saque,saldo_mais_limite)
                if autoriza:
                    saldo_atualizado = saldo - float(valor_saque)
                    print("=================================================== ")
                    print("SALDO ANTERIOR R$ " + "{:.2f} ".format(saldo))
                    print("VALOR SAQUE    R$ " + "{:.2f} ".format(valor_saque))
                    print("SALDO ATUAL    R$ " + "{:.2f} ".format(saldo_atualizado))
                    print("=================================================== ")
                    # atualiza saldo da conta
                    sa = self.ajusta_saldo_saque(valor_saque, saldo, limite)
                    self.contas[chave]['saldo'] = sa['saldo']
                    self.contas[chave]['limite'] = sa['limite']
                    self.contas[chave]['saldo_total'] = sa['saldo'] + sa['limite']
                    # Gravar a Transacao
                    registro = Transacao.gera_transacao(self, self.data_atual(), "(-) SAQUE    ", valor_saque)
                    self.contas[chave]['transacao'].append(registro)
                    a = 0

                    input("PRESSIONE < ENTER > PARA CONTINUAR")
                    print("")
                    print("")
                    return
                else:
                    input("SAQUE NÃO AUTORIZADO < ENTER > PARA CONTINUAR")
                    return
            chave += 1
        input("CONTA NAO IDENTIFICADA < ENTER > PARA CONTINUAR")

    def autoriza_saque(self, valor_saque, saldo_mais_limite):
        if valor_saque > saldo_mais_limite:
            return False
        else:
            return True

    # make debit saldo and after make debit on limit and returns values updated {'saldo' 0.00,  'limite': 0,00}
    def ajusta_saldo_saque(self, valor_saque, saldo, limite):
        # ajust saldo
        if saldo >= valor_saque:
            saldo = saldo - valor_saque
        else:
            diferenca = valor_saque - (saldo + limite)
            saldo = diferenca * -1
            limite = limite - diferenca
        return {'saldo':saldo, 'limite':limite}


    def gerar_contas(self):
        conta1 = {'agencia': '0001', 'conta':'00001-1', 'nome':'Renato Pereira', 'cpf': '11707899860', 'saldo': 1000.0, 'limite':0.0, 'saldo_total': 1000.0, 'data_abertura':'02/10/2019 10:41:10', 'transacao':[], 'cadastro':[{'cpf':'11707899860', 'rg':'21967629', 'telefone':'1146395855'}]}
        conta2 = {'agencia': '0001', 'conta':'00002-2', 'nome': 'Aline Blasco',  'cpf': '43061665897','saldo': 1000.0,  'limite':0.0, 'saldo_total': 1000.0, 'data_abertura':'02/10/2019 10:41:10', 'transacao':[], 'cadastro':[{'cpf':'43061668597', 'rg':'21963222', 'telefone':'1146395855'}]}
        self.contas.append(conta1)
        self.contas.append(conta2)
        return self.contas

    def conta_lista(self):
        print("===================================================")
        print("BANCO ACME - CONTAS ATIVAS -  "+self.data_atual())
        print("=================================================== ")
        print("")
        for conta in self.contas:
            print(conta['agencia'] +"/"+conta['conta']+" CPF "+conta['cpf']+"  "+conta['nome'])

        print("")
        input("PRESSIONE < ENTER > PARA CONTINUAR")


    def conta_abertura(self):
        print("")
        print("")
        print("===================================================")
        print("BANCO ACME - ABERTURA DE CONTAS "+self.data_atual())
        print("=================================================== ")
        print("")
        input("PRESSIONE < ENTER > PARA CONTINUAR")


if __name__ == '__main__':


    c = ContaBanco()
    con = c.gerar_contas()
    acao = True
    while acao == True:
        print("===================================================")
        print("BANCO ACME - ABC               "+c.data_atual())
        print("=================================================== ")
        print("                 MENU CLIENTE")
        print("=================================================== ")
        print("         0 - VERIFICAÇÃO SALDO                          ")
        print("         1 - DEPOSITOS                                 ")
        print("         2 - SAQUE                                     ")
        print("         3 - TRANSFERENCIAS                            ")
        print("         4 - EXTRATO CONTA")
        print("=================================================== ")
        print("               MENU ADMINISTRATIVO")
        print("=================================================== ")
        print("         5 - LISTAGEM DE CONTAS ATIVAS                 ")
        print("         6 - ABERTURA DE CONTAS")
        print("         7 - LIBERA LIMITE CREDITO")
        print("         8 - DADOS CADASTRAIS CLIENTE")
        print("         99 - SAIR DO SISTEMA                           ")
        print("===================================================")
        escolha = input("OPÇÃO DESEJADA ")
        print("")
        if escolha == '':
            continue

        elif int(escolha) == 0:
            c.conta_saldo()
        elif int(escolha) == 1:
            c.conta_deposito()
        elif int(escolha) == 2:
            c.conta_saque()
        elif int(escolha) == 4:
            c.conta_extrato()
        elif int(escolha) == 5:
            c.conta_lista()
        elif int(escolha) == 6:
            c.conta_abertura()
        elif int(escolha) == 99:
            acao = False




