#Getting and setting up the AI
import openai 
openai.api_key = "" #Insert key here
model_engine = "text-davinci-003"

#Grabbing variables
age = input("How old are you?")
gender = input("what is your gender?")
TAW = int(input("How many times a week do you work out?"))
curWeight = int(input("Whats your current weight?"))
lbsGoal = int(input("What is your weight goal?"))

#Prompt for chatGPT
prompt = "I am a " + str(age) + " year old " + str(gender) + ". I weigh " + str(curWeight) + "lbs. I work out " + str(TAW) + " times a week. My weight goal is " + str(lbsGoal) + "lbs. Tell me my daily calorie goal, with a meal plan that outlines my calories and protein. "

#Paramaters for ChatGPT...
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temprature=0.5 
)

aiResponse = completion.choices[0].text
print(aiResponse)