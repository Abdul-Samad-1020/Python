import pandas as pd
import os
from langdetect import detect, DetectorFactory

# Ensures language detection is consistent
DetectorFactory.seed = 0

def load_data(file_path):
    """Safely loads the dictionary file."""
    # We use standard text [!] instead of emojis to prevent terminal crashes
    if not os.path.exists(file_path):
        print(f"[!] Error: The file '{file_path}' was not found.")
        print(f"Current Working Directory: {os.getcwd()}") # This helps find where Python is looking
        return set()
    
    try:
        df = pd.read_csv(file_path, header=None)
        # Clean the data
        return set(df[0].dropna().astype(str).str.lower().str.strip())
    except Exception as e:
        print(f"[!] Error loading dictionary: {e}")
        return set()

def check_word(word, dictionary, dict_name="Dictionary"):
    """Check if a word exists in the dictionary."""
    word = word.lower().strip()
    if not word:
        return "No word entered."
    
    if word in dictionary:
        return f"MATCH: Word found in {dict_name}"
    else:
        return f"NO MATCH: Word not in {dict_name}"

def find_words(search_term, dictionary, match_type="exact"):
    """Find words matching a search term.
    
    match_type options:
    - 'exact': exact match
    - 'start': words starting with search term
    - 'contains': words containing search term
    """
    search_term = search_term.lower().strip()
    if not search_term:
        return []
    
    results = []
    for word in dictionary:
        if match_type == "exact" and word == search_term:
            results.append(word)
        elif match_type == "start" and word.startswith(search_term):
            results.append(word)
        elif match_type == "contains" and search_term in word:
            results.append(word)
    
    return sorted(results)

def detect_language(word):
    try:
        return detect(word)
    except:
        return "Unknown"

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("WORD CHECKER - MENU")
    print("=" * 40)
    print("1. Check word (exact match)")
    print("2. Find words (starts with)")
    print("3. Find words (contains)")
    print("4. Check multiple words")
    print("5. Exit")
    print("=" * 40)
    return input("Select option (1-5): ").strip()

# --- EXECUTION ---
FILE_NAMES = {
    "oxford": "Oxford5000.txt",
    "custom": "words.txt"
}

# Load both dictionaries
oxford_words = load_data(FILE_NAMES["oxford"])
custom_words = load_data(FILE_NAMES["custom"])

print("[+] Dictionaries loaded successfully!")
print(f"    Oxford5000: {len(oxford_words)} words")
print(f"    words.txt: {len(custom_words)} words")

if oxford_words or custom_words:
    while True:
        choice = display_menu()
        
        if choice == "1":
            # Check single word
            word_input = input("\nEnter a word: ").strip()
            if word_input:
                print("-" * 40)
                print(f"Oxford5000: {check_word(word_input, oxford_words, 'Oxford5000')}")
                print(f"words.txt:  {check_word(word_input, custom_words, 'words.txt')}")
                print(f"Language:   {detect_language(word_input)}")
                print("-" * 40)
        
        elif choice == "2":
            # Find words starting with
            search_term = input("\nFind words starting with: ").strip()
            if search_term:
                print("-" * 40)
                oxford_results = find_words(search_term, oxford_words, "start")
                custom_results = find_words(search_term, custom_words, "start")
                
                print(f"Oxford5000 ({len(oxford_results)} found):")
                if oxford_results:
                    print(f"  {', '.join(oxford_results[:10])}" + 
                          ("..." if len(oxford_results) > 10 else ""))
                else:
                    print("  No matches")
                
                print(f"\nwords.txt ({len(custom_results)} found):")
                if custom_results:
                    print(f"  {', '.join(custom_results[:10])}" + 
                          ("..." if len(custom_results) > 10 else ""))
                else:
                    print("  No matches")
                print("-" * 40)
        
        elif choice == "3":
            # Find words containing
            search_term = input("\nFind words containing: ").strip()
            if search_term:
                print("-" * 40)
                oxford_results = find_words(search_term, oxford_words, "contains")
                custom_results = find_words(search_term, custom_words, "contains")
                
                print(f"Oxford5000 ({len(oxford_results)} found):")
                if oxford_results:
                    print(f"  {', '.join(oxford_results[:10])}" + 
                          ("..." if len(oxford_results) > 10 else ""))
                else:
                    print("  No matches")
                
                print(f"\nwords.txt ({len(custom_results)} found):")
                if custom_results:
                    print(f"  {', '.join(custom_results[:10])}" + 
                          ("..." if len(custom_results) > 10 else ""))
                else:
                    print("  No matches")
                print("-" * 40)
        
        elif choice == "4":
            # Check multiple words
            words_input = input("\nEnter words (comma-separated): ").strip()
            if words_input:
                words_list = [w.strip() for w in words_input.split(",")]
                print("-" * 40)
                for word in words_list:
                    print(f"\n'{word}':")
                    print(f"  Oxford5000: {check_word(word, oxford_words, 'Oxford5000')}")
                    print(f"  words.txt:  {check_word(word, custom_words, 'words.txt')}")
                print("-" * 40)
        
        elif choice == "5":
            print("\n[+] Goodbye!")
            break
        
        else:
            print("[!] Invalid option. Please select 1-5.")
else:
    print("[!] Program stopped: Dictionaries could not be loaded.")