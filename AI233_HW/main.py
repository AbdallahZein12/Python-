
if __name__ == "__main__":

    import re 
    import random

    num_words = 0
    frequencies = []
    bag_of_wrds = {}

    with open('pg71768.txt','r',encoding='utf-8-sig') as f:
        for line in f:
            
            line_words = re.split("[. ,:/!?\"]", line.lower().strip())
            line_words = [i for i in line_words if len(i) > 0]
            line_num_words = len(line_words)
            
            num_words += line_num_words
            
            for word in line_words:
                if word in bag_of_wrds:
                    bag_of_wrds[word] += 1 
                else:
                    bag_of_wrds[word] = 1
                    
    print(f"\nNum of Words: {num_words}\n")
    
    freqWords = sorted(bag_of_wrds.items(), key=lambda x: x[1], reverse=True)

    
    for word, num in freqWords:
        wordFreq = round(num/num_words,4)
        frequencies.append(wordFreq)
        
    top_5_words = freqWords[:5]
    
    top_5_words = list(zip(freqWords[:5],frequencies[:5]))
    
    
    rank = 1
    for i in top_5_words:
        print(f"{rank} - {i[0][0]} - {i[0][1]} - {i[1]}")
        rank +=1
        
    all_wrds = list(bag_of_wrds.keys())
    
    list_of_choices = random.choices(all_wrds,k=50,weights=frequencies)
    
    
    
    print(f"\n\nThe list of 50 random choices based on the word frequencies and their weights\n\n{list_of_choices}\n\n")
    
    
    
    


