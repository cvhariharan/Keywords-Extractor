import re
def normalize(text):
    text = re.sub("[^A-Za-z0-9_]", " ", text)
    text = re.sub(" +"," ",text)
    text = text.lower()
    return text

def extract_words(text):
    words = []
    words = re.split(" +",text)
    if "" in words:
        words.remove("")
    return words

def extract_keywords(text):
    text = normalize(text)
    print(text)
    keywords = []
    sentences = []
    stopwordsList = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
    regexSeq = " |\\b".join(stopwordsList)

    regexSeq = "\\b"+regexSeq
    sentences = text.split(".")
    for sentence in sentences:
        temp = re.split(regexSeq,sentence)
        temp = [x.strip() for x in temp if x != ' ' and x != ''] #Removes empty strings
        keywords.append(temp)
        superList = []
    for l in keywords:
        superList = superList + l
    #print(regexSeq)
    return superList
    #return stopwordsList

text = "Samsung Electronics Co Ltd said on Wednesday it has developed the world's smallest DRAM chip, widening its technical lead on competitors as it tracks towards a record operating profit in 2017 driven by the semiconductor business.The 'second-generation' 10-nanometre class, 8-gigabit DRAM chips with improved energy efficiency and data processing performance would be geared toward premium data-crunching electronics such as cloud computing centres, mobile devices and high-speed graphic cards, Samsung said in a statement.The global leader in computer chips, televisions and smartphones said it would shift most of its existing DRAM production capacity to 10-nano chips in 2018.This \"aggressive\" production expansion would \"accommodate strong market demand,\" said Gyoyoung Jin, president of Memory Business at Samsung Electronics.With the appointment of a new generation of top managers in its three main businesses including semiconductors in late October, the South Korean company said it was not looking to expand chip shipments immediately but was investing to maintain longer-term market position."
print(extract_keywords(text))
"""print(normalize(text))
print(extract_words(text))"""
