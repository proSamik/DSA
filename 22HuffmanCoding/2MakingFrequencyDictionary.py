class HuffmanCoding:

    def __init__(self, path):
        self.path = path

    def __make_frequency_dict(self,text):
        freq_dict = {}
        for char in text:
            freq_dict[char] = freq_dict.get(char,0) + 1
        
        return freq_dict

    def compress(self):
        #Get file from path
        #To read the text from file
        text = "fasbsajfhbsafjhbashf"

        #Make frequency dictionary using the text
        freq_dict = self.__make_frequency_dict(text)

        #Construct the heap from the frequency_dict

        #Construct the binary tree from the heap

        #Construct the codes from binary tree

        # Creating the encoded text using the codes

        #put this encoded text into the binary file

        #return this binary file as output
        pass