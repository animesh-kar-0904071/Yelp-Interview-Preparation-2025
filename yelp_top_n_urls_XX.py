from collections import defaultdict


class Solution:

    def getTopN(self, urls: list[str], n: int) -> {}:

        freqCount = defaultdict(int)

        # for i in range(len(urls)):
        #     freqCount[urls[i]] +=1 

        for url in urls:
            freqCount[url] +=1     
        
       
        sorted_urls = sorted(freqCount.items(), key = lambda x:x[1], reverse= False)
        print(sorted_urls)

    





urls = [
    "google.com", "youtube.com", "google.com", "facebook.com",
    "google.com", "youtube.com", "facebook.com", "instagram.com",
    "twitter.com", "linkedin.com", "youtube.com", "google.com",
    "stackoverflow.com", "github.com", "github.com", "github.com"
]
n = 5

sol_ins = Solution()

sol_ins.getTopN(urls, n)