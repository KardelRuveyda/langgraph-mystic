from dotenv import load_dotenv
load_dotenv()

from graph.graph import app

# get_response fonksiyonunu tanımlıyoruz
def get_response(user_query):
    input_data = {"question": user_query}  # input_data is a dictionary
    return app.invoke(input=input_data)  # Sends the data as required

#if __name__ == "__main__":
#    print("Hello Advanced RAG")
#    print(get_response({"question": "rüyada fırtına görmek?"}))
