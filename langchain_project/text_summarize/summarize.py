from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

speech = '''
Listen to me carefully.

There will be days when you feel tired. There will be moments when you question yourself. You will look at other people and wonder why they are moving ahead while you are still struggling.

You will work hard and sometimes see no results. You will give your best and still face rejection. And there will be nights when you lie awake, thinking about your future, your responsibilities, and your dreams.

But let me tell you something.

**Your current situation is not your final destination.**

Just because life is difficult today doesn't mean it will always be difficult. Just because you failed yesterday doesn't mean you cannot succeed tomorrow.

Every successful person you admire has faced moments when giving up seemed easier than continuing. The difference is not that they never felt afraid. The difference is that they kept moving forward despite their fear.

Remember, a seed must stay buried in darkness before it can grow into a tree.

Maybe right now, you are in that dark phase of your life. Maybe nobody sees your hard work. Maybe nobody appreciates your sacrifices.

But don't stop growing just because nobody is watching.

**Work in silence. Improve yourself every day. Let your results speak for you.**

You don't need to become successful overnight. You don't need to prove yourself to the entire world today.

You just need to be a little better than you were yesterday.

Learn something new. Take one more step. Try one more time. Get back up after every fall.

And most importantly, stop comparing your journey with someone else's.

Their chapter ten might be your chapter two. You don't know what they have sacrificed, and they don't know what you are fighting through.

So focus on your own journey.

One day, the struggles that make you cry today might become the stories that inspire someone else tomorrow.

One day, the sacrifices you are making today might give your family the life you've always dreamed of.

But that day will never come if you give up on yourself now.

So lift your head. Take a deep breath. Forget about how many times you have failed.

**You are still here. You still have time. And you still have a chance to change your life.**

Don't wait for motivation every morning. Build discipline. Don't wait for the perfect opportunity. Start with what you have.

Because your future is not built by what you wish for. It is built by what you do consistently.

And whenever life gets hard, remember these words:

*You may be tired, but keep going.*

*You may be afraid, but take the step.*

*You may have failed, but try again.*

Because the moment you stop believing in yourself is the moment you stop giving yourself a chance.

Your story isn't over.

Now go out there, work hard, believe in yourself, and create a life that your future self will be proud of.

**Your time will come. But until it does, keep working. Keep learning. Keep fighting. Never give up on yourself.**
'''

# chat_msg = [
#     SystemMessage(content='You are an expert with expertise in summarizing text'),
#     HumanMessage(content=f'Please provide the short and concise summary for the provided text: {speech}')
# ]

# response = model.invoke(chat_msg)

# print(response.content)

from langchain_core.prompts import PromptTemplate

generic_prompt = '''Summarize the following text: {text} to be concise
in this language: {language}
'''

prompt = PromptTemplate(template=generic_prompt, input_variables=['text', 'language'])

final_prompt = prompt.format(text=speech, language='hindi')

# print(model.get_num_tokens(final_prompt))

chain = prompt | model

response = chain.invoke({'text': speech, 'language': 'french'})

print(response)