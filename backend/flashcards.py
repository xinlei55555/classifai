#For the flashcards creator, we can use a table question answer model, which takes in a table of questions.abs
    ## not exactly what I want # https://huggingface.co/tasks/table-question-answering

from transformers import pipeline

#first, a model that generates a set of questions to answer
def questionGeneration(transcript = "Nothing has been passed!"):
    #create a 
    pass

#second, a model that asks all the questions and gets the answers.
    #https://huggingface.co/learn/nlp-course/chapter1/3?fw=pt
def questionAnswering():
    question_answer = pipeline("questions-answering")
    answer = questions_answerer(
        question = "What is the number of years the person has worked",
        context = "Richard Phillips Feynman was an American theoretical physicist, known for his work in the path integral formulation of quantum mechanics, the theory of quantum electrodynamics, the physics of the superfluidity of supercooled liquid helium, as well as his work in particle physics for which he proposed the parton model. For his contributions to the development of quantum electrodynamics, Feynman received the Nobel Prize in Physics in 1965 jointly with Julian Schwinger and Shin'ichirō Tomonaga. Feynman developed a widely used pictorial representation scheme for the mathematical expressions describing the behavior of subatomic particles, which later became known as Feynman diagrams. During his lifetime, Feynman became one of the best-known scientists in the world. In a 1999 poll of 130 leading physicists worldwide by the British journal Physics World, he was ranked the seventh-greatest physicist of all time.[1]He assisted in the development of the atomic bomb during World War II and became known to a wide public in the 1980s as a member of the Rogers Commission, the panel that investigated the Space Shuttle Challenger disaster. Along with his work in theoretical physics, Feynman has been credited with pioneering the field of quantum computing and introducing the concept of nanotechnology. He held the Richard C. Tolman professorship in theoretical physics at the California Institute of Technology.Feynman was a keen popularizer of physics through both books and lectures, including a 1959 talk on top-down nanotechnology called There's Plenty of Room at the Bottom and the three-volume publication of his undergraduate lectures, The Feynman Lectures on Physics. Feynman also became known through his autobiographical books Surely You're Joking, Mr. Feynman! and What Do You Care What Other People Think?, and books written about him such as Tuva or Bust! by Ralph Leighton and the biography Genius: The Life and Science of Richard Feynman by James Gleick.Early life"
    )
    return answers

def Flashcards(transcript = "Nothing has been passed!"):
    print(questionAnswering())
    return transcript

Flashcards("HI")