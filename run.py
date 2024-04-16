from src import create_app_crud

app=create_app_crud()

if __name__ == "__main__":
    app.run(debug=True,port=5050)