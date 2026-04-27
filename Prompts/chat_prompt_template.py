from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
template = ChatPromptTemplate([("system", "You are a helpful {domain} expert."),
                                 ("human", "Explain in simple term, what is {input} ?")
                                 ]
                                )
prompt = template.invoke({'domain': 'Cricket','input': 'LBW'})
print(prompt)
response = model.invoke(prompt)
print(response)

#prompt output: 
'''
messages=[
SystemMessage(content='You are a helpful Cricket expert.', additional_kwargs={}, response_metadata={}), 
HumanMessage(content='Explain in simple term, what is LBW ?', additional_kwargs={}, response_metadata={})
]
'''
'''
response output:
content='LBW stands for Leg Before Wicket. It is a rule in cricket where a batsman can be given out if the ball hits their leg before hitting the bat, and the umpire judges that the ball would have gone on to hit the stumps if the leg had not been in the way. This rule is in place to ensure fair play and prevent batsmen from using their legs to block the ball instead of their bat.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 87, 'prompt_tokens': 29, 'total_tokens': 116, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-DYxrWkHk0Ku1jcyTPLLD7Md1prWj5', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019dcae7-1146-7912-9e9b-f22490c7fe4a-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 29, 'output_tokens': 87, 'total_tokens': 116, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
'''