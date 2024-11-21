

def matchingStrings(stringList, queries):
    # Write your code here
    hash_table = {}
    for string in stringList:
        if hash_table.get(string):
            hash_table[string] += 1
        else:
            hash_table[string] = 1

    print(hash_table)

    ans = []
    for query in queries:
        if hash_table.get(query):
            ans.append(hash_table[query])
        else:
            ans.append(0)

    return ans

stringList = ['def', 'de', 'fgh']
queries = ['de', 'lmn', 'fgh']
print(matchingStrings(stringList, queries))