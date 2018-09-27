import random

# 問題のデータキーが当道府県、値が県庁所在地
capitals = {'北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市', '宮城県': '仙台市', '秋田県': '秋田市', '山形県': '山形市'
            , '福島県': '福島市', '茨城県': '水戸市', '栃木県': '宇都宮市', '群馬県': '前橋市', '埼玉県': 'さいたま市', '東京都': '東京', }

# 35個の問題集を作成する
for quiz_num in range(35):
    # 問題集と回答集のファイルを作る
    quiz_file = open('capitalsquiz{}.txt'.format(quiz_num + 1), 'w')
    answer_key_file = open('capitalsquiz{}.txt'.format(quiz_num + 1), 'w')

    # 問題集のヘッダーを書く
    quiz_file.write('名前：\n\n日付：\n\n学期：\n\n')
    quiz_file.write((' ' * 20) + '都道府県クイズ（問題番号{}）'.format(quiz_num + 1))
    quiz_file.write('\n\n')

    # 都道府県の順番をシャッフルする
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)

    # 47都道府県をループしてそれぞれ問題を作る
    for question_num in range(len(prefectures)):
        # 正解と誤答を取得する
        correct_answer = capitals[prefectures[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # 問題ファイルと回答選択肢をファイルに書く
        quiz_file.write('{}. {}の県庁所在地は？\n'.format(question_num + 1, prefectures[question_num]))
        for i in range(4):
            quiz_file.write('{}. {}\n'.format('ABCD'[i], answer_options[i]))

        quiz_file.write('\n')

        # 答えの選択肢をファイルに書く
        answer_key_file.write('{}.{}\n'.format(question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_key_file.close()
