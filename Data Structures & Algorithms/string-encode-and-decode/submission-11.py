class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        arr = []
        encoded_str = ""
        
        for word in strs:
            encoded_str += str(len(word))
            encoded_str += ","
        encoded_str += "#"

        for word in strs:
            encoded_str+=word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        str_start = 0
        str_length = ""
        len_words = []
        for i, char in enumerate (s):
            if char == "#":
                str_start = i+1
                break
            else:
                str_length+=char
                
        len_words = str_length.split(",")

        len_words.pop(len(len_words)-1)

        list_length = []
        for length in len_words:
            list_length.append(int(length))
        
        words = list(s[str_start:])
        
        strs = []
        temp = ""
        for num in list_length:
            for i in range (num):
                temp += words.pop(0)
            strs.append(temp)
            temp = ""
        return strs