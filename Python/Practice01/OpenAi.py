import openai
import os

# openai.organization = "org-eiKuHnZde6RXyJlkC1vj6fv0"
# openai.api_key = os.getenv("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")
# openai.Model.list()

openai.api_key ='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'

def chat(prompt, model):
    completions = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()


if __name__ == '__main__':
    answer =chat('你好',"davinci")
    print(answer.replace('\n', ''))
