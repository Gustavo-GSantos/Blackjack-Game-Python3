from random import sample, choice


class Baralho:

    def __init__(self) -> None:
        self.baralho = []

    def criar_baralho(self):
        for i in range(1, 14):
            if i <= 10:
                self.baralho.append(f'{i} de Paus')
                self.baralho.append(f'{i} de Ouros')
                self.baralho.append(f'{i} de Copas')
                self.baralho.append(f'{i} de Espadas')
            if i > 10:
                n = None
                if i == 11:
                    n = 'Valete'
                if i == 12:
                    n = 'Dama'
                if i == 13:
                    n = 'Rei'
                self.baralho.append(f'{n} de Paus')
                self.baralho.append(f'{n} de Ouros')
                self.baralho.append(f'{n} de Copas')
                self.baralho.append(f'{n} de Espadas')
        return self.baralho


class Jogo21:
    def __init__(self, baralho):
        self.baralho = baralho
        self.jogadores = []

    def distribuir_cartas(self):
        for i in range(4):
            self.jogadores.append(sample(self.baralho, 1))
            for c in self.jogadores:
                for c2 in c:
                    if c2 in self.baralho:
                        self.baralho.remove(c2)
    
    def verificar_pontos(mao):
        pontos = 0
        for i in mao:
            if i.count('Valete') > 0:
                pontos += 11
            elif i.count('Dama') > 0:
                pontos += 12
            elif i.count('Rei') > 0:
                pontos += 13
            p = [int(s) for s in i.split() if s.isdigit()]
            pontos += sum(p)
            p.clear
        return pontos

    def comp(self):
        jogador = Jogo21.verificar_pontos(self.jogadores[0])
        for i in self.jogadores[1:4]:
            while True:
                pontos = Jogo21.verificar_pontos(i)
                if pontos < jogador:
                    c = choice(self.baralho)
                    i.append(c)
                    self.baralho.remove(c)
                    continue
                else:
                    break


    def jogar(self):
        print('\nBLACKJACK!')
        print(f'Essa é a sua mão: {self.jogadores[0]}')
        print(f'Pontos do jogador = {Jogo21.verificar_pontos(self.jogadores[0])}')
        print()
        print('Se escolher não puxar uma carta será o fim da jogada!')
        while True:
            mao = self.jogadores[0]
            escolha = str(input('\nPuxar uma carta (S/N)? ')).upper()
            print()
            pontos = Jogo21.verificar_pontos(mao)
            if escolha == 'S':
                c = choice(self.baralho)
                self.jogadores[0].append(c)
                self.baralho.remove(c)
                pontos = Jogo21.verificar_pontos(mao)
                print(f'Essa é a sua nova mão: {mao} \nE esses sao seus pontos {pontos}.')
                if pontos == 21:
                    print('Parabéns, você venceu!')
                    break
                elif pontos > 21:
                    print('Que pena, você perdeu!')
                    break
                else:
                    continue
            elif escolha == 'N':
                pf = {}
                self.comp()
                print(f'Pontos do jogador = {pontos}')
                cont = 1
                pf['Jogador'] = pontos
                for i in self.jogadores[1:4]:
                    pontos_finais = Jogo21.verificar_pontos(i)
                    print(f'Pontos do Bot {cont} = {pontos_finais}')
                    if pontos_finais <= 21:
                        pf[f'Bot {cont}'] = pontos_finais
                    cont += 1

                print()
                print(f'Vencedor dessa rodada = {max(pf, key=pf.get)}')
                break
            else:
                print('Digito Inválido! Tente novamente.')


deck = Baralho()
jogo = Jogo21(deck.criar_baralho())

jogo.distribuir_cartas()
jogo.jogar()
while True:
    op = input('\nDeseja continuar jogando(S/N)? ').upper()
    if op == 'S':
        print("\033c")
        jogo.jogar()
    elif op == 'N':
        break
    else:
        print('Digito invalido! Tente novamente.')
