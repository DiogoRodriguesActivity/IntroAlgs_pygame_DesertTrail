# Proposta Inicial do Jogo

## Desert Trail
<table border="0" width="100%">
  <tr>
    <td width="60%" valign="top">
      <p>
        Desert Trail é um jogo de plataformas e fases, que envolve uma cativante aventura do nosso protagonista NickName, uma nobre aventureira que tem como objetivo passar pelos árduo             desafios do Deserto do Egito, a fim de derrotar uma Esfinge que atormenta a sua vila com pragas. Passe por desafios de plataforma e derrote a Esfinge no final da Fase.
      </p>
</br>
      <p>
        Todos os direitos autorais reservados ao Criadores do Jogo (Presente no topico 2)
      </p>
    </td>
    <td width="40%" valign="top" align="center">
      <img src="assets\imagens\LogoJogo.png" alt="Logo do Jogo" width="100%">
    </td>
  </tr>
</table>

## 1. Nome provisório do jogo

> Desert Trail

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Nathan Junquer de Almeida Castro
- Nome 2: Isaque de Jesus Marra
- Nome 3: Diogo Rodrigues da Silva
- Nome 4: Gabriel Silva Dias

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Tipo escolhido pelo grupo:

> Jogo de plataforma com fases, obstáculos e sistema de perguntas e respostas.

## 4. Descrição geral do jogo

Descrição:

> Desert Trail será um jogo de plataforma em 2D com cenário de deserto. O jogador controlará um personagem que precisa atravessar três fases, pulando entre plataformas e desviando de obstáculos. Nas duas primeiras fases, se o jogador morrer, ele volta para a fase inicial. Na terceira fase, haverá uma bossfight, em que o jogador precisará responder perguntas corretamente para derrotar o chefe final

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Objetivo:

> O objetivo principal do jogador é atravessar as três fases, evitar obstáculos, manter suas vidas e derrotar o chefe final na última fase respondendo corretamente às perguntas.

## 6. Regras principais

Liste as principais regras do jogo.

Regras do grupo:
- Regra 1: Cada colisão com obstáculo ele volta para a fase inicial.
- Regra 2: O jogador vence quando passar as três fases.
- Regra 3: O jogador tera 3 vidas na bossfight 
- Regra 4: Caso o jogador erre alguma pergunta, ele perde uma vida
- Regra 5: Se o jogador perder as três vidas ele volta para o inicio 
- Regra 6: Para derrotar o boss, o jogador precisa responder perguntas    corretamente.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Condição de vitória:

> O jogador vence o jogo quando completa as três fases e derrota o chefe final na terceira fase, respondendo corretamente às perguntas da batalha final.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Condição de derrota ou encerramento:

> O jogador perde se ficar sem vidas ou colide com algum obstáculo. A partida também pode ser encerrada caso o jogador feche o jogo ou escolha sair pelo menu.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Descrição:

> O jogador controlará um personagem em 2D em um cenário de deserto. Esse personagem poderá andar para a esquerda, andar para a direita e pular sobre plataformas. O objetivo dele será atravessar as fases, evitar obstáculos e chegar até o final do caminho.

## Obstáculos, inimigos ou desafios

Descrição:

> O jogo terá obstáculos como buracos, espinhos, plataformas difíceis e outros perigos do cenário. O jogador precisará desviar desses obstáculos para não perder vidas. Na terceira fase, haverá um boss final, que será derrotado por meio de perguntas e respostas.

## Itens, alvos ou objetos de interação

Descrição:

> O jogo terá placas ou objetos de interação para indicar o caminho, explicar comandos ou iniciar as perguntas da bossfight.

## Pontuação, vidas, tempo ou progresso

Descrição:

> Nas duas primeiras fases, o jogador não terá sistema de vidas: se morrer, cair em um buraco ou encostar em um obstáculo perigoso, voltará para a fase inicial. O sistema de vidas será usado apenas na bossfight da terceira fase. Durante a luta contra o boss, o jogador terá uma quantidade limitada de vidas e perderá vida ao responder perguntas incorretamente. O progresso do jogo será representado pela fase atual e, na bossfight, pela quantidade de perguntas respondidas corretamente.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Controles do grupo:

- Seta para esquerda ou tecla A: mover o personagem para a esquerda.
- Seta para direita ou tecla D: mover o personagem para a direita.
- Espaço ou seta para cima: pular.
- Teclas 1, 2, 3 ou 4: escolher alternativas nas perguntas.
- ESC: sair ou pausar o jogo.

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Organização planejada:

> main.py: inicia o jogo e controla o loop principal.

> config.py: guarda informações como tamanho da tela, cores, FPS, velocidade e gravidade.

> player.py: fica responsável pelo personagem, como movimentação, pulo e colisões.

> fases.py: guarda as informações das fases, como plataformas, obstáculos e final da fase.

> boss.py: controla a parte do chefe final e as vidas durante a bossfight.

> perguntas.py: guarda as perguntas, alternativas e respostas certas.

> funcoes.py: guarda funções auxiliares, como desenhar textos, carregar imagens e reiniciar o jogo.


## 12. Recursos externos previstos

Recursos previstos:

> Sons gratuitos, imagens obtidas de banco gratuito, animações, fonte personalizada.

Todas as músicas e efeitos sonoros foram tiradas no site: www.pixabay.com

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Dificuldades previstas:

- Dificuldade 1: Criar a movimentação do jogador com pulo, gravidade e colisão com plataformas.

- Dificuldade 2: Organizar o código de forma clara, separando fases, personagem, obstáculos e perguntas.

- Dificuldade 3: Testar o jogo para corrigir erros de colisão, perda de vidas, troca de fases e funcionamento da bossfight.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Escopo mínimo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, três fases simples, obstáculos aparecendo na tela, sistema de vidas, uma bossfight com perguntas e respostas e uma tela de fim de jogo. O jogador deverá conseguir perder vidas, passar de fase e vencer ao derrotar o boss final.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Melhorias possíveis:


| Funcionalidades | Status | Nome do Programador |
| :--- | :---: | :---: |
| Um Menu para o Jogo, com a logo do Jogo, background e com o Botão de Começar e o de Sair | [Diogo, Nathan, Isaque] | X |
| Um Personagem que muda de Sprite quando está andando | [Natham] | X |
| Documentação de como jogar o jogo | [Diogo] | X |
| A Customização da Fase Final, junto com o boneco da Esfinge (pode colocar uma cena de Dialogo com a Esfinge antes de começar a fase final) | [Diogo] | (Não feito) |
| A Fase 1 Completa, além de pensar no inimigo do Jogo (Falta apenas criar um sistema de mortes) | [Diogo e Gabriel Silva] | X |

| --------- Não Obrigatório --------------- | | |
| :--- | :---: | :---: |
| Musica para o Menu, para a Fase e para o Inimigo Final | [Isaque] | X |
| O personagem também mudará de Sprite quando estiver pulando ou caindo | [Nathan] | (Não feito)|.
