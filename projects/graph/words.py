from graph import Graph
import sys

#define words
start_word = 'hit'
end_word = 'cog'

#helpers to filter out words we dont care about (limits our loops and decreases run time)
first = [start_word[0], end_word[0]]
last = [start_word[-1], end_word[-1]]
length = len(start_word)

#grabs words from our word file.
f = open("words.txt", 'r')
all_words_length = [word for word in f.read().splitlines()
                    if len(word) == length and word.islower()]
f.close()

#instantiates the graph and generates a certex for each valid word
gr = Graph()
for word in all_words_length:
    if word[0] in first and word[-1] in last:
        gr.add_vertex(word)

# compare current vertex against rest of vertices to find word one letter different from end_word
for v1 in gr.vertices: #for each word/vertex
    for v2 in gr.vertices: #loop through all words/vertices
        oneOff = 0 #to track number of differences
        #check each letter againt corresponding letter
        for i in range(0, len(v1)): 
            if v1[i] == v2[i]:
                oneOff += 1 #if the letter in word 1 matches the same-index-letter in word 2 add to count
        if oneOff == len(v1) - 1: #if all but one letter match 
            gr.add_edge(v1, v2)#add as an edge.

print(gr.bfs(start_word, end_word))