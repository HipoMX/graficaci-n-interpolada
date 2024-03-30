import numpy as np
import imageio
from scipy import ndimage

# Cargar la imagen en escala de grises
image = imageio.imread('perro.png', as_gray=True)

# Aplicar el filtro de mediana con un tamaño de ventana de 5x5 píxeles
filtered_image = ndimage.median_filter(image, size=5)

# Guardar la imagen filtrada en un archivo de imagen
imageio.imwrite('perro_filtered.png', filtered_image)

# Mostrar las imágenes original y filtrada
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(image, cmap='gray')
ax1.set_title('Imagen original')
ax2.imshow(filtered_image, cmap='gray')
ax2.set_title('Imagen filtrada')
plt.show()