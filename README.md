# Programacao Matematica
Atividade de Programacao Matematica 2021.1

Clone o repositorio e use as variaveis
* obj_func - função objetivo
* obj - Maximização (MAX) ou Miminização (MIN)
* restricoes - restrições (apenas "<=")

No arquivo PM.ipynb (jupyter notebook) ou atribua por linha de comando no PM.py para definir o problema, depois execute

Observações:
* APENAS MAXIMIZAÇÃO IMPLEMENTADA E RESTRIÇÕES "<="
* Variaveis devem ser adicionadas as expressões em ordem alfabetica
* Selecione entre minimização ('MIN') e maximização ('MAX')
* Para cada restrição fi, escreva na forma ['f1','f2'...'fn']


Exemplo:

Maximizar: 3x + y

Com as restrições:
* x + y <= 100
* 5x + 2y <= 300

No arquivo PM.ipynb (jupyter notebook)

* obj_func = '3x + y'
* obj = 'MAX'
* restricoes = ['x + y <= 100', '5x + 2y <= 300']

Ou atribua por linha de comando no PM.py

Para utilizar valores negativos use o coeficiente -1 junto com o sinal de soma, exemplo, para adicionar a restrição 2x - y use '2x + -1y'
