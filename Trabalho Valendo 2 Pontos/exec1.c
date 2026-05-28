PARTE 1 — Pesquisa e Fundamentação (0,5 ponto)
Questão 1 — Pensamento Computacional
Pesquise e responda:
A) O que é pensamento computacional?
O pensamento computacional é um método de resolução de problemas baseado em técnicas da ciência da computação.
B) Explique os conceitos:
⦁	decomposição = Dividir um problema complexo em partes menores e mais fáceis de gerenciar.
⦁	abstração = Filtrar detalhes desnecessários, focando apenas nas informações essenciais para resolver o problema.
⦁	reconhecimento de padrões = Identificar semelhanças, tendências ou repetições entre os problemas para usar soluções anteriores.
⦁	algoritmo = Criar um conjunto de instruções passo a passo, claras e ordenadas, para resolver o desafio.
C)Explique a diferença entre:
⦁	AND (&&) = Exige que todas as condições sejam verdadeiras para o resultado ser verdadeiro. Se apenas uma falhar, o resultado é falso.
⦁	OR (||) = Exige que pelo menos uma condição seja verdadeira para o resultado ser verdadeiro. Ele só é falso se todas falharem.

PARTE 2 — Tabela Verdade (0,5 ponto)
Questão 2 — Tabela Verdade
Considere:
p = idade >= 18
q = possuiCarteira == 1

A) Complete a tabela verdade para:
p && q
p	q	p && q
V	V	v
V	F	F
F	V	F
F	F	F

B) Complete a tabela verdade para:
p || q
 | p | q | p || q |
|---|---|--------|
| V | V |    V         |
| V | F |    V        |
| F | V |    V      |
| F | F |    F       |

PARTE 3 — Programação Prática (1,0 ponto)
https://www.programiz.com/online-compiler/6n6SuHs62mEuB

FLUXOGRAMA

[INÍCIO]
   │
   ▼
[Declarar variáveis: idades[10], possuiAutorizacao, liberadas=0, negadas=0, maiorIdade=0, somaIdades=0, i=0]
   │
   ▼
┌───────────────────────────────┐
│ LOOP FOR (i de 0 até 9)       │◄─────────────────────────────────────────┐
└──────────────┬────────────────┘                                          │
               │ (Se i < 10)                                               │
               ▼                                                           │
     [Ler idade do participante]                                           │
     [Armazenar em idades[i]]                                              │
               │                                                           │
               ▼                                                           │
     [Ler possuiAutorizacao (1 ou 0)]                                      │
               │                                                           │
               ▼                                                           │
      /                     \                                              │
     < idade[i] >= 18 OU     >                                             │
     < possuiAutorizacao == 1>                                             │
      \                     /                                              │
         /               \                                                 │
  (Sim) /                 \ (Não)                                          │
       ▼                   ▼                                               │
[Exibir: LIBERADA]   [Exibir: NEGADA]                                      │
[liberadas =         [negadas =                                            │
 liberadas + 1]       negadas + 1]                                         │
       \                   /                                               │
        \─────────────────/                                                │
                 │                                                         │
                 ▼                                                         │
       /                    \                                              │
      <  idades[i] >         >                                             │
      <  maiorIdade          >                                             │
       \                    /                                              │
          /              \                                                 │
   (Sim) /                \ (Não)                                          │
        ▼                  ▼                                               │
 [maiorIdade = idades[i]]  [Manter maiorIdade]                             │
        \                  /                                               │
         \────────────────/                                                │
                 │                                                         │
                 ▼                                                         │
[somaIdades = somaIdades + idades[i]]                                      │
                 │                                                         │
                 ▼                                                         │
          [Incrementar i++] ───────────────────────────────────────────────┘
                 │
                 │ (Quando i chega a 10)
                 ▼
       [Calcular média = somaIdades / 10]
                 │
                 ▼
       [Exibir total de liberadas]
       [Exibir total de negadas]
       [Exibir maiorIdade registrada]
       [Exibir média calculada]
                 │
                 ▼
              [FIM]

              
Pseudocódico

Algoritmo "Acesso_Direto"

Variáveis
   idades: vetor [1..10] de inteiro
   autorizado, liberadas, negadas, maior, i: inteiro
   soma: real

Início
   Para i de 1 ate 10 Faca
      Leia(idades[i])
      Leia(autorizado)

      Se (idades[i] >= 18) OU (autorizado = 1) Entao
         Escreva("ENTRADA LIBERADA")
         liberadas <- liberadas + 1
      Senao
         Escreva("ENTRADA NEGADA")
         negadas <- negadas + 1
      FimSe

      Se idades[i] > maior Entao
         maior <- idades[i]
      FimSe

      soma <- soma + idades[i]
   FimPara

   Escreva("Liberadas: ", liberadas)
   Escreva("Negadas: ", negadas)
   Escreva("Maior idade: ", maior)
   Escreva("Média: ", soma / 10)
FimAlgoritmo