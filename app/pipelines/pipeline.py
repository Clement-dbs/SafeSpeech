from app.models import Models

def main():
    models = Models().models
    print(models)

if __name__ == "__main__":
    main()