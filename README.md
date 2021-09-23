# Measuring the Ripeness of Fruit with Hyperspectral Imaging and Deep Learning

Here you can find the dataset and the official implementation of the HS-CNN network.

## Dataset
The dataset is [here](https://cloud.cs.uni-tuebingen.de/index.php/s/nWKxxtN5wM9fz5E) available. It contains 1038 hyperspectral recordings of avocados and 1522 hyperspectral recordings of kiwis. The ripening process from unripe to overripe is covered. Because of the destructive manner of the labeling process, only 180 avocado recordings and 262 kiwis recordings are labeled by indicator measurements.
Two cameras (Specim FX 10 and INNO-SPEC Redeye 1.7) were used. The two measurement series cover a total of 28 days in the years 2019 and 2020.

## HS-CNN
This is the official implementation of the HS-CNN network. The implementation is based on PyTorch and PyTorch Lightning.

The code is divided into subfolders, which correspond to the use cases:
 - 'classification' contains the training process for the classification task. Here you can find the implementation of HS-CNN, AlexNet, ResNet-18, SVM and kNN.
 - 'extract_fruit' trains a layer classifier and extracts the fruits.
 - 'false_color_images' defines the two stage training process of the autoencoder and the classification network. This allows the visualization of the ripening process.
 - 'core' contains the basic components. (IO, loss functions)


             
## Citation
The paper was be presented on IJCNN 2021.
```
@inproceedings{Varga2021,
abstract = {We present a system to measure the ripeness of fruit with a hyperspectral camera and a suitable deep neural network architecture. This architecture did outperform competitive baseline models on the prediction of the ripeness state of fruit. For this, we recorded a data set of ripening avocados and kiwis, which we make public. We also describe the process of data collection in a manner that the adaption for other fruit is easy. The trained network is validated empirically, and we investigate the trained features. Furthermore, a technique is introduced to visualize the ripening process.},
archivePrefix = {arXiv},
arxivId = {2104.09808},
author = {Varga, Leon Amadeus and Makowski, Jan and Zell, Andreas},
booktitle = {2021 International Joint Conference on Neural Networks (IJCNN)},
doi = {10.1109/IJCNN52387.2021.9533728},
eprint = {2104.09808},
isbn = {978-1-6654-3900-8},
keywords = {Index Terms-hyperspectral,convolutional neu-ral network,deep learning,ripening fruit},
month = {jul},
pages = {1--8},
publisher = {IEEE},
title = {{Measuring the Ripeness of Fruit with Hyperspectral Imaging and Deep Learning}},
url = {https://arxiv.org/abs/2104.09808v1 http://arxiv.org/abs/2104.09808 https://ieeexplore.ieee.org/document/9533728/},
year = {2021}
}

```

