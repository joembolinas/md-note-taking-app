from textblob import TextBlob
from app.models.schemas import GrammarMatch

def check_grammar(text: str) -> list[GrammarMatch]:
    """
    Check grammar/spelling using TextBlob.
    Note: TextBlob is primarily a simplified NLP library. 
    For robust grammar checking, LanguageTool is preferred but requires Java.
    This implementation uses TextBlob's correction capabilities to simulate suggestions.
    """
    blob = TextBlob(text)
    matches = []
    
    # TextBlob doesn't give offsets easily for grammar, mostly spelling.
    # We will simulate the "match" structure by iterating sentences/words.
    # This is a simplified MVP implementation.
    
    # Simple Spelling Check approach
    for i, word in enumerate(blob.words):
        corrected = word.correct()
        if word != corrected:
            # Approximate offset finding (very naive, assumes first occurrence)
            # In a real app, we'd track precise offsets.
            start_index = text.find(word) 
            if start_index != -1:
                matches.append(
                    GrammarMatch(
                        message=f"Possible spelling error: '{word}'",
                        offset=start_index,
                        length=len(word),
                        replacements=[str(corrected)]
                    )
                )
    
    return matches
