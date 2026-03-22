import re

# Split a paragraph into sentence-like chunks.
def split_into_sentences(paragraph: str) -> list[str]:
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

# Display each sentence and the total count.
def display_sentences(sentences: list[str]) -> None:
	print("\nIndividual sentences:")
	for index, sentence in enumerate(sentences, start=1):
		print(f"{index}. {sentence}")

	print(f"\nTotal number of sentences: {len(sentences)}")

# Read input text, split it, and print results.
def main() -> None:
	paragraph: str = str(input("Enter a paragraph: "))
	sentences: list[str] = list(split_into_sentences(paragraph))
	display_sentences(sentences)

if __name__ == "__main__":
	main()
