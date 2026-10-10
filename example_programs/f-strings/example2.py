prompt = """Please write a {} lines about {} as the topic,
and please output the response in {} format."""

lines = 50
topic = "Python"
response_format = "String"

print(prompt.format(lines, topic, response_format))

students = ["abhinav","aman","rahul","yash"]

details = {
    "abhinav": {
        "rollno": 1,
        "subject": "python"
    },
    "aman": {
        "rollno": 2,
        "subject": "java"
    }
}