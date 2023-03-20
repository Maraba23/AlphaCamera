import numpy as np
import cv2 as cv

# Cria uma matriz com todas as combinações possíveis de índices entre os limites definidos
def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack((idx_i, idx_j))
    return idx

# Aplica uma rotação na imagem com o ângulo especificado
def rotate_image(image, angle):
    width = image.shape[1] # Largura da imagem
    height = image.shape[0] # Altura da imagem

    # Cria a matriz com todos os índices da imagem
    X = criar_indices(0, width, 0, height)
    X = np.vstack((X, np.ones(X.shape[1])))

    # Matriz de translação que move a imagem para o centro da matriz
    T = np.array([[1, 0, -width / 2], [0, 1, -height / 2], [0, 0, 1]])
    # Matriz de rotação que aplica a rotação na imagem
    R = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    # Matriz de translação que move a imagem de volta para a posição original
    T2 = np.array([[1, 0, width / 2], [0, 1, height / 2], [0, 0, 1]])

    # Aplica as matrizes de transformação na matriz de índices
    Xd = T @ X
    Xd = R @ Xd
    Xd = T2 @ Xd

    # Converte os índices para inteiros
    Xd = Xd.astype(int)
    X = X.astype(int)

    # Garante que os índices estejam dentro dos limites da imagem
    Xd[0, :] = np.clip(Xd[0, :], 0, width - 1)
    Xd[1, :] = np.clip(Xd[1, :], 0, height - 1)

    # Cria uma imagem preta com as mesmas dimensões da imagem original
    image2 = np.zeros_like(image)

    # Verifica quais índices são válidos e copia os valores da imagem original para a nova imagem
    valid_indices = np.logical_and(Xd[0, :] >= 0, Xd[0, :] < width)
    valid_indices = np.logical_and(valid_indices, Xd[1, :] >= 0)
    valid_indices = np.logical_and(valid_indices, Xd[1, :] < height)
    image2[Xd[1, valid_indices], Xd[0, valid_indices], :] = image[X[1, valid_indices], X[0, valid_indices], :]

    return image2

# Captura o vídeo da câmera, aplica a rotação e o filtro e exibe na janela do OpenCV
def run():
    cap = cv.VideoCapture(0)

    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    angle = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (320, 240), interpolation=cv.INTER_AREA)

        image = np.array(frame).astype(float) / 255

        image2 = rotate_image(image, angle)
        filtro = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        image2 = cv.filter2D(image2, -1, filtro)

        cv.imshow('frame', image2)

        angle += np.pi / 50.0

        if angle > 2 * np.pi:
            angle -= 2 * np.pi

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    run()