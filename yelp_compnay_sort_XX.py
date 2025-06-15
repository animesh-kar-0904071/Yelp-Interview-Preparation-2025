class Solution:

    def sortCompaniesByRank(self, companies, reversed=True) -> None:

        companies = sorted(companies, key= lambda x:x[1], reverse = reversed)
        # key = lambda x:x[1]

        print(companies)
        pass





# Given a company name and rank number, sort the companies by their number.
companies = [('Google', 1), ('Siemens', 10), ('Microsoft', 2) , ('EA', 6)]

sol_obj = Solution()

sol_obj.sortCompaniesByRank(companies)
 

# Given a company name and rank number, sort the companies by their number.