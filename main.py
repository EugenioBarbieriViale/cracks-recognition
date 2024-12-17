import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

n_images = 5000

data_pos = []
data_neg = []

for i in range(1, n_images):
    if i < 10000 or i >= 19379:
        pos = mpimg.imread("./dataset/Positive/" + str(i).zfill(5) + ".jpg")
    else:
        pos = mpimg.imread("./dataset/Positive/" + str(i) + "_1.jpg")

    neg = mpimg.imread("./dataset/Negative/" + str(i).zfill(5) + ".jpg")

    data_pos.append(pos)
    data_neg.append(neg)

# plt.imshow(data_pos[1999])
# plt.axis('off')
# plt.show()

data_pos = np.array(data_pos)
data_neg = np.array(data_neg)

data_pos = data_pos / 255.0
data_neg = data_neg / 255.0
