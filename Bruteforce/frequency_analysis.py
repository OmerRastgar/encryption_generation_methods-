from collections import Counter

# Define common English words or frequent letters
common_english_words = ["the", "and", "for", "is", "on", "in", "to", "of", "e"]

def split_into_blocks(ciphertext, block_size):
    """
    Split the ciphertext into blocks of the given block size.
    """
    return [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]

def frequency_analysis(ciphertext, block_size):
    """
    Perform frequency analysis on ECB-encrypted ciphertext by identifying repeating blocks.
    """
    # Split the ciphertext into blocks
    blocks = split_into_blocks(ciphertext, block_size)

    # Count how often each block appears
    block_frequencies = Counter(blocks)

    # Sort blocks by frequency in descending order
    sorted_blocks = block_frequencies.most_common()

    # Output the results with frequency analysis
    print("=== Frequency Analysis ===")
    for block, freq in sorted_blocks:
        print(f"Block: {block.hex()} - Frequency: {freq}")

    return sorted_blocks

def map_to_common_english_words(sorted_blocks, block_size):
    """
    Attempt to map common ciphertext blocks to common English words or letters.
    """
    print("\n=== Possible Mapping to Common English Words/Letters ===")
    
    # A simplified approach to try to map the most frequent blocks
    for i, block in enumerate(sorted_blocks):
        if i < len(common_english_words):
            # Try to map the most frequent ciphertext block to a common word
            possible_word = common_english_words[i]
            print(f"Ciphertext Block {block[0].hex()} could correspond to '{possible_word}'")

# Example usage
if __name__ == "__main__":
    # Sample ciphertext (replace this with actual ECB-encrypted ciphertext)
    ciphertext = bytes.fromhex("8b93c689d9adba9f8b93c689d9adba9f1e7ff8e679b2f8420d2c6f42fd5296c1")

    # Block size for AES is 16 bytes (128 bits)
    block_size = 16

    # Step 1: Perform frequency analysis
    sorted_blocks = frequency_analysis(ciphertext, block_size)

    # Step 2: Map frequent blocks to common English words/letters
    map_to_common_english_words(sorted_blocks, block_size)
