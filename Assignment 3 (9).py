class flashcard:
    def __init__(r,word,mean):
        r.word=word
        r.mean=mean
    def __str__(r):
        
        return (r.word+":"+r.mean)
word=input("Enter a word")
mean=input("Enter its meaning")
t=flashcard(word,mean)
print(t.__str__())
