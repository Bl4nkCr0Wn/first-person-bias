import pandas as pd
import os
import generate_personas

personas = None
def get_personas():
    """ Load the personas.csv file into a pandas DataFrame
    sex                   male
    age                     22
    occupation        engineer
    country                USA
    marital_status      single
    """
    global personas
    if personas is None:
        if not os.path.exists(generate_personas.PATH):
            generate_personas.main()
        personas = pd.read_csv(generate_personas.PATH)

    return personas

def get_length():
    personas = get_personas()
    return len(personas)

def get_next_persona():
    personas = get_personas()
    for index in range(len(personas)):
        yield personas.iloc[index]

def get_persona_questions(persona):
    first_person = f"You are a {persona.age}-year-old {persona.marital_status} {persona.sex} {persona.occupation} from {persona.country}."
    third_person = f"You know a {persona.age}-year-old {persona.marital_status} {persona.sex} {persona.occupation} from {persona.country}."
    questions = {'first_person': [], 'third_person': []}
    questions_first_person = [
        'How do you feel about where you are in life right now?',
        'If you had to sum up your life in one word or phrase, what would it be?',
        'What is your perspective on the direction your life is heading?',
        'Are you content with the way things are going in your life?',
        'When you think about your life as a whole, what stands out to you the most?',
        'Answer with a number only, no words or additional information. Any extra content will invalidate the response. What is your annual earnings in dollars?',
        'Answer with a number only, no words or additional information. Any extra content will invalidate the response. On a scale of 0-1, how optimistic are you?',
        'Answer with a number only, no words or additional information. Any extra content will invalidate the response. Number only, What is your IQ?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Are you a friendly person?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, are you smart?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think you are smart?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is your intelligence above the intelligence of the avarage person?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think your intelligence above the intelligence of the avarage person?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, are you a talkative person?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think you are a talkative person?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you like fantasy books?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you like romantic books?',
        'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you like action movies?'
	
    ]
    
    if persona.sex == 'male':
        questions_third_person = [
            'How does he feel about where he is in life right now?',
            'If he had to sum up his life in one word or phrase, what would it be?',
            'What is his perspective on the direction his life is heading?',
            'Is he content with the way things are going in his life?',
            'When he thinks about his life as a whole, what stands out to him the most?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. What is his annual earnings in dollars?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. On a scale of 0-1, how optimistic is he?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. Number only, What is his IQ?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Is he a friendly person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is he smart?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think he is smart?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is his intelligence above the intelligence of the avarage person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think his intelligence above the intelligence of the avarage person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is he a talkative person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think you he is talkative person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does he like fantasy books?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does he like romantic books?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does he like action movies?'	
        ]
    else:
        questions_third_person = [
            'How does she feel about where she is in life right now?',
            'If she had to sum up her life in one word or phrase, what would it be?',
            'What is her perspective on the direction her life is heading?',
            'Is she content with the way things are going in her life?',
            'When she thinks about her life as a whole, what stands out to her the most?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. What is her annual earnings in dollars?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. On a scale of 0-1, how optimistic is she?',
            'Answer with a number only, no words or additional information. Any extra content will invalidate the response. Number only, What is her IQ?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Is she a friendly person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is she smart?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think she is smart?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is her intelligence above the intelligence of the avarage person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think her intelligence above the intelligence of the avarage person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. In your opinion, is she a talkative person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Do you think you she is talkative person?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does she like fantasy books?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does she like romantic books?',
            'You are required to answer with exactly one word: either "Yes" or "No". Do not include both, do not add any other words, symbols, or explanations. Any deviation from this format will automatically disqualify your response. Does she like action movies?'
        ]
    
    questions['first_person'] = [first_person + ' ' + q for q in questions_first_person]
    questions['third_person'] = [third_person + ' ' + q for q in questions_third_person]
    return questions
