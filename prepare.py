import os, logging, coloredlogs
import urllib.request
from tqdm.auto import tqdm

DL_DATASET = {
    'C1' : [
        None
    ],
    'C2' : [
        ('https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip', 'cats_and_dogs.zip'),
        ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip', None),
        ('https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5', None),
        ('https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip', None)
    ]
}

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

if __name__ == '__main__':
    coloredlogs.install()
    logging.info('Preparring Dataset for DeepLearning Course Exercise Notebook..')
    logging.info('Please choose subcourse')
    print('''C1 : Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning
C2 : Convolutional Neural Networks in TensorFlow
C3 : Natural Language Processing in TensorFlow
C4 : Sequences, Time Series and Prediction
a : all

Multiple subcourse selection Example:
C1 C4''')
    subcourse = input('Subcourse Selection : ').upper().split()
    if 'A' in subcourse:
        subcourse = ['C1', 'C2', 'C3', 'C4']
    for c in subcourse:
        for url, name in DL_DATASET[c]:
            if name == None:
                name = url.split('/')[-1]
            download_url(url, name)