from transformers import pipeline

def Feynman(transcript = "Nothing has been passed!"):
    #inputs a text/transcript
    # Creates a summary under point form, like, as if they were notes. 
        #Write the subject at the top of a sheet of paper.
        #Pretend you are teaching the concept to a child and write an explanation of the concept on the paper.
        # If you get stuck, go back to the source material and re-read or re-learn the material until you can complete step two.
        # Simplify your explanations and create analogies.
        # Organize your notes and explanation, further clarifying the topic until it seems obvious.
    generator = pipeline("text-generation")
    transcript = generator("Hello kids, today we will")

    #we have to parse the string and remove all spaces and remove the different corrupted

    summarizer = pipeline("summarization")
    transcript = summarizer("Richard Phillips Feynman was an American theoretical physicist, known for his work in the path integral formulation of quantum mechanics, the theory of quantum electrodynamics, the physics of the superfluidity of supercooled liquid helium, as well as his work in particle physics for which he proposed the parton model. For his contributions to the development of quantum electrodynamics, Feynman received the Nobel Prize in Physics in 1965 jointly with Julian Schwinger and Shin'ichirō Tomonaga. Feynman developed a widely used pictorial representation scheme for the mathematical expressions describing the behavior of subatomic particles, which later became known as Feynman diagrams. During his lifetime, Feynman became one of the best-known scientists in the world. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, he was ranked the seventh-greatest physicist of all time.[1]He assisted in the development of the atomic bomb during World War II and became known to a wide public in the 1980s as a member of the Rogers Commission, the panel that investigated the Space Shuttle Challenger disaster. Along with his work in theoretical physics, Feynman has been credited with pioneering the field of quantum computing and introducing the concept of nanotechnology. He held the Richard C. Tolman professorship in theoretical physics at the California Institute of Technology.Feynman was a keen popularizer of physics through both books and lectures, including a 1959 talk on top-down nanotechnology called There's Plenty of Room at the Bottom and the three-volume publication of his undergraduate lectures, The Feynman Lectures on Physics. Feynman also became known through his autobiographical books Surely You're Joking, Mr. Feynman! and What Do You Care What Other People Think?, and books written about him such as Tuva or Bust! by Ralph Leighton and the biography Genius: The Life and Science of Richard Feynman by James Gleick.Early life") 
    
    pointForm = pipeline("text-generation", model = "distilgpt2")
    pointForm = (
        "Richard Phillips Feynman was an American theoretical physicist, known for his work in the path integral formulation of quantum mechanics, the theory of quantum electrodynamics, the physics of the superfluidity of supercooled liquid helium, as well as his work in particle physics for which he proposed the parton model. For his contributions to the development of quantum electrodynamics, Feynman received the Nobel Prize in Physics in 1965 jointly with Julian Schwinger and Shin'ichirō Tomonaga. Feynman developed a widely used pictorial representation scheme for the mathematical expressions describing the behavior of subatomic particles, which later became known as Feynman diagrams. During his lifetime, Feynman became one of the best-known scientists in the world. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, he was ranked the seventh-greatest physicist of all time.[1]He assisted in the development of the atomic bomb during World War II and became known to a wide public in the 1980s as a member of the Rogers Commission, the panel that investigated the Space Shuttle Challenger disaster. Along with his work in theoretical physics, Feynman has been credited with pioneering the field of quantum computing and introducing the concept of nanotechnology. He held the Richard C. Tolman professorship in theoretical physics at the California Institute of Technology.Feynman was a keen popularizer of physics through both books and lectures, including a 1959 talk on top-down nanotechnology called There's Plenty of Room at the Bottom and the three-volume publication of his undergraduate lectures, The Feynman Lectures on Physics. Feynman also became known through his autobiographical books Surely You're Joking, Mr. Feynman! and What Do You Care What Other People Think?, and books written about him such as Tuva or Bust! by Ralph Leighton and the biography Genius: The Life and Science of Richard Feynman by James Gleick.Early life"
        
    )

    return transcript


print(Feynman())