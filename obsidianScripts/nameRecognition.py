from Levenshtein import distance

def calculate_similarity(arr, string):
    if string == "":
        return []
    string = string.lower()
    # first look for exact matches, do any of the strings in the array match the string exactly?
    def simpleSearch(arr, string):
        if string.lower() in arr:
            return [string]
        # if not, do any of the strings contain the string?
        if any(string in s.lower() for s in arr):
            return [s for s in arr if string in s]
        else:
            return None
    simpleResult = simpleSearch(arr, string)
    if(simpleResult!=None):
        return simpleResult
    
    
    
    # if not, calculate the levenshtein distance between the string and each string in the array
    # if the input string as an i, swap it for an ee and check again
    # if the input string has an ee, swap it for an i and check again
    elif 'i' in string :
        PhoneticString = string.replace('i','ee')

        print("phoneticstring",PhoneticString)
        print(arr)
        simpleResult= simpleSearch(arr, PhoneticString)
        if(simpleResult!=None):
            return simpleResult
    
    # the only way we'd get here is if the other conditions weren't met
    # only check for first names, which means split them by space and only check the first element
    

    threshold = 3
    similar_strings = []
    
    for name in arr:
        name = name.split(" ")[0]
        score = distance(name, string.lower())
        if score <= threshold:
            similar_strings.append([name, score])



    # pick whatever one in the group of similar strings has the lowest levenshtein distance
    if len(similar_strings) > 0:
        min_score = min([x[1] for x in similar_strings])
        similar_strings = [x[0] for x in similar_strings if abs(x[1] - min_score)<2]
        result =  similar_strings
        # check which one has the same first letter
        if len(similar_strings) > 1:
            print("several strings had the same distance")
            print(similar_strings)
            result = [x for x in similar_strings if x[0].lower() == string[0].lower()]
            if(result!=[]):
                if len(result) > 1:
                    print("several strings had the same first letter")
                    resultLower = [x for x in result if x[-1] == string[-1].lower()]
                    if(len(resultLower)==0):
                        return result
                    return result
                else:
                    return result
            else:
                print("no strings had the same first letter")
                # recalculate the similarity if we now remove the first letter, keep doing this until we're empty
                return calculate_similarity(similar_strings,string[1:])
        else:
            return result
    else:
        # throw an error if no similar strings were found, this should never happen
        raise Exception(f"the name {string} was not found in the list of people")
        print("no similar strings were found")

        return []
