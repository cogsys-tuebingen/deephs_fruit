from classification.models import (
    AlexNet,
    ClassifierNetwork,
    DeepHSNet_with_HyVEConv,
    resnet18,
    se_resnet18,
    SpectralNet,
    SEClassifierNetwork
)

VALID_MODELS = {
    'deephs_net': ClassifierNetwork,
    'hyve': DeepHSNet_with_HyVEConv,
    'resnet': resnet18,
    'alexnet': AlexNet,
    'spectralnet': SpectralNet,
    'se_resnet': se_resnet18,
    'deephs_net_se': SEClassifierNetwork,
}

CAMERA_AGNOSTIC_MODELS = ('hyve')


def get_model(hparams):
    bands = hparams['bands']

    if hparams['model'] == 'deephs_net':
        model = ClassifierNetwork(bands, num_classes=hparams['num_classes'])
    elif hparams['model'] == 'deephs_net_se':
        model = SEClassifierNetwork(bands, num_classes=hparams['num_classes'])
    elif hparams['model'] == 'resnet':
        model = resnet18(False, bands=bands,
                         num_classes=hparams['num_classes'])
    elif hparams['model'] == 'se_resnet':
        model = se_resnet18(False, bands=bands,
                            num_classes=hparams['num_classes'])
    elif hparams['model'] == 'spectralnet':
        model = SpectralNet(bands=bands,
                            num_classes=hparams['num_classes'])
    elif hparams['model'] == 'alexnet':
        model = AlexNet(bands=bands, num_classes=hparams['num_classes'])
    elif hparams['model'] in CAMERA_AGNOSTIC_MODELS:
        if 'wavelength_range' in hparams:
            wavelength_range = hparams['wavelength_range']
        else:
            wavelengths = hparams['wavelengths']
            wavelength_range = wavelengths[::len(wavelengths) - 1]
        options = {
            'bands': bands,
            'num_classes': hparams['num_classes'],
            'wavelength_range': wavelength_range,
            'num_of_wrois': hparams['camera_agnostic_num_gauss']
        }

        model = VALID_MODELS[hparams['model']](
            **options
        )

    elif hparams['model'] in VALID_MODELS.keys():
        model = VALID_MODELS[hparams['model']](bands)
    else:
        raise Exception(
            f"Model %s is not in known models ({','.join(VALID_MODELS.keys())}" % hparams['model'])

    return model