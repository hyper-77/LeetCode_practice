

def lengthOfLongestSubstring( s):
    hash={}
    index=0
    score=0
    start=0
    high=0
    for char in s:
        index+=1
        score+=1
        if char in hash:
            preindex=hash[char]
            if start<=preindex:
                score=index-preindex
                start=preindex+1

        hash[char]=index
        high=max(high,score)

    return high




print(lengthOfLongestSubstring("abbbbbn"))