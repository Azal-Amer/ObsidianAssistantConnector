def propertyHandle(properties,property):
    # first we need to isolate the property section
    # this can be done by just finding the line the property comes up on, up till the line with the next heading
    
    linesAfter = properties.split(property)[1]
    attributesInProperty = property
    for i,line in enumerate(linesAfter.split("\n")):
        # print("line",line)
        if i == 0:
            attributesInProperty+=(line)
        elif "-" in line:
            attributesInProperty+=("\n"+line)
        else:
            break
    
    return attributesInProperty
    

# the below function splits up the body of the note into blocks of increasing resolution, to find the block that contains the information we're looking for
def entriesHandler(body,locations):
    
    activeBlock = body
    for i in locations:
        # split the file by the number of hashtags
        hashtags = "\n"+(int(i)+1)*"#"+" "
        activeBlock = activeBlock.split(hashtags)
        

        missingHeadings = []
        # the above variable contains the level and name of a missing heading, so that it can be added back later
        if(len(activeBlock)==1):
            print(f"the level {locations[i]} was not found in the file")
            missingHeadings.append(i)
        if(hashtags + locations[i] not in body):
            missingHeadings.append(i)
        # we want to be able to check if a certain level of the hierarchy is or isnt defined, so if 

        # find which block starts with the name of the location in the first line
        for block in activeBlock:
           
            if(int(i)>0):
                oldTitleCondition = locations[str(int(i)-1)] not in block.split("\n")[0]
            else:
                oldTitleCondition = True
            # this checks if the new block has accidentally held the title of the parent block, True if it hasn't, False if it does
            # Ex: the subheading name "Likes" is in the Heading "Likes and Dislikes", so we need to make sure we select blocks that dont have the parent

            if locations[i] in block.split("\n")[0] and oldTitleCondition:
                activeBlock = block
                break
        if type(activeBlock) == list:
            activeBlock = activeBlock[0]
        
        
    # if the type is an array, get the zeroth index


    return {"activeBlock":activeBlock,"headings":missingHeadings}
        
