from google import genai

client = genai.Client(api_key="AIzaSyCahKQxh47Mdt8VO2cHSt2Hl8nCFoPowZA")

for model in client.models.list():
    print(model.name)