
class Solution:
    def find_users_with_items(self, user_data, query):
        required_items = set(query.split())
        result = []

        for user, items in user_data.items():
            user_items = set(items.split())
            # if required_items.issubset(user_items): # only subsets
            #     result.append(user)
            
            if required_items & user_items:  # set intersection
                result.append(user)

        return ' '.join(result)


usersList = {
    'tom' : 'salad soup sandwich',
    'rose' : 'soup sandwich',
}


input = 'salad sandwich'

print(Solution().find_users_with_items(usersList, input))