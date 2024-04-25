Este documento descreve as funções implementadas em uma calculadora científica em Python. As funções incluem operações matemáticas como exponencial, logaritmo, trigonometria e constantes matemáticas como π.

## Estrutura do Código

O código da calculadora científica está organizado em um único arquivo Python `calculadora_cientifica.py` contendo as seguintes funções:

1. **`opcoes()`**: Exibe um menu de opções para escolher e calcular diferentes funções matemáticas.

2. **Funções Matemáticas**:
   - `e(x, precisao=100)`: Calcula a função exponencial `e^x` usando a série de Taylor.
   - `ln(x, precisao=100)`: Calcula o logaritmo natural `ln(x)` usando a série de Taylor.
   - `log(x, precisao=100)`: Calcula o logaritmo `log(x)`usando a função `ln(x)/ln(10)`.
   - `sen(x, precisao=100)`: Calcula o seno `sin(x)` usando a série de Taylor.
   - `cos(x, precisao=100)`: Calcula o cosseno `cos(x)` usando a série de Taylor.
   - `tg(x, precisao=100)`: Calcula a tangente `tan(x)` usando a série de Taylor.
   - `sqrt(x, precisao=100)`: Calcula a raiz quadrada `sqrt(x)` usando a série de Taylor.
   - `pi(precisao=1000)`: Calcula o valor de π (pi) usando a série de Leibniz.
   - `factorial(n)`: Calcula o fatorial de um número inteiro `n`.
   - `binomial(a, n)`: Calcula o coeficiente binomial `C(a, n)`.

## Utilização

Para utilizar a calculadora científica:

1. Execute o script Python `calculadora_cientifica.py`.
2. O menu de opções será exibido, permitindo a escolha de uma função matemática.
3. Digite o número da opção desejada e forneça os parâmetros necessários quando solicitado.
4. O resultado da função escolhida será exibido na tela.

## Observações

- Certifique-se de inserir valores válidos para os cálculos, pois algumas funções têm restrições de domínio (por exemplo, logaritmo natural para `x > 0`, raiz quadrada para `x >= 0`, etc.).
- As funções matemáticas utilizam séries de Taylor para calcular os valores aproximados, e a precisão pode ser ajustada por meio dos parâmetros `precisao`.

## Referências

O código da calculadora científica foi implementado com base em conceitos matemáticos e séries numéricas. Consulte a documentação interna das funções para obter mais detalhes sobre os métodos utilizados.
