#!/usr/bin/python
import sys
import os
import glob
import numpy
import cPickle as pkl

from collections import OrderedDict


dic = {'entailment': '0', 'neutral': '1', 'contradiction': '2'}

def build_dictionary(filepaths, dst_path, lowercase=False):
    word_freqs = OrderedDict()
    for filepath in filepaths:
        print 'Processing', filepath
        with open(filepath, 'r') as f:
            for line in f:
                if lowercase:
                    line = line.lower()
                words_in = line.strip().split(' ')
                for w in words_in:
                    if w not in word_freqs:
                        word_freqs[w] = 0
                    word_freqs[w] += 1

    words = word_freqs.keys()
    freqs = word_freqs.values()

    sorted_idx = numpy.argsort(freqs)
    sorted_words = [words[ii] for ii in sorted_idx[::-1]]

    worddict = OrderedDict()
    worddict['_EOS_'] = 0 # end-of-sentence
    worddict['_OOV_'] = 1 # out-of-vocabulary
    
    for ii, ww in enumerate(sorted_words):
        worddict[ww] = ii + 2

    with open(os.path.join(dst_path, 'vocab_cased.pkl'), 'wb') as f:
        pkl.dump(worddict, f)
    print 'Done'


def make_dirs(dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

if __name__ == '__main__':
    print('=' * 80)
    print('Preprocessing SNLI dataset')
    print('=' * 80)
    base_dir = os.path.dirname(os.path.realpath(__file__))
    dst_dir = os.path.join(base_dir, 'word_sequence')

    build_dictionary([os.path.join(dst_dir, 'premise_snli_1.0_train.txt'), 
        os.path.join(dst_dir, 'hypothesis_snli_1.0_train.txt')], 
        dst_dir)

