import numpy
import os

from nli import train

def main(job_id, params):
    print params
    validerr = train(saveto=params['model'][0],
                    reload_=params['reload'][0],
                    dim_word=params['dim_word'][0],
                    dim=params['dim'][0],
                    patience=params['patience'][0],
                    n_words=params['n-words'][0],
                    decay_c=params['decay-c'][0],
                    clip_c=params['clip-c'][0],
                    lrate=params['learning-rate'][0],
                    optimizer=params['optimizer'][0], 
                    maxlen=100,
                    batch_size=32,
                    valid_batch_size=128,
                    datasets=['../../data/word_sequence/premise_snli_1.0_train.txt', 
                    '../../data/word_sequence/hypothesis_snli_1.0_train.txt',
                    '../../data/word_sequence/label_snli_1.0_train.txt'],
                    valid_datasets=['../../data/word_sequence/premise_snli_1.0_dev.txt', 
                    '../../data/word_sequence/hypothesis_snli_1.0_dev.txt',
                    '../../data/word_sequence/label_snli_1.0_dev.txt'],
                    test_datasets=['../../data/word_sequence/premise_snli_1.0_test.txt', 
                    '../../data/word_sequence/hypothesis_snli_1.0_test.txt',
                    '../../data/word_sequence/label_snli_1.0_test.txt'],
                    dictionary='../../data/word_sequence/vocab_cased.pkl', 
                    validFreq=int(549367/32+1),
                    dispFreq=1000,
                    saveFreq=int(549367/32+1),
                    use_dropout=params['use-dropout'][0],
                    verbose=False,
                    # embedding='../../data/glove.840B.300d.txt'%os.environ['USER']
                    )
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['./baseline.npz'],
        'dim_word': [300],
        'dim': [300],
        'n-words': [30000], 
        'patience': [1],
        'optimizer': ['adam'],
        'decay-c': [0.], 
        'clip-c': [10.], 
        'use-dropout': [True],
        'learning-rate': [0.0004],
        'reload': [False],
        })


