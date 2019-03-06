class Scrambler:
    """A word scrambler that "scrambles" the letters inside a word
       by switching every two letters. It's not a true scramble
       because I couldn't figure out how to do a random function,
       with what we have learned so far in ZyBooks."""
    
    # Constructor
    def _init_(self):
        self.sentence = ""

    # Scrambler function
    def scrambler(self):
        # Initiates a sentence user input
        self.sentence = input("Type as many sentences as you want to scramble.\n" \
                            "Press Enter to exit.\n")

        while(self.sentence != ""):
            # A new list created by the split() sentence
            list_words = self.sentence.split()
            # Test to see if input was successful
            # Test to see if split was successful
            # Test to see length of word
            #print(self.sentence)
            #print(list_words)
            #print(len(list_words))
            
            # Call to scramble list
            self.scramble_it(list_words)
            # Starts up the scrambler process again
            self.scrambler()
            
        # Exit statement
        print("Good-Bye!")

    def scramble_it(self, aList):
        i = 0
        new_str = ""
        temp_str = ""
        while i < len(aList):
            current_word = aList[i]
            # If the word is only three letters, then moves onto next word
            if(len(current_word) <= 3):
                i += 1
                temp_str += current_word
                # Print statement for testing
                #print("small temp", temp_str)
                temp_str = ""
            else:
                # Splitting the words into 3 parts
                beginning = current_word[0]
                middle = current_word[1:-1]
                end = current_word[-1]

                j = 0
                
                # Only scrambling the middle letters
                #while j + 1 < len(middle):
                k = j + 1
                temp_str += middle[k]
                temp_str += middle[j]
                while(k + 1 < len(middle)):
                    j = k + 1
                    if k < len(middle):
                        temp_str += middle[j]
                        k += 1
                    else:
                        k = len(middle)
                # Print statement for testing
                # print("Temp str: ", temp_str)
                middle = temp_str
                temp_str = ""
                    
                #j += 2

                # Concatenating back the parts into a single word
                scrambled_word = (beginning
                                  + middle
                                  + end)

                # Putting back the word into the list.
                aList[i] = scrambled_word
                # Iterating the i
                i += 1
        print(" ".join(aList))

print("Inititalize your key by typing 'your key' = Scrambler().\n" \
      "Then type your 'key'.scrambler() to start!\n" \
      "Then after type 'key'.scramble_it() to start scrambling!\n")



if __name__ == "__main__":
    s = Scrambler()
    s.scrambler()
