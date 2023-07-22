from transformers import pipeline
#inputs a text/transcript
    # Creates a summary under point form, like, as if they were notes. 
        #Write the subject at the top of a sheet of paper.
        #Pretend you are teaching the concept to a child and write an explanation of the concept on the paper.
        # If you get stuck, go back to the source material and re-read or re-learn the material until you can complete step two.
        # Simplify your explanations and create analogies.
        # Organize your notes and explanation, further clarifying the topic until it seems obvious.
    
    #https://huggingface.co/learn/nlp-course/chapter1/3?fw=pt
    
#separates the paragraph into sentences.
def sentences(transcript):
    return transcript.split('.')

def remove_bad_characters(transcript):
    return transcript.strip("\\\{\}\:\(\)\'\'\"\"")

#summarize the transcript repetitively to get the subject.
def summary(transcript, n, summarizer):
    print(transcript)
    if(n==1):
        return transcript
    else:
        #summarizer returns a list of dictionaries.
        transcript = summarizer(transcript)[0]["summary_text"] 
        return summary(transcript, n-1, summarizer)
    
def Feynman(transcript = "Nothing has been passed!"):
    #we have to parse the string and remove all spaces and remove the different corrupted characters
    transcript = remove_bad_characters(transcript)

    #generate a title for the notes:
    subjectFinder =  pipeline("question-answering")
    summarizer=pipeline("summarization")
    #the number of summarizations depends on the length of the script, and is recursively summarized
    subject = subjectFinder(question="Who or what is the main subject of this paragraph?", context=summary(transcript, len(transcript)//500, summarizer))['answer']

    #returns a summarized vesrion of each paragraph, by summarizing each sentence
    point_form=[]
    summarizer = pipeline("summarization")
    paragraph = sentences(transcript)
    summarized=""
    for sentence in paragraph:
        summarized+= sentence
        #summarize three sentences at a time? Or a specific character count at a time? 
        if len(summarized>700): 
            point_form.append(summarizer(summarized)[0]["summary_text"])
            summarized=""
    
    notes = {"subject": subject, "point_form":point_form}
    return notes

transcript = "Richard Phillips Feynman was an American theoretical physicist, known for his work in the path integral formulation of quantum mechanics, the theory of quantum electrodynamics, the physics of the superfluidity of supercooled liquid helium, as well as his work in particle physics for which he proposed the parton model. For his contributions to the development of quantum electrodynamics, Feynman received the Nobel Prize in Physics in 1965 jointly with Julian Schwinger and Shin'ichirō Tomonaga. Feynman developed a widely used pictorial representation scheme for the mathematical expressions describing the behavior of subatomic particles, which later became known as Feynman diagrams. During his lifetime, Feynman became one of the best-known scientists in the world. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, he was ranked the seventh-greatest physicist of all time.[1]He assisted in the development of the atomic bomb during World War II and became known to a wide public in the 1980s as a member of the Rogers Commission, the panel that investigated the Space Shuttle Challenger disaster. Along with his work in theoretical physics, Feynman has been credited with pioneering the field of quantum computing and introducing the concept of nanotechnology. He held the Richard C. Tolman professorship in theoretical physics at the California Institute of Technology.Feynman was a keen popularizer of physics through both books and lectures, including a 1959 talk on top-down nanotechnology called There's Plenty of Room at the Bottom and the three-volume publication of his undergraduate lectures, The Feynman Lectures on Physics. Feynman also became known through his autobiographical books Surely You're Joking, Mr. Feynman! and What Do You Care What Other People Think?, and books written about him such as Tuva or Bust! by Ralph Leighton and the biography Genius: The Life and Science of Richard Feynman by James Gleick.Early life"
print(Feynman(transcript))
# print(sentences(transcript))
# print(remove_bad_characters(transcript))


# pointForm = pipeline("text-generation", model = "distilgpt2")
    # pointForm = (
    # )
    # generator = pipeline("text-generation")
    # transcript = generator("Hello kids, today we will")