STOPWORDS = {
    "the", "is", "and", "a", "an", "of", "to", "in", "on", "for", "with",
    "as", "by", "at", "from", "this", "that", "it", "was", "were", "be",
    "has", "had", "have", "but", "or", "which"
}


def retrieve_signals(content: str, caption: str, char: str):
    content_words = {
        w for w in content.lower().split()
        if w not in STOPWORDS and len(w) > 2
    }

    caption_words = {
        w for w in caption.lower().split()
        if w not in STOPWORDS and len(w) > 2
    }

    if not content_words:
        overlap_ratio = 0.0
    else:
        overlap_ratio = len(content_words & caption_words) / len(content_words)

    negation_words = {"not", "never", "no", "none"}
    negation_flag = int(any(n in content.lower() for n in negation_words))

    caption_empty = int(len(caption.strip()) == 0)

    return {
        "overlap_ratio": overlap_ratio,
        "negation_flag": negation_flag,
        "caption_empty": caption_empty
    }
