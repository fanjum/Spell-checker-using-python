from textblob import TextBlob
x="hiy"
print("Input text: "+x)
y=TextBlob(x)
print("Correct Text: "+str(y.correct()))