from nltk.stem import SnowballStemmer, PorterStemmer

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer('english')


plurals = ['caresses','generously','figuratively', 'adamantly','enourmesly', 'suddenly','logistically']

porter_singles = [porter_stemmer.stem(plural) for plural in plurals]
snowball_singles = [snowball_stemmer.stem(plural) for plural in plurals]


print(f"\nExamples for testing:\n{plurals}\nPorter examples:\n{porter_singles}\nSnowball examples:\n{snowball_singles}")





