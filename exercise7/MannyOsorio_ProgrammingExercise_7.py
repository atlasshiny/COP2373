import re


def split_into_sentences(paragraph: str) -> list[str]:
	"""
	Splits a paragraph into sentence-like chunks using regex.

	Parameters:
		paragraph (str): The paragraph text to split into sentences.

	Variables:
		parts (list[str]): The regex findall results before trimming.

	Return:
		list[str]: A list of sentence strings (trimmed).
	"""
	paragraph = paragraph.strip()
	if not paragraph:
		return []

	# The positive lookahead `(?=\s+|$)` keeps the punctuation attached to the sentence; `re.DOTALL` allows `.` to match 
	# newlines and `re.MULTILINE` helps handle line boundaries.
	parts = re.findall(
		r".+?(?:[.!?](?=\s+|$)|$)",
		paragraph,
		flags=re.MULTILINE | re.DOTALL,
	)
	return [sentence.strip() for sentence in parts if sentence.strip()]

def display_sentences(sentences: list[str]) -> None:
	"""
	Prints each sentence on its own line and shows the total count.

	Parameters:
		sentences (list[str]): The list of sentences to display.

	Variables:
		None

	Return:
		None
	"""
	print("\nIndividual sentences:")
	for index, sentence in enumerate(sentences, start=1):
		print(f"{index}. {sentence}")

	print(f"\nTotal number of sentences: {len(sentences)}")

def main() -> None:
	"""
	Reads a paragraph from user input, splits into sentences, and displays them.

	Parameters:
		None

	Variables:
		paragraph (str): The user-provided paragraph.
		sentences (list[str]): The list of sentences produced by the splitter.

	Return:
		None
	"""
	paragraph: str = str(input("Enter a paragraph: "))
	sentences: list[str] = list(split_into_sentences(paragraph))
	display_sentences(sentences)

if __name__ == "__main__":
	main()
