import google.generativeai as genai
import PIL.Image ,time ,os
safety_config=[
  {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_NONE"},
  {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_NONE"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_NONE"},
  ]
#{"category": "HARM_CATEGORY_CIVIC_INTEGRITY","threshold": "BLOCK_NONE"}


# example uses:
# download 10 wallpaers on desktop in a new folder using any 3rd party api such as wallhaven
# find all the python codes on the whole pc and cut and paste them in a new folder in downloads also scan for all sub folders
# go wild with your imagination !!




genai.configure(api_key='AIzaSyC6eJncb6a4mF47lUqC94-aYglJv7JVApk') # i know i shouldnt be hardcoding this but this was just experimental project so.
# yes u can use my api key since its free 
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8128,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  safety_settings=safety_config
)
chat = model.start_chat(
  history=[
  ])
previous = " "
what = "no attempts yet."
def  AI(prompt):
  return model.generate_content(prompt).text


while True:
  time.sleep(3)
  if not previous == " ":
    juryp = f'''here : {previous}

An AI is being used to achieve the task of any sort by python code that runs in exec() ,
you have to accurately see ( request by user , code and result output) to see what happen ,
if the code ran perfectly or if it got error , or if it didnt do the thing that it was supposed to ,
write when successful (no errors , task achieved ) 
write when not successful (error , what was the request , what and why it occured & solution to fix it) this includes the gaps in code such as example codes , placeholder api keys , wrong approach etc..
NOTE : DO NOT WRITE ANYTHING EXTRA , KEEP it simple.
if u see NONE  then most likely it suceeded , but still analyse the code for imperfections like placeholders or example code and not the final product
'''
    what = AI(juryp)
    print()
    print(what)
    print()
    time.sleep(3)

  x = input('enter your request')
  prompt = f'''you have to write a clean code to 100% achieve this task given and
u have to make sure that the given task is finished with the code u write
make sure not to write unnecessary comments and make sure u dont leave any placeholders
write all the information as if the code is a final product and leave no gaps or example placeholders.
such as passwords , directories , api keys , etc..., you are allowed to use 3rd party api and libraries !
if u do need to leave gaps such as a exmaple placeholder such as directory then do it on desktop "C:\\Users\\asus\\Desktop
and for api keys if not already provided by user, do not use a method which asks for api key rather use a non api key library
feel free to import modules to ur code but make sure that u install them before using subprocess
NOTE : dont write a code that gets stuck in endless loop of retrying wrong method

requested by user / user's message : {x}

previous attempt / requests : -
{what}
'''
  response = chat.send_message(prompt)
  print(response.text)
  ask = int(input("wanna run?"))
  if ask  == 1:
        try:
             result = exec(str(response.text).replace("`", "").replace("python", ""))
             print()
             print(result)
             print()
             previous = f"previously asked by user : {x} ,  code given by ai to do the task  : {response.text} , output of code / error : {result}"
             print(previous)
        except:
            pass
  else:
            pass 



