characters_count = {}
paragraph="A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument."
paragraph=paragraph.lower()
for i in paragraph:
	if i not in characters_count:
		characters_count[i]=1
	else:
		characters_count[i]+=1


print(characters_count)