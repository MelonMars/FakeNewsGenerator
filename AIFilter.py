no = ["Carter:"]

def Filter(article, headline):
    ah = article + headline
    for word in no:
        if word in ah:
            return False
    if len(article) < 100:
        return False
    
    return True