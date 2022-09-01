from multiprocessing.connection import answer_challenge


score=0
print ("A. Sverige\n B.Italy\n C.England")
answer1 = input("Who won the 2006 world cup?")
if answer_challenge == "Italy":
    score+=3

print ("A.88\ B.100\ C.96")
anwser2= input("Hur gammal är englands drottning?")
if  answer_challenge == "96":
    score+=3

print("A.Dance Monkey\n B.Shape of you\n C. Blinding lights")
aswser3 = input ("what is the most streamed song on spotify?")
if answer_challenge == "B":
  score+=5

print("A.Bayern Munich\n B.Liverpool\n C. Ac Milan\n D.Chelsea ")
answer4 = input ("what team has second most champions league titles?")
if answer_challenge == "C":
    score+=5

