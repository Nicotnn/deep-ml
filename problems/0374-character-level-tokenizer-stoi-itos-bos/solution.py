class CharTokenizer:
    def __init__(self, text: str):
        """
        Build a character-level tokenizer from the input text.
        
        Args:
            text: A string used to build the vocabulary.
        """
        self.vocab = sorted(set(text))
        self.stoi = {"<BOS>": 0, "<EOS>": 1}
        for i, char in enumerate(self.vocab):
            self.stoi[char] = i +2 
        self.itos = {i: char for char, i in self.stoi.items()}
        self.vocab_size = len(self.vocab) + 2

    def encode(self, text: str) -> list:
        """
        Encode a string into a list of token indices.
        
        Args:
            text: The string to encode.
        Returns:
            List of integer indices.
        """
        encoded_chars = [self.stoi["<BOS>"]] + [  self.stoi[char] for char in text] + [self.stoi["<EOS>"]]
        return encoded_chars

    def decode(self, indices: list) -> str:
        """
        Decode a list of token indices back into a string.
        
        Args:
            indices: List of integer indices.
        Returns:
            Decoded string.
        """
        decoded_chars = "".join(self.itos[i] for i in indices)
        return decoded_chars