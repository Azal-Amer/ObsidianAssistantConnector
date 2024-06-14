from obsidianScripts.parsingFiles import propertyHandle,entriesHandler

def memory(name = 'guessed_name', body = 'body',properties='properties',personalFile = '',safemode = True,json_data = '',peopleDir = '',attribute_classifier = {}):
    firstLocation = json_data['location']['0']
    print("attribute classifier",attribute_classifier.keys())
    print("first location",firstLocation)

    if(attribute_classifier[firstLocation]=="entry"):
        
        handlerOutput = entriesHandler(body,json_data['location'])
        highlightedSection = handlerOutput['activeBlock']
        requiredHeadings = handlerOutput['headings']
        additionalHeadings = '\n'
        for i in range(len(json_data['location'])):
            if(len(requiredHeadings)>0):
                print(requiredHeadings)
                if str(i) in requiredHeadings[0]:
                    additionalHeadings = "\n"+(int(i)+1)*"#"+" "+json_data['location'][f'{i}']+"\n"
        print(highlightedSection)
        try:
            updatedSection = highlightedSection  +additionalHeadings+ "- "+json_data['item']
        except Exception as e:
            updatedSection = highlightedSection 
        updatedFile = personalFile.replace(highlightedSection, updatedSection)
        # write this to a file
        print('here')
        if(safemode):
            newFileDir = peopleDir + "/" + name + "1"+".md"
        else:
            newFileDir = peopleDir + "/" + name +".md"
        with open(newFileDir, 'w') as file:
            file.write(updatedFile)
            print("file written")
            file.close()
    elif (attribute_classifier[firstLocation]=="property"):
        property = json_data['location']['0']
        handlerOutput = propertyHandle(properties,property )
        print(handlerOutput)
        newAttribute = json_data['item']
        # now we want to check if the handler output has only a single value in it, 
        # as it would make the formatitng different
        firstline = handlerOutput.split("\n")[0].split(f"{json_data['location']['0']}:")
        # this splits the first line to see if there's anything sitting there
        updatedProperties = ""

        # join the array to a string and check if it's empty



        
        if ''.join(firstline)!='':
            
            firstProperty = "\n  - "+firstline[1][1:]
            updatedProperties = f"{json_data['location']['0']}:"+ firstProperty + "\n  - "+newAttribute
        else:
            # print('here'+handlerOutput)
            updatedProperties = handlerOutput + "\n  - "+newAttribute
        updatedFile = personalFile.replace(handlerOutput, updatedProperties)
        if(safemode):
            newFileDir = peopleDir + "/" + name + "1"+".md"
        else:
            newFileDir = peopleDir + "/" + name +".md"
        with open(newFileDir, 'w') as file:
            file.write(updatedFile)
            print("file written")
            file.close()
        return 'Remembered'


def retrieval(body = 'body',properties='properties',json_data = '',attribute_classifier = ''):
    firstLocation = json_data['location']['0']
    if(attribute_classifier[firstLocation]=="entry"):
        
        handlerOutput = entriesHandler(body,json_data['location'])
        relevantSection = handlerOutput["activeBlock"]
        print(handlerOutput["headings"])
        if(len(handlerOutput["headings"])>0):
            result = f"there's no sorted information for this catagory {handlerOutput['headings']}"
            return result
        else:
            return relevantSection
    elif (attribute_classifier[firstLocation]=="property"):
        handlerOutput = propertyHandle(properties,firstLocation)
        # handlerOutput would then get passed through the chatbot
        # print(handlerOutput)
        return handlerOutput
    

