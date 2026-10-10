lines = 50
topic = "Python"
response_format = "String"

prompt = f"""Please write a {lines} lines about {topic} as the topic,
and please output the response in {response_format} format."""

print(prompt)