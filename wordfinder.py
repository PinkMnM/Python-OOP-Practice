from random import choice


class WordFinder:
    """Accepts a file and creates a wordlist of each line within the file."""

    def __init__(self, file_path):
        """Initialize the WordFinder Class."""
        self.file_path = file_path
        self.word_list = self.get_words()
        self.word_list_len = len(self.word_list)
        self.print_word_count()

    def print_word_count(self):
        """Print the number of words read."""
        print(f"{self.word_list_len} words read")

    def get_words(self):
        """Return the list of lines extracted from the file specified in the file_path argument."""
        try:
            with open(self.file_path) as file:
                words = [line.rstrip() for line in file]
            return words
        except (FileNotFoundError, IOError) as exc:
            raise FileNotFoundError(f"Error reading file: {exc}")

    def random(self):
        """Extract a random word from the word_list."""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Version of WordFinder that ignores blank lines and lines starting with #."""

    def __init__(self, file_path):
        """Initialize SpecialWordFinder Class via WordFinder."""
        super().__init__(file_path)

    def get_words(self):
        """Return a list of words. Blank lines and lines starting with # are ignored."""
        try:
            with open(self.file_path) as file:
                words = [line.rstrip() for line in file]
                valid_words = [
                    word for word in words if word and not word.startswith("#")
                ]
            return valid_words
        except (FileNotFoundError, IOError) as exc:
            raise FileNotFoundError(f"Error reading file: {exc}")
