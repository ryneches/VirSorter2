#!/usr/bin/env python

import sys
import os
import pandas as pd


def main():
    '''Merge classification of trimmed seqs from different viral groups

    Example:
        python merge-clf-trim-from-groups.py <outfile> <A.clf> <B.clf> ..

        <outfile>: merged classifcation results showing probability of being
            viral with different classifers
        <A.clf> ..: list of classifications results from viral groups

    '''
    if len(sys.argv) < 3:
        mes = '*** Usage: python {} <outfile> <A.clf> <B.clf> ..\n'
        sys.stderr.write(mes.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    outfile = sys.argv[1]
    clf_lis = sys.argv[2:]
    cnt = 0
    for clf in clf_lis:
        df = pd.read_csv(clf, sep='\t', header=0)
        if cnt == 0:
            merged = df
        else:
            #merged = pd.merge(prev, df, on='seqname', how='inner')
            merged = pd.merge(prev, df, on='seqname', how='outer')

        prev = merged
        cnt += 1

    merged.to_csv(outfile, sep='\t', na_rep='NaN',
            index=False, float_format='%.3f')

if __name__ == '__main__':
    main()
