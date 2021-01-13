import gspread

def strToNumber(array, type):
    new_array = []
    if type == 'int':
        for i in array:
            new_array.append(int(i))
    elif type == 'float':
        for i in array:
            new_array.append(float(i))
    return new_array

def return_column_data(data, column_number):
    column_data = []
    for i in data:
        column_data.append(i[column_number])

    return column_data


def get_sleep_data(sheet_number):
    gc = gspread.service_account(filename='C:/Users/euanh/Documents/Imperial/Design Engineering/Year 4/IoT and Sensing/Coursework/service_account.json')
    sh = gc.open('Sleep data')

    sheets = sh.worksheets()

    sheet = sheets[sheet_number]
    sheet_data = sheet.get_all_values()
    time = strToNumber(return_column_data(sheet_data, 0), 'int')
    x_accel = strToNumber(return_column_data(sheet_data, 1), 'float')
    y_accel = strToNumber(return_column_data(sheet_data, 2), 'float')
    z_accel = strToNumber(return_column_data(sheet_data, 3), 'float')
    mic1 = strToNumber(return_column_data(sheet_data, 4), 'int')
    mic2 = strToNumber(return_column_data(sheet_data, 5), 'int')
    cancelled_sound = strToNumber(return_column_data(sheet_data, 6), 'int')
    return [time, x_accel, y_accel, z_accel, mic1, mic2, cancelled_sound]

def get_all_sleep_data():
    all_data = []
    gc = gspread.service_account(filename='C:/Users/euanh/Documents/Imperial/Design Engineering/Year 4/IoT and Sensing/Coursework/service_account.json')
    sh = gc.open('Sleep data')
    sheets = sh.worksheets()

    for sheet in sheets:
        sheet_data = sheet.get_all_values()
        time = strToNumber(return_column_data(sheet_data, 0), 'int')
        x_accel = strToNumber(return_column_data(sheet_data, 1), 'float')
        y_accel = strToNumber(return_column_data(sheet_data, 2), 'float')
        z_accel = strToNumber(return_column_data(sheet_data, 3), 'float')
        mic1 = strToNumber(return_column_data(sheet_data, 4), 'int')
        mic2 = strToNumber(return_column_data(sheet_data, 5), 'int')
        cancelled_sound = strToNumber(return_column_data(sheet_data, 6), 'int')
        all_data.append([time, x_accel, y_accel, z_accel, mic1, mic2, cancelled_sound])
    return all_data


def get_news_data():
    gc = gspread.service_account(filename='C:/Users/euanh/Documents/Imperial/Design Engineering/Year 4/IoT and Sensing/Coursework/service_account.json')
    sh = gc.open('News data')

    sheets = sh.worksheets()

    guardian_headlines = []
    bbc_headlines = []
    total_guardian_score = []
    total_bbc_score = []

    for sheet in sheets:
            sheet_data = sheet.get_all_values()
            guardian_headlines.append(return_column_data(sheet_data, 0))
            bbc_headlines.append(return_column_data(sheet_data, 3))

            guardian_sentiment = (return_column_data(sheet_data, 1))
            guardian_scores = (return_column_data(sheet_data, 2))
            guardian_score = 0
            for index in range(len(guardian_scores)):
                if guardian_sentiment[index] == 'Positive':
                    guardian_score += float(guardian_scores[index])
                else:
                    guardian_score -= float(guardian_scores[index])
            total_guardian_score.append(guardian_score)

            bbc_sentiment = (return_column_data(sheet_data, 4))
            bbc_scores = (return_column_data(sheet_data, 5))
            bbc_score = 0
            for index in range(len(bbc_scores)):
                if bbc_sentiment[index] == 'Positive':
                    bbc_score += float(bbc_scores[index])
                else:
                    bbc_score -= float(bbc_scores[index])
            total_bbc_score.append(bbc_score)

    return [guardian_headlines,bbc_headlines,total_guardian_score,total_bbc_score]
