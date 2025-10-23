

def main():

    sentence = "I like to learn python in northeastern"

    new_sentence = sentence.split(" ")
    print(new_sentence)

    #joined 
    join_sentence = "-" .join(new_sentence)
    print(join_sentence)



    for i in range(0, 10 ):
        print(i, end =' ')
    print("\n")
    
    name = "Anton"
    for i in range(len(name)):
        print(f"index {i}", name[i])

    
    







if __name__ =='__main__':
    main()