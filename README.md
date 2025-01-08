# Notas Uniasselvi LeoAPP
 Algoritmo para saber quanto você precisa para passar em uma matéria no curso da UNIASSELVI

 Erros:
   Erro 1: Você precisa colocar o somatório total equivalente a 10 (pois é possível que o peso das notas mudem, como já aconteceu)
        
   Erro 2: Você precisa colocar uma das opções que está no painel, se não, será considerada como um erro

Dúvidas: 
   O que é peso e o que é nota? 
    Peso é o equivalente ao quanto aquela prova pode te dar de pontuação. Geralmente ele é de acordo com a dificuldade e segue numa somatória com outras provas (ex: a prova 1 pesa 2.00, a prova 2 pesa 3.00 e a prova 3 pesa 5.00. Seguindo a somatória, seria 2.00 + 3.00 + 5.00 = 10.00)

   
   Já a nota seria a pontuação que você recebe ao fazer uma prova. Geralmente é de 0.00 até 10.00 e depende exclusivamente do seu desempenho

   Nesse modelo, se você tirar uma nota 5.00 na prova 1, a sua pontuação final naquela prova seria de:
   5.00 * 2.00 / 10.00 = 1.00 (Sua nota, Peso da prova, Soma dos pesos de todas as provas )
   Continuando, se você tirar 10.00 na prova 2 e 8.00 sua nota final ficaria assim:
   ((5.00 * 2.00) + (10.00 * 3.00) + (8.00 * 5.00) / 10) = 8.00
        
   Dependendo da média (no caso da UNIASSELVI, seria 7.00) você pode saber se passou ou não
    
   E por que esse algoritmo?
    Estava com dificuldade de saber exatamente quanto eu precisava para passar na matéria fazendo a última prova. Vendo o cálculo, é muito complicado fazer várias vezes para saber uma nota só, principalmente se você tem dificuldade em matemática (O que não é o caso) e então preferi juntar um problema que eu tinha com python e BOOM.

Observações:
    Mesmo que não seja tão necessário esse código, se for preciso eu posso atualizar e analisar forks e issues de acordo com as métricas atuais da UNIASSELVI, seja opções de mudança de média, quantidade de provas, ou até mesmo redundâncias ou erros no código. O objetivo é analisar, testar e aprender com o código, pois fiz tanto para resolver um problema quanto praticar meus conhecimentos.
