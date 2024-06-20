---
tags:
  - googleAssistant
  - LLM
  - obsidianWorkflow
  - webHook
  - ngrok
Status: Completed
---

# Overview
The goal of the project, is that I can interface with my notes through the google assistant. More specifically, the below

| ![[../../Supplemental Files/images/Google Assistant Obsidian Connector 2024-06-01 14.00.05.excalidraw]] |
| ------------------------------------------------------------------------------------------------------- |
| Fig 0.1: Diagram of the ideal workflow                                                                  |
## Example
> "Hey Google, **in my notes**, remember that *Abeera likes swiss cheese*". 

GA recognizes it needs to send this down the pipeline, through the API, which **decides** if this is a retrieval or memory situation. (Either keyword or use the local LLM). If memory, we use an LLM to process the direct text prompt, into a JSON, with the structure
```
{
type:"memory",
person:"Abeera",
location:{
	0: "Likes and Dislikes",
	1: "Likes",
	2: "Food"
	}
item: "Swiss Cheese"
}
```
Then this JSON is read by a python script, which will then edit the markdown file to add this. 


## Reflection
- I enjoyed working on this project, because I learned how simple it was to setup a webhook for future projects using Flask. Chaining LLM's together was interesting, and made me appreciate Langchain more.
# Project overview
3 parts, google assistant end, receiving and sending from server, and processing.
Let's start with processing, and make sure what we want to do is possible. 

## Google Assistant
- this might be a major pain in the ass, can we use sms instead and have assistant just read messages
- https://youtu.be/ZrkAWSemDC8
## Receiving and Sending
- SMS?
## Processing

### JSON Format
```
{
type:"memory" or "retrival",
file:"filename",
location:{
	0: "heading1",
	1: "heading 2",
	2: "heading 3"
	}
item: "object to add"
}
```

To make JSON standardization easier, we should **identify all the headings and subheadings we've used thus far**, so that there is something to reference off of
#### Interpreter and Connector

> [!Todo] Todo for the connector
> - [x] If a subheading doesn't exist for a given file, automatically create it
> - [x] add support for retrieving and adding properties

Thus far, the connector can read a JSON, and then run down the file to add the item as the last bullet in the given section. **It does not generate a new section when asked.** We also don't have support for properties.
#### Interpersonal Template JSON Structure
 ```
 [
  {
  
    "heading": "Likes and Dislikes",
    "children": [
      {
        "heading": "Likes",
        "items": [],
        "children": [
          {
            "heading": "Media",
            "items": []
          },
          {
            "heading": "Music",
            "items": []
          },
          {
            "heading": "Food",
            "items": []
          },
          {
            "heading": "Smells",
            "items": []
          }
        ]
      },
      {
        "heading": "Dislikes",
        "items": [],
        "children": [
          {
            "heading": "Media",
            "items": []
          },
          {
            "heading": "Music",
            "items": []
          },
          {
            "heading": "Food",
            "items": []
          },
          {
            "heading": "Smells",
            "items": []
          }
        ]
      }
    ]
  },
  {
    "heading": "Important Details",
    "children": [
      {
        "heading": "Relationship",
        "items": []
      },
      {
        "heading": "Memorable Conversations",
        "items": []
      }
    ]
  },
  {
    "heading": "Gift Ideas",
    "items": []
  }
]
``` 
### Command analysis

> [!Warning] Computational Power constraint
> We're running this on potentially a raspberry pi, so we need to keep the processing light.

- [x] Generate example prompt inputs and outputs, then we can use those to check if what our system does, works.
- The goal would be harvesting relevant data from the prompt, with the following structure


3 parts to this, identifying the filename, identifying what object to add, and identifying where to place the object in the file.

If you cannot identify category, default to a null location.

Using GPT3.5, with a system prompt, the code is sometimes running into an issue of whether something is retrieval or memory.

Right now, the retrieval will return what was asked, while the memory will just say "store"


> [!Todo] What's next
> Wrap GPT into a function, then call that through telegram.
> Build up the below format, which involves 3 total API calls
> 
>| ![[../../Supplemental Files/images/Google Assistant Obsidian Connector 2024-06-13 00.09.59.excalidraw]] |
| ------------------------------------------------------------------------------------------------------- |
>Right now we've written out the behavior of sister, so we should make the whole GPT pipeline first

#### Context (?)
- Maybe give the bot access to context about the weather and date

#### Memory
An example prompts for **memory** would be:
> "Hey Google, **in my notes**, remember that *Abeera likes swiss cheese*". 
>  "Hey Google, **in my notes**, remember that *Mama doesn't like carrots*". 
>  "Hey Google, **in my notes**, an important detail about Harshini is that she is  roommates with Ananya". 

#### Retrieval
An example prompt for retrieval would be:
> "Hey Google, **in my notes**,does *Abeera likes swiss cheese*?". 



For retrieval, we might need an LLM, as this becomes more complicated. 

My thoughts for version 1, is that we use GPT3 for the memory writing and processing.  We can hotswap it for something more private later.
For retrieval, we'd need to ask it twice, first is where in the heading we expect the information to be, and second is what the information is. Two API calls.

The API would return the JSON output with the memory or retrieval task. Then that's fed into a python script, which is hardcoded to add these pieces of information.




# Future Features
- Implement Access to Langchain
- Use DSPY to improve prompting