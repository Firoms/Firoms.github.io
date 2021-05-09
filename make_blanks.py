import random


sentences = {1: 'We are often told that there is no innovation without competition, which is absurd given that most of the greatest innovation in science and technology have resulted from the sharing of research across academic silos, national borders, and language barriers. In truth, no great innovations occur in isolation. Personally, I have been asked to sign an awfully large number of nondisclosure agreements from other researchers terrified that their ideas will get out. But in truth, I’ve found this approach counterproductive. Those who hold their cards too close to the vest are rarely the ones who play the winning hand. It is when we share our findings with people with other areas of expertise or perspectives, or seek feedback about our concept from someone in a different field, or try out our idea with potential users, that suddenly the real potential starts to emerge.',
             2: 'The competitive arena is, by its very nature, difficult, unpredictable, and uncontrollable. Despite their best efforts, athletes can never prepare for every eventuality that may occur in competition or control everything that may influence their performances, Routines offer a structure within which to prepare for performance and the flexibility to adjust to the uncertain nature of competition Because routines are not inviolate, but rather provide a guide for athletes to follow, they can also be readily altered to fit the demands of a unique or unexpected competitive environment. Unforeseen changes in the competitive setting, such as weatherm unexpected opponents, late arrival, insufficient warm-up space, and broken or lost equipment, can have a disturbing and disruptive effect on athletes before a competition. Athletes often perform below expectations because they are unable to respond appropriately to these occurrences or become unsettled mentaly. lose motivation or confidence, get distracted, or experience anxiety. Athletes with well-organized yet flexible routines will be better able to respond positively to these challenges, keep calm, and maintain a high level of performance.',
             3: '',
             4: '',
             5: '',
             6: '',
             7: '',
             8: '',
             9: '',
             10: '',
             11: '',
             12: ''}

kor = {1: '우리는 경쟁 없이는 혁신이 없다는 말을 흔히 듣는데, 과학과 기술의 가장 위대한 혁신의 대부분이 (구분되는) 학문 영역, 국경, 언어 장벽을 넘어 연구를 공유하는 것에서 비롯되었다는 점을 고려할 때 그것은 터무니없는 말이다. 사실, 위대한 혁신은 고립된 채로 일어나지 않는다. 개인적으로, 나는 자신들의 아이디어가 알려질 것을 두려워하는 다른 연구자들로부터 끔찍하게 많은 기밀 유지 협약서에 서명하라는 요청을 받은 적이 있었다. 그러나 사실, 나는 이 접근법이 역효과를 낸다는 것을 알게 되었다. 카드를 조끼에 너무 가까이 대고 있는 사람들은 이기는 패를 들고 있는 사람인 경우가 드물다. 갑자기 진정한 잠재력이 나타나기 시작하는 것은, 바로 우리의 연구 결과를 다른 분야의 전문 지식이나 관점을 가진 사람들과 공유하거나, 다른 분야에 있는 누군가로부터 우리의 개념에 관한 피드백을 구하거나, 또는 우리의 아이디어를 잠재적 사용자들과 함께 시도하는 때이다.',
       2: '',
       3: '',
       4: '',
       5: '',
       6: '',
       7: '',
       8: '',
       9: '',
       10: '',
       11: '',
       12: ''}


sentence_num = int(input("지문 번호를 입력하세요 : "))
try:
    sentence = sentences[sentence_num]
    words = sentence.split()
    blank_num = int(input("빈칸 개수를 입력하세요 : "))
    print("")
    ran_words = random.sample(range(0, len(words)), blank_num)
    ran_words.sort()
    answer_li = []
    for i in ran_words:
        answer_li.append(words.pop(i))
        words.insert(i, "(  )")
    print(' '.join(words))
    print(kor[sentence_num])
    print("")

    for i in answer_li:
        enter = input("다음 정답을 입력해주세요 : ")
        if enter == i:
            print("정답입니다")
        else:
            print("오답입니다. 정답은", i)


except:
    print("없는 지문 번호입니다.")
