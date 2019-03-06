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
            print(self.sentence)
            print(list_words)
            print(len(list_words))
            
            # Call to scramble list
            self.scramble_it(list_words)
            # Starts up the scrambler process again
            self.scrambler()
            
        # Exit statement
        print("Good-Bye!")

    def scramble_it(aList):
        while i < len(aList):
            current_word = aList[i]
            # If the word is only three letters, then moves onto next word
            if(current_word <= 3):
                i += 1
            else:
                # Splitting the words into 3 parts
                beginning = current_word[0]
                middle = current_word[1:-1]
                end = current_word[-1]

                j = 0
                
                # Only scrambling the middle letters
                while j <= len(middle):
                    k = j+1
                    middle[j],middle[k] = middle[k],middle[j]
                    j += 2

                # Concatenating back the parts into a single word
                scrambled_word = (beginning
                                  + middle
                                  + end)

                # Putting back the word into the list.
                aList[i] = scrambled_word
                # Iterating the i
                i += 1
        print(final_list = " ".join(aList))

print("Inititalize your key by typing 'your key' = Scrambler().\n" \
      "Then type your 'key'.scrambler() to start!\n" \
      "Then after type 'key'.scramble_it() to start scrambling!\n")
