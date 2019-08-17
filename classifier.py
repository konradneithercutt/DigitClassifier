import random
import gzip
import io
import pickle
import json
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tkinter as tk
from sklearn.neural_network import MLPClassifier

class Classifier(object):

    def __init__(self):
        self.save_new = False
        self.load_old = True
        self.training_images, self.training_labels, self.cv_images, self.cv_labels = self.load_training_cv_data()

        self.mlp = self.initialize_mlp()
        # self.show_digit(self.training_images[0], self.mlp.predict([self.training_images[0]]))


        # Testing the accuracy of the classifier on CV set.
        # predictions = self.mlp.predict(cv_images)
        # correct = 0
        # for i in range(len(predictions)):
        #     if(predictions[i] == self.cv_labels[i]):
        #         correct = correct + 1
        # print(correct, "labels out of", len(predictions), "labels predicted correctly")

    # initialized the MLP according to the specifications of save_new and load_old,
    # traning a new MLP if necessary.
    def initialize_mlp(self):
        if self.load_old:
            mlp = self.load_mlp()
        else:
            mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(784), max_iter=100, activation='logistic', random_state=1)
            mlp.fit(training_images[:40000], training_labels[:40000])
            if self.save_new:
                self.save_mlp(mlp)
        return mlp

    # Loads the data from the training image files and from the labels files and
    # returns them as an array of Examples which are (image, label) pairs.
    # Returns a tuple of such pairs, a test and a cross-validation set.
    def load_training_cv_data(self):
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

    def save_mlp(self, mlp):
        file = open("saved_mlp.pickle", "wb")
        pickle.dump(mlp, file)
        file.close()

    def load_mlp(self):
        file = open("saved_mlp.pickle", "rb")
        mlp = pickle.load(file, fix_imports=True, encoding="ASCII", errors="strict")
        file.close()
        return mlp

    # Returns a triple containing a random array of image_data, its predicted label
    # and its known label in that order
    def get_random_digit(self):
        rand_index = random.randint(0, 40000)
        image_data = None
        if rand_index < 40000:
            image_data = self.training_images[rand_index]
            gold_label = self.training_labels[rand_index]
            predicted_label = self.mlp.predict(image_data)

            image_data_array = []
            for i in range(0, 28):
                image_data_array.append(image_data[i*28:(i+1)*28])
            return (image_data_array, gold_label, predicted_label)
        else:
            # TODO -- allow an image from the CV set to be selected
            return None


    # Displays this example as a grayscale image:
    # Expects data to be 28x28 Array
    def show_digit(self, image_data, label):
        image_data_array = []
        for i in range(0, 28):
            image_data_array.append(image_data[i*28:(i+1)*28])
        plt.imshow(image_data_array, cmap=plt.get_cmap('gray'))
        plt.title("Label is " + str(label))
        plt.show()

if __name__ == "__main__":
    Classifier()
