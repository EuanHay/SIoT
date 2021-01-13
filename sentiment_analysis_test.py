import gspread
from sentiment_analysis import test_model
from monkeylearn import MonkeyLearn
import pandas as pd

def collect_comparison():
    gc = gspread.service_account(filename='C:/Users/euanh/Documents/Imperial/Design Engineering/Year 4/IoT and Sensing/Coursework/service_account.json')
    sh = gc.open('News data')

    sheets = sh.worksheets()
    headlines = []
    for sheet in sheets:
        guardian_headlines = sheet.col_values(1)
        bbc_headlines = sheet.col_values(4)
        daily_headlines = guardian_headlines + bbc_headlines
        headlines += daily_headlines
    print(headlines)

    ml = MonkeyLearn('aeb287eb770f34e274240336aeb4b7cf9a9c89b5')
    response = ml.classifiers.classify(
        model_id='cl_Jx8qzYJh',
        data=headlines
    )

    sentiment_analyser = []
    for headline in headlines:
        sentiment_analyser.append(test_model(headline))
    print(sentiment_analyser)


    monkeylearn_analyser = []
    for i in range(len(headlines)):
        monkeylearn_analyser.append([response.body[i]['classifications'][0]['tag_name'],
                                    response.body[i]['classifications'][0]['confidence']])



    sh2 = gc.open('Sentiment Comparison')
    comparison_sheet = sh2.sheet1
    comparison_sheet.update('A1', sentiment_analyser)
    comparison_sheet.update('D1', monkeylearn_analyser)

def compare_sentiment():
    gc = gspread.service_account(
        filename='C:/Users/euanh/Documents/Imperial/Design Engineering/Year 4/IoT and Sensing/Coursework/service_account.json')
    sh = gc.open('Sentiment Comparison')

    sheet = sh.sheet1
    data = sheet.get_all_values()
    filtered_data = []
    for i in data:
        if i[3] != 'Neutral':
            filtered_data.append(i)

    print(filtered_data)

    sentiment_analyser_array = [0,0]
    sentiment_analyser_score = 0
    monkeylearn_score = 0
    for i in filtered_data:
        if i[1] == 'Negative':
            sentiment_analyser_score += float(i[2])
            sentiment_analyser_array[0] += 1
            if i[3] == 'Negative':
                sentiment_analyser_array[0] +=1
                monkeylearn_score += float(i[4])
            elif i[3] == 'Positive':
                sentiment_analyser_array[1] += 1
                monkeylearn_score -= float(i[4])
        elif i[1] == 'Positive':
            sentiment_analyser_score -= float(i[2])
            if i[3] == 'Positive':
                sentiment_analyser_array[0] += 1
                monkeylearn_score -= float(i[4])
            elif i[3] == 'Negative':
                sentiment_analyser_array[1] += 1
                monkeylearn_score += float(i[4])


    print(sentiment_analyser_array)
    print(sentiment_analyser_score)
    print(monkeylearn_score)
    print((sentiment_analyser_array[0]/(sentiment_analyser_array[0] + sentiment_analyser_array[1]))*100)



compare_sentiment()