import gzip
import io
import pickle
import json
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tkinter as tk
from sklearn.neural_network import MLPClassifier



save_new = False
load_old = True

def main():

    training_images, training_labels, cv_images, cv_labels = load_training_cv_data()

    if load_old:
        mlp = load_mlp()
    else:
        mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(784), max_iter=100, activation='logistic', random_state=1)
        mlp.fit(training_images[:40000], training_labels[:40000])
        if save_new:
            save_mlp(mlp)

    # predictions = mlp.predict(cv_images)
    # correct = 0
    # for i in range(len(predictions)):
    #     if(predictions[i] == cv_labels[i]):
    #         correct = correct + 1
    # print(correct, "labels out of", len(predictions), "labels predicted correctly")


# Loads the data from the training image files and from the labels files and
# returns them as an array of Examples which are (image, label) pairs.
# Returns a tuple of such pairs, a test and a cross-validation set.
def load_training_cv_data():
    all_images = []
    all_labels = []
    # A File containing the data for the training images
    # Here we open it to read bytes mode and convert it to a bytes_stream :
    train_images_file = gzip.open("E:\\Users\\Steven Marmorstein\\PyWorkspace\\MNIST\\train-images-idx3-ubyte.gz", "rb")
    bytes_stream_img_data = io.BytesIO(train_images_file.read())
    train_images_file.close()
    train_labels_file = gzip.open("E:\\Users\\Steven Marmorstein\\PyWorkspace\\MNIST\\train-labels-idx1-ubyte.gz", "rb")
    bytes_stream_labels_data = io.BytesIO(train_labels_file.read())
    train_labels_file.close()

    # getting the "magic number" at the start of the files out of the way:
    bytes_stream_img_data.read(4)
    bytes_stream_labels_data.read(4)
    # reading the number of images, rows, and columns from the header of the files:
    num_images = int.from_bytes(bytes_stream_img_data.read(4), byteorder='big')
    num_labels = int.from_bytes(bytes_stream_labels_data.read(4), byteorder='big')
    num_rows = int.from_bytes(bytes_stream_img_data.read(4), byteorder='big')
    num_cols = int.from_bytes(bytes_stream_img_data.read(4), byteorder='big')

    for m in range(0, num_images):
        image_data = []
        label = int.from_bytes(bytes_stream_labels_data.read(1), byteorder='big')
        all_labels.append(label)
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                val = int.from_bytes(bytes_stream_img_data.read(1), byteorder='big')
                image_data.append(val)

        all_images.append(image_data)

    bytes_stream_img_data.close()
    bytes_stream_labels_data.close()

    training_images = all_images[0:40000]
    training_labels = all_labels[0:40000]
    cv_images = all_images[40000:]
    cv_labels = all_labels[40000:]

    return (training_images, training_labels, cv_images, cv_labels)

def save_mlp(mlp):
    file = open("saved_mlp.pickle", "wb")
    pickle.dump(mlp, file)
    file.close()

def load_mlp():
    file = open("saved_mlp.pickle", "rb")
    mlp = pickle.load(file, fix_imports=True, encoding="ASCII", errors="strict")
    file.close()
    return mlp

# Displays this example as a grayscale image:
# Expects data to be 28x28 Array
def show_digit(image_data, label):
    image_data_array = []
    for i in range(0, 28):
        image_data_array.append(image_data[i*28:(i+1)*28])
    plt.imshow(image_data_array, cmap=plt.get_cmap('gray'))
    plt.title("Label is " + str(label))
    plt.show()


if __name__ == "__main__":
    main()
