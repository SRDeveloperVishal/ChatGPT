from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv
import openai

load_dotenv()
def chat_room(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print (message,'message')
        response = generate_response(message)
        print (response,'response')
        return JsonResponse({'response': response})
    else:
        return render(request, 'chat/chat.html')

def generate_response(message):
    #def generate_response(message):
    openai.api_key = os.environ.get('API_KEY')

    # Define the prompt for GPT-3
    prompt = f"User: {message}\nAI: "

    # Call the GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=255,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated response from the API response
    generated_text = response.choices[0].text.strip()


    # Return the generated response
    return generated_text
