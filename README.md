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

Para rotacionar a imagem, é necessário aplicar três transformações sucessivas: translação, rotação e translação inversa. Primeiro, a imagem é movida para que seu centro coincida com a origem. Em seguida, a imagem é rotacionada em torno da origem. Finalmente, a imagem é movida de volta para sua posição original.

A translação é realizada por meio da adição ou subtração de um valor constante em todas as coordenadas da imagem. A rotação é realizada por meio de uma matriz de rotação que multiplica as coordenadas da imagem. A translação inversa é realizada por meio da adição ou subtração de um valor constante em todas as coordenadas da imagem novamente.

O código começa inicializando a câmera, capturando um quadro de vídeo e redimensionando-o para uma resolução menor. Em seguida, a imagem é normalizada para que os valores dos pixels fiquem no intervalo [0,1] em vez de [0,255]. Isso é feito dividindo cada valor de pixel por 255.

Depois disso, a função rotate_image é chamada, recebendo a imagem e um ângulo de rotação como parâmetros. A função cria uma matriz de coordenadas usando a função criar_indices, que retorna uma matriz com as coordenadas x e y de todos os pixels da imagem. Essa matriz é usada para calcular as novas coordenadas dos pixels após a rotação.

A matriz de coordenadas é então transformada usando a matriz de translação, matriz de rotação e matriz de translação inversa. As matrizes de transformação são criadas usando funções da biblioteca numpy, que é uma biblioteca de computação científica para Python. A matriz resultante é então usada para mapear os pixels da imagem original para as suas novas posições na imagem rotacionada.

A nova imagem é retornada pela função rotate_image e exibida na tela usando a função imshow da biblioteca OpenCV. O ângulo de rotação é aumentado a cada quadro para que a imagem continue girando em torno de seu centro.

Por fim, o programa é encerrado quando o usuário pressiona a tecla "q". A câmera é liberada e todas as janelas abertas são fechadas usando a função destroyAllWindows da biblioteca OpenCV.
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

