import spacy
nlp = spacy.load('en_core_web_md')

# Example code
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# This makes sense in the way that cat and money had the highest score as both are animals.
# The second highest score was monkey and banana which is very ofter associated for monkeys eat banana.
# The lowest score was cat and banana which actually doesn't seem to have any relevant connection.

# Personal exmaple
word1 = nlp("fish")
word2 = nlp("ball")
word3 = nlp("cat")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# This was interesting because as expected cat and fish had the highest score but the second was fish and ball intead of cat and ball.
# I would expect cat and ball be more similiar as cats usually play with balls and I cannot see a closer relation to fish and ball.

  
# Other example code
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))




sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",  similarity)
    
# In this example the highest score is between the one to compare and "Hello, there is my car", 
# although the "I\'ve lost my car in my car" also refers to a car it also has the element key whcih might lower the score.
# After that one we can see both dog relate sentences with  "where did my dog go" scoring higher 
# than "I will name my dog Diana" most likely due to the fact that it is also a question.  
# Lastly we see the "I\'d like my boat back" which is clearly the one less similar to the one to compare"
    
	
# With sm it was a bit of a surprise as it stated that both cat and fish and cat and monkey had the lowest score from each examples being that those are both animals.
