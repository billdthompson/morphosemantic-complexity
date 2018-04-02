import pandas as pd
import click
import os

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

DATADIR = '../Data/'

@click.command()
def run():
	
	for uddir in os.listdir(DATADIR):
		language = uddir.split('_')[1]

		logging.info("Atempting lemmatization of: {}".format(language))

		conllu = DATADIR + uddir + '/{}.conllu'.format(language)

		if not os.path.exists(conllu):
			logging.info("Failed: {}".format(conllu))
			continue

		parsed = pd.read_csv(conllu, sep = '\t', header = None, comment = '#', encoding = 'utf-8', error_bad_lines = False, quoting = 3)

		# parsed[2] = lemmas
		lemmatised = ' '.join(parsed[2].astype(str).values)

		plain = ' '.join(parsed[1].astype(str).values)

		with open('{}_lemmatized.txt'.format(language), 'w') as f:
			f.write(lemmatised)
		
		with open('{}_plain.txt'.format(language), 'w') as f:
			f.write(plain)

		logging.info("finished {}".format(language))

if __name__ == '__main__':
    run()