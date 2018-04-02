from utils import skipgram
import pandas as pd
import click
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

VECTORDIMENSIONS = ['d_{}'.format(d + 1) for d in range(300)]

@click.command()
@click.option('--vec', '-v', default='wiki.en.vec')
@click.option('--conllu', '-c', default='English.conllu')
@click.option('--language', '-l', default='English')
@click.option('--cache/--no-cache', default=True)
def run(vec, conllu, language, cache):

	# read the conllu parse into a df, rename vars, & lose duplicates
	logging.info("Pre-processing > reading conllu data from: {}".format(conllu)) 
	df = pd.read_csv(conllu, header = None, comment = "#", sep = '\t', encoding = 'utf-8', error_bad_lines = False)
	df = df.rename(columns = {1: 'form', 2: 'lemma'})
	df = df.drop_duplicates(subset = ['form', 'lemma'])

	# obtain semantic model
	logging.info("Pre-processing > obtaining semantic model from: {}".format(vec)) 
	model = skipgram.Skipgram(vec)

	def getvecs(row):
		# subtract lemma vector from form vector to obtain difference vector
		diffvec = [None] * 300 if not ((row.form in model) & (row.lemma in model)) else model[row.form] - model[row.lemma]
		return pd.Series(diffvec, index = VECTORDIMENSIONS)

	# combine recources: loop over the conllu data, extract difference vectors
	logging.info("Compute > obtaining difference-set vectors")
	differenceset = df.apply(getvecs, axis = 1)
	df = pd.concat([df, differenceset], axis = 1).dropna(subset = VECTORDIMENSIONS)

	# save out the difference vectors
	if cache:
		logging.info("Cache > saving vectors to {}".format('{}.diffset'.format(language)))
		df.to_csv('{}.diffset'.format(language))

	logging.info("Results > saving coplexity statistics to: {}.morphosemantics".format(language))
	results = pd.DataFrame(dict(language = [language]), index = [0])
	results['Semantic Distance (All Tokens)'] = df[VECTORDIMENSIONS].pow(2).sum(axis = 1).mean()
	results['Semantic Distance (Non-identical Tokens)'] = df[df.form != df.lemma][VECTORDIMENSIONS].pow(2).sum(axis = 1).mean()
	results['Semantic Variance (All Tokens)'] = df[VECTORDIMENSIONS].var(axis = 0).sum()
	results['Semantic Variance (Non-identical Tokens)'] = df[df.form != df.lemma][VECTORDIMENSIONS].var(axis = 0).sum()
	results.to_csv('{}.morphosemantics'.format(language), index = False)

if __name__ == '__main__':
    run()