# GIVEN CODE HAS OFFENSIVE PROFANITY FOR USAGE WITHIN MODERATION SYSTEM. YOU HAVE BEEN WARNED.
#NSFW! DO NOT OPEN IN PUBLIC WORKPLACE

def check_profanity(message):
    banned_words = [
    # Hardcore (NSFW/offensive)
    "fuck", "fucker", "fucking", "motherfucker",
    "cunt", "dick", "cock", "slut", "whore",
    "nigger", "nigga", "faggot",

    # Mild (common rude words)
    "shit", "bullshit", "bitch", "ass", "asshole",
    "bastard", "damn", "piss", "twat", "wank",
    "crap", "dildo", "tit", "tits", "prick","stfu","gandu","bkl","ban"
    # Hindi Cuss words
    
    "bhosdi", "bhosdike", "chutiya", "chutiye", "madarchod", "behenchod",
    "lund", "gaand", "haraami", "kutte", "kutti", "raand", "randi",
    "lavde", "lavda", "chodu", "chodna", "chod", "suar", 
    "jhant", "jhantichod", "chutiya", "maa ke", "behen ke", 
    "maa ka", "behan ka", "choddo", "chodti", "chodunga", "chudwa", 
    "chudne", "chudane", "gaandmasti", "lundbaaz", "bhen ke", "madar ke","bsdk","niamos"
    

                    ]
    message = message.lower() #for not making my life a hellhole


    for word in banned_words:
        if word in message:
            return True
        
    return False

