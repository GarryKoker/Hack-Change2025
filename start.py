from AImodel import predict

while True:
    query = input("Введите текст отзыва: ")
    AIanswer = str(predict(query))
    
    if AIanswer == "[0]":
        result = "Характеристика отзыва: нейтральный\n"

    elif AIanswer == "[1]":
        result = "Характеристика отзыва: позитивный\n"

    else:
        result = "Характеристика отзыва: негативный\n"
        
    print(result)
    
    while True:
        askforcontinue = input("Хотите проанализировать еще отзыв? (да/нет): ")
        if askforcontinue.lower() in ["да", "нет"]:
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

    if askforcontinue.lower() != "да":
        break
    
    print("")
