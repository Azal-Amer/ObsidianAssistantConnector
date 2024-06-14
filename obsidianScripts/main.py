
import os
import json
from obsidianScripts.nameRecognition import calculate_similarity
from obsidianScripts.inputParser import memory,retrieval

peopleDir = "/Users/amer_/Documents/Obsidian Vault/Personal/People"



# print all the files in the people directory
def main(safemode = True,peopleDir = peopleDir,json_data = {},debug = False,hotword = "memory"):

    attribute_classifier = {
        "Likes and Dislikes":"entry",
        "Important Details":"entry",
        "Gift Ideas":"entry",
        "Birthday":"property",
        "Dietary Restrictions":"property",
        "pronouns":"property",
        "tags":"property",}
    if safemode == True :
        print("safemode is on")
        print("this will not write to the files")
    if debug == True:
        
        print("debug mode is on")
        print(json_data)        



    people = []
    for file in os.listdir(peopleDir):
        people.append(file[:-3])
    name = json_data['person']
    # Perform soft similarity search
    guessed_name = ""

    try:
        # lowercase the array
        peopleLower = [x.lower().split(' ')[0] for x in people]
        guessed_name = (calculate_similarity(peopleLower, json_data["person"].split(' ')[0])[0])
        guessed_name = (people[peopleLower.index(guessed_name)])
        # this then returns the closest first name within our list to the query, allegedly the 
    except Exception as e:
        print(e)
        print("no match found")


    # from here, we want to load the file with the name that was guessed
    personalFileDir = peopleDir + "/" + guessed_name + ".md"
    with open(personalFileDir, 'r') as file:
        personalFile = file.read()
        file.close()


    # there are two ways to treat a given piece of information, we want to classify something as either a property, or an entry
    # a property will be treated by being put in the relevant property section, ex. birthday will be in the property, allergy is a property, etc.
    # an entry will be treated by being put in the relevant entry section



    # first we should split off the properties list, which is the first thing in the file, it will be split from the second ---
    properties,body = personalFile.split("---")[1:3]
    warning = '''
    > [!warning]-
    > ## Important Reminders
    > - **Do Not Tag with Arguments:** Avoid memorializing arguments or conflicts.
    > - **Only Factual Information:** Record only freely given information, no Googling.
    > - **Comfortable Tagging:** Tag people to observe their influence but also remember happy memories.
    > - **Initial Population:** Fill out information for close friends, optionally using contacts.
    > 
    > '''
    body = body.replace(warning,"")
    # print(entries)
    lowercaseItems = ['birthday','dietary destrictions',"likes and dislikes","important details","gift ideas","pronouns","tags"]
    if json_data["location"]['0'] == 'Pronouns':
        json_data["location"]['0'] = 'pronouns'
    elif json_data["location"]['0'].lower() in lowercaseItems:
        if json_data["location"]['0'].title()=="Likes And Dislikes":
            json_data["location"]['0'] = "Likes and Dislikes"
        elif json_data["location"]['0'] == "Pronouns":
            json_data["location"]['0'] = "pronouns"
        elif json_data["location"]['0'] == "Tags":
            json_data["location"]['0'] = "tags"

        elif json_data["location"]['0'] == "Birthday":
            json_data["location"]['0'] = "Birthday"
        else:
            json_data["location"]['0'] = json_data["location"]['0'].title()
    if json_data["type"] == hotword:
        print(guessed_name)
        result = memory(name=guessed_name,body=body,properties = properties,
            personalFile = personalFile,safemode = safemode,json_data = json_data,peopleDir = peopleDir,
            attribute_classifier = attribute_classifier)
    elif json_data["type"] == "retrieval":
        result = json_data["location"]['0']+':'+retrieval(body=body,properties = properties,json_data = json_data,
                attribute_classifier = attribute_classifier)
    return result

# main(attribute_classifier=attribute_classifier,safemode = True,peopleDir = peopleDir,json_data = {})