A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
Z = np.dot(A,B)   # results in [[0, 2], [0, 2]])
np.sin(Z)   # results in [[0.        , 0.90929743],   [0.        , 0.90929743]]
C = np.array([[1,1],[2,2],[3,3]])   # calculate the transposed matrix
C   # results in [[1, 1],        [2, 2],       [3, 3]]
C.T   # results in [[1, 2, 3],     [1, 2, 3]]

