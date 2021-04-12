import os, logging, coloredlogs
import urllib.request
from tqdm.auto import tqdm

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path, name):
    try:
        with DownloadProgressBar(unit='B', unit_scale=True,
                                miniters=1, desc=name) as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)
    except:
        logging.error(f'Failed to download {name}')

class DlAssetsDownloader:
    DIR = 'DeepLearning.AI TensorFlow Developer'
    DL_DATASET = {
        'C1' : [
            ("https://storage.googleapis.com/laurencemoroney-blog.appspot.com/happy-or-sad.zip", None),
            ("https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz", None)
        ],'C2' : [
            ('https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip', 'cats_and_dogs.zip'),
            ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip', None),
            ('https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5', None),
            ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip', None),
            ('https://query.data.world/s/3h2vsf75bfvsv5nykuomi24t5emlzn', 'sign_mnist_train.csv'),
            ('https://query.data.world/s/n7oielhqmoppgbwlhblruenw54o7wi', 'sign_mnist_test.csv')
        ],'C3' : [
            ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/bbc-text.csv', None),
            ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/training_cleaned.csv', None),
            ('https://ia803006.us.archive.org/1/items/glove.6B.50d-300d/glove.6B.50d.txt', None),
            ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sonnets.txt', None)
        ], 'C4' : [
            ('https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv', None)
        ]
    }

    def prep_input(self, inputs):
        subcourse = {'C1' : '01. Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning',
                     'C2' : '02. Convolutional Neural Networks in TensorFlow',
                     'C3' : '03. Natural Language Processing in TensorFlow',
                     'C4' : '04. Sequences, Time Series and Prediction'}
        if 'A' in inputs:
            return list(subcourse.items())
        return [(x, subcourse[x]) for x in inputs]

    def main(self):
        logging.info(f'Menyiapkan Dataset untuk Exercise Notebook pada {self.DIR} Course..')
        logging.info('Masukkan subcourse..')
        print('''C1 : Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning
C2 : Convolutional Neural Networks in TensorFlow
C3 : Natural Language Processing in TensorFlow
C4 : Sequences, Time Series and Prediction
a : all

Contoh memilih lebih dari 1 subcourse:
C1 C4''')
        subcourse = self.prep_input(input('Pilihan Subcourse : ').upper().split())
        for c, C in subcourse:
            logging.info(f'Downloading dataset for {C}')
            loc = os.path.join(self.DIR, C, 'Exercise', 'tmp2')
            os.mkdir(loc)
            for url, name in self.DL_DATASET[c]:
                if name == None:
                    name = url.split('/')[-1]
                download_url(url, os.path.join(loc, name), name)

class MLAssetsDownloader:
    DIR = 'Math for Machine Learning'
    DL_DATASET = [
        ('https://query.data.world/s/6z5gojkvkzpwc6remnip26vdwz6txt', 'mnist-original.mat'),
        ('https://query.data.world/s/733ktfuuqdio6gjrmkknourchhhlzp', 'eigenfaces.npy')
    ]

    def main(self):
        logging.info(f'Menyiapkan Dataset untuk Exercise Notebook pada {self.DIR} Course..')
        loc = os.path.join(self.DIR, '03. PCA', 'Notebook', 'tmp2')
        os.mkdir(loc)
        for url, name in self.DL_DATASET:
            if name == None:
                name = url.split('/')[-1]
            download_url(url, os.path.join(loc, name), name)

DL_PREP = DlAssetsDownloader()
ML_PREP = MLAssetsDownloader()

if __name__ == '__main__':
    coloredlogs.install()
    DL_PREP.main()
    ML_PREP.main()

    logging.info('Selesai!')