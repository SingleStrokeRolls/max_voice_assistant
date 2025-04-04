from volcenginesdkarkruntime import Ark

'''
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)
'''
def single_query_text(client,user_text):
    completion = client.chat.completions.create(
        model="ep-20240828173110-z9ssb",
        messages = [
            {"role":"system","content":"You are a funny home assistant. Answer any question under 50 words. Try to be funny."},
            {"role":"user","content":user_text},
        ],
    )
    #print(completion.choices[0].message.content)
    return completion.choices[0].message.content

#print(completion.choices[0].message.content)
