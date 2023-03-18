import numpy as np
import cv2 as cv


def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack((idx_i, idx_j))
    return idx


def rotate_image(image, angle):
    width = image.shape[1]
    height = image.shape[0]

    X = criar_indices(0, width, 0, height)
    X = np.vstack((X, np.ones(X.shape[1])))

    T = np.array([[1, 0, -width / 2], [0, 1, -height / 2], [0, 0, 1]])
    R = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    T2 = np.array([[1, 0, width / 2], [0, 1, height / 2], [0, 0, 1]])

    Xd = T @ X
    Xd = R @ Xd
    Xd = T2 @ Xd

    Xd = Xd.astype(int)
    X = X.astype(int)

    Xd[0, :] = np.clip(Xd[0, :], 0, width - 1)
    Xd[1, :] = np.clip(Xd[1, :], 0, height - 1)

    image2 = np.zeros_like(image)

    # Ensure that the indices are within the valid range of the image2 array
    valid_indices = np.logical_and(Xd[0, :] >= 0, Xd[0, :] < width)
    valid_indices = np.logical_and(valid_indices, Xd[1, :] >= 0)
    valid_indices = np.logical_and(valid_indices, Xd[1, :] < height)

    # Only copy the values for the valid indices
    image2[Xd[1, valid_indices], Xd[0, valid_indices], :] = image[X[1, valid_indices], X[0, valid_indices], :]
    return image2


def run():
    cap = cv.VideoCapture(0)

    width = 320
    height = 240

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

        image = np.array(frame).astype(float) / 255

        center = (width / 2, height / 2)
        angle = -45
        scale = 1

        # Compute rotation matrix
        M = cv.getRotationMatrix2D(center, angle, scale)

        # Apply rotation to image
        image2 = cv.warpAffine(image, M, (width, height), flags=cv.INTER_LINEAR, borderMode=cv.BORDER_CONSTANT,
                               borderValue=(0, 0, 0))

        cv.imshow('frame', image2)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


run()
