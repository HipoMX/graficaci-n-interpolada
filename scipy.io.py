import numpy as np
from scipy.io import loadmat, savemat

# Crear un array de NumPy
arr = np.array([[1, 2], [3, 4]])

# Guardar el array en un archivo .mat
savemat('mi_archivo.mat', {'my_array': arr})

# Cargar el archivo .mat y acceder al contenido
mat_contents = loadmat('mi_archivo.mat')
loaded_arr = mat_contents['my_array']

# Mostrar el array original y el array cargado
print('Array original:')
print(arr)
print('Array cargado:')
print(loaded_arr)