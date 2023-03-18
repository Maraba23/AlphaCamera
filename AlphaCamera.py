import numpy as np

# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 320
    height = 240

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        
        # Aqui, vamos criar um índice para acessar os pixels da imagem
        X = criar_indices(0, width, 0, height)
        X = np.vstack ( (X, np.ones( X.shape[1]) ) )        
        # vamos jogar nossa imagem para a origem
        T = np.array( [ [1, 0, -width/2], [0, 1, -height/2], [0, 0, 1] ] )
        # vamos rotacionar a imagem em 45 graus
        R = np.array( [ [np.cos(np.pi/4), -np.sin(np.pi/4), 0], [np.sin(np.pi/4), np.cos(np.pi/4), 0], [0, 0, 1] ] )
        # vamos transladar a imagem para a direita
        T2 = np.array( [ [1, 0, width/2], [0, 1, height/2], [0, 0, 1] ] )
        # vamos aplicar a transformação
        Xd = T @ X
        Xd = R @ Xd
        Xd = T2 @ Xd
        # vamos recuperar os índices
        Xd = Xd.astype(int)
        X = X.astype(int)
        
        Xd[0, :] = np.clip(Xd[0, :], 0, width-1)
        Xd[1, :] = np.clip(Xd[1, :], 0, height-1)

        image2 = np.zeros_like(image)

        image2[Xd[0, :], Xd[1, :], :] = image[X[0, :], X[1, :], :]

        cv.imshow('frame', image2)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()
