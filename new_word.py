class Word:
    def __init__(self,new_word,choice1,choice2,answer):
        self.new_word=new_word
        self.choice1=choice1
        self.choice2=choice2
        self.answer=answer

    def show_question(self):
        print("{}의 뜻은?".format(self.new_word))
        print("1.{}".format(self.choice1))
        print("2.{}".format(self.choice2))

    def check_answer(self,select):
        if select==self.answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")



word=Word("얼죽아","얼어 죽어도 아메리카노","얼굴만은 죽어도 아기피부",1)
word.show_question()
word.check_answer(int(input("=>")))