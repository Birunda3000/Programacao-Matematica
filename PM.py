import simplex
obj_func = "10x + y" # ---DEFINA A FUNÇÃO OBJETIVO AQUI---
obj = 'MAX' # APENAS MAXIMIZAÇÃO IMPLEMENTADA
restricoes = ['x + y <= 200', '2x + 2y <= 600'] # ---DEFINA AS RESTRIÇÕES AQUI---
simplex = simplex.Simplex(obj_func, obj)
if len(restricoes) > 0:
    for k in restricoes:
        simplex.add_constraints(k)
solucao = simplex.solve()
for var in simplex.coefficients:
    print("Valor de {}: {}".format(var, solucao[var]))
print('\n-Solução: {}-'.format(solucao['solution']))