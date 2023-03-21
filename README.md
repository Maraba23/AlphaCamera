# AlphaCamera
## Authors

- [Marcelo Rabello Barranco](https://www.github.com/Maraba23)
- [Thomas Chiari Ciocchetti de Souza](https://www.github.com/thomaschiari)




## Features

- Imagem roda para sempre no sentido horario


## Helps

 - [chatgpt](https://openai.com/blog/chatgpt)

## About

O código em questão é um exemplo de como rotacionar uma imagem em torno do seu centro usando transformações geométricas. As transformações geométricas são operações matemáticas que podem ser usadas para transformar uma imagem em diversas maneiras, como por exemplo, transladar, girar, escalar, espelhar e distorcer.

A imagem é representada por uma matriz de pixels, onde cada pixel contém informações sobre a cor e a posição daquele ponto na imagem. A posição dos pixels é determinada por suas coordenadas no sistema de coordenadas cartesiano. A coordenada (0,0) é o canto superior esquerdo da imagem e as coordenadas aumentam em direção ao canto inferior direito.

Usamos então uma matriz $X_{i,j}$ onde $x_{i,j}$ é i-ésima cordenada do j-ésimo pixel da imagem.

Para rotacionar a imagem, é necessário aplicar três transformações sucessivas: translação, rotação e translação inversa. Primeiro, a imagem é movida para que seu centro coincida com a origem.

Para isso usamos a matriz:

$$
T = \begin{bmatrix}
1 & 0 & -width/2 \\
0 & 1 & -height/2 \\
0 & 0 & 1
\end{bmatrix}
$$

Com isso conseguimos chegar na origem da imagem tirando a metade da largura e da altura da imagem.

Em seguida, a imagem é rotacionada em torno da origem.

Para isso usamos a matriz:

$$
R = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

onde $\theta$ eh sempre atualizado para que a imagem continue girando em torno do seu centro.
 
Finalmente, a imagem é movida de volta para sua posição original.

Usando a matriz:
$$
T2 = \begin{bmatrix}
1 & 0 & width/2 \\
0 & 1 & height/2 \\
0 & 0 & 1
\end{bmatrix}
$$

Em suma, jogamos nossa imagem para o ponto (0,0) e a rotacionamos em torno do ponto (0,0), e depois a movemos de volta para o ponto (width/2, height/2), que é o centro da imagem.

Para isso são realizadas as seguintes operações:
```python
Xd = T @ X # Translada a imagem para a origem
Xd = R @ Xd # Rotaciona a imagem em torno da origem
Xd = T2 @ Xd # Translada a imagem de volta para o centro
```

Em seguida clipamos a matriz Xd para não ficar com pixels fora da imagem original.

## Running Tests

Primeiro, instale as dependências do projeto.

```bash
  pip install -r requirements.txt
```

Para rodar, apenes execute o arquivo Alpha Camera ou execute no terminal

```bash
  python AlphaCamera.py
```

Para finalizar o programa, pressione a tecla "q".

