top_2000 = [ "abc","pqr","def"]
mat = np.zeros((len(top_2000), len(top_2000)))
window_size = 2
CORPUS=["abc def ijk pqr", "pqr klm opq", "lmn pqr xyz abc def pqr abc"]
for top_word_index,top_word in enumerate(top_2000):
    print("top_word  :{}".format(top_word))
    print("top_word_index  :{}".format(top_word_index))
    for sentance in CORPUS:
        print("Entire sentance  :{}".format(sentance))
        if top_word in sentance:
            print("Top word is in sentance........")
            list_sent_words = sentance.split(" ")
            top_word_index_in_sentance = [i for i, x in enumerate(list_sent_words) if x == top_word]
            print("top word indexes in sentance:  {}".format(top_word_index_in_sentance))
            print("entire sentance into list  :{}".format(list_sent_words))
            for num in top_word_index_in_sentance:
                print(num)
                for x in range(window_size):
                    if num-(x+1) >= 0:
                        print("before hand word:  {}".format(list_sent_words[num-(x+1)]))
                        if list_sent_words[num-(x+1)] in top_2000:
                            print("Yep")
                            mat[top_word_index][top_2000.index(list_sent_words[num-(x+1)])] += 1
                            print("index of matched word:  {}".format(top_2000.index(list_sent_words[num-(x+1)])))
                    if num+(x+1) < len(list_sent_words):
                        print("after hand word:   {}".format(list_sent_words[num+(x+1)]))
                        if list_sent_words[num+(x+1)] in top_2000:
                            print("Yep")
                            mat[top_word_index][top_2000.index(list_sent_words[num+(x+1)])] += 1
                            #print("index of matched word:  {}".format(top_2000.index(list_sent_words[num-(x+1)])))
print(mat)