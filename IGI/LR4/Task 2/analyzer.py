import re

def analyze_text(text: str):
    """
    Analyzes the text using regular expressions.
    """
    sentence_count = len(re.findall(r'[.!?]', text))

    narrative_count = len(re.findall(r'[.]\s*', text))
    interrogative_count = len(re.findall(r'[?]\s*', text))
    imperative_count = len(re.findall(r'[!]\s*', text))

    sentence_lengths = [len(sentence) for sentence in re.split(r'[.!?]', text) if sentence.strip()]
    average_sentence_length = sum(sentence_lengths) / len(sentence_lengths)
    
    smileys_count = len(re.findall(r'[:;][-]*[\[\(\]\)]+', text))
    
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    names = []
    for email in emails:
        names.append(email.split('@')[0])
        
    def replace_v(match):
        char = match.group(1)
        return f"v[{char}]"
    
    changed_text = re.sub(r'\$v_\(([A-Za-z0-9])\)\$', replace_v, text)

    vowel_words = len(re.findall(r'\b[aeiouAEIOU][a-zA-Z]+\b', text))
    
    all_characters = re.findall(r'[a-zA-Z]', text)
    
    char_count = {}
    
    for char in all_characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    words_after_comma = re.findall(r',\s*([A-Za-z]+)', text)
    words_after_comma.sort()
    
    return {
        "Changed Text": changed_text,
        "Words after comma": words_after_comma,
        "Repeating Characters" : char_count,
        "Vowel Words": vowel_words,
        "Emails" : emails,
        "Names" : names,
        "Narrative Sentences": narrative_count,
        "Smileys Count": smileys_count,
        "Sentence Count": sentence_count,
        "Interrogative Sentences": interrogative_count,
        "Imperative Sentences": imperative_count,
        "Average Sentence Length": average_sentence_length,
    }
    
