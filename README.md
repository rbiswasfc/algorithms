# algorithms


# Spark
General purpose in-memory computation engine
Spark can be used with Hadoop, Yarn and other Big Data components to harness the power of spark and improve the performance of your applications

# MT

## SMT
* learn P(y|x) for translating from language x to language y
* min P(y|x) with respect to y -> min P(x|y)*P(y)
* P(x|y) is the translation model, learned from parallel texts
* P(y) is the language model

### Alignment
Alignment is the correspondence between particular words in the translated sentence pairs. This can be complex
* some words have no counterpart
* many to one 
* one to many
* many to many (phrase level translation)

Greedy decoding has no way to undo selected words, not true arg max