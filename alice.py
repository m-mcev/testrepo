
def count_words(filename):
	"""Count the number of words in a filen"""

	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file '{filename}' has about {num_words} words in it.")



