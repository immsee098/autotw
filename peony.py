# -*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import tweepy
import time
import random
from datetime import datetime
import math
print('this is my twitter bot')


CONSUMER_KEY = '9rK8XwuJFDTLgYUgyIpR1DXix'
CONSUMER_SECRET = 'rDqNgWXftmzGGuw2Nxc5bLbsSPDuvJARax0cUUPy460ZOv0Lkb'
ACCESS_KEY = '956896188808101888-ZLl0VMNm8rKuIV6uENJsflsc24d8FGF'
ACCESS_SECRET = 'oegz4sXyk3iLNRseVL1c832UPdoYkG0X9L4vsWT8ns6nb'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

mentions = api.mentions_timeline()

FILE_NAME = 'arcana_1_bot.txt'

FLOWER_FILE = ''

def find_flower_exp(flower_file_name):
    #FLOWER_FILE = 'student_otoha.txt' #stu_name #'student_otoha.txt'
    flower_read = open(flower_file_name, 'r')
    last_seen_exp = int(flower_read.read().strip())
    flower_read.close()
    return last_seen_exp #finding flower exp and returning it

def save_flower_exp(last_found_exp, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_found_exp))
    f_write.close()
    return

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def flower_app_show(otoha_num, user_id, user_name, now, mention_id):
    flower_sel = ['튤립', '붓꽃', '메리골드', '제라늄', '세인트폴리아','천일홍', '물망초', '칼랑코에']
    if(otoha_num > 0 and otoha_num<=19):
        api.update_status('@' + user_id + ' ' + user_name + "는/은…\n[씨앗]을 무럭무럭 키웠다. 언제쯤 싹이 날까?\n현재 성장도는...["+str(otoha_num)+"]입니다."+ now, mention_id)
    elif(otoha_num > 19 and otoha_num<50):
        api.update_status('@' + user_id + ' ' + user_name + '는/은…\n' + '[떡잎]을 무럭무럭 키웠다. 귀여워!\n현재 성장도는...['+str(otoha_num)+']입니다.'+ now, mention_id)
    elif(otoha_num > 49 and otoha_num<=70):
        api.update_status('@' + user_id + ' ' + user_name + "는/은…\n[더 자란 싹]을 무럭무럭 키웠다. 얼른 자랐으면 좋겠다!\n현재 성장도는...["+str(otoha_num)+"]입니다."+ now, mention_id)
    elif(otoha_num > 69 and otoha_num<=99):
        api.update_status('@' + user_id + ' ' + user_name + "는/은…\n[쑥쑥 자라는 줄기]를 무럭무럭 키웠다. 얼른 꽃이 폈음 좋겠다!\n현재 성장도는...["+str(otoha_num)+"]입니다."+ now, mention_id)
    elif(otoha_num > 99 and otoha_num<=111):
        api.update_status('@' + user_id + ' ' + user_name + "는/은…\n[꽃눈이 달린 식물]을 무럭무럭 키웠다. 조금 더 하면 봉오리가 되겠지?\n현재 성장도는...["+str(otoha_num)+"]입니다."+ now, mention_id)
    elif(otoha_num > 111 and otoha_num<=124):
        api.update_status('@' + user_id + ' ' + user_name + "는/은…\n[봉오리가 맺힌 식물]을 무럭무럭 키웠다. 곧 꽃이 피지 않을까?\n현재 성장도는...["+str(otoha_num)+"]입니다."+ now, mention_id)
    elif(otoha_num > 124 and otoha_num<=140):
        api.update_status('@' + user_id + ' ' + user_name + "는/은 무럭무럭 키워서…\n드디어 꽃이 피었다! 이건 유이 선생님이 좋아하는 ["+random.choice(flower_sel)+"]이잖아?"+ now, mention_id)
    else:
        print("nothing here!")
        return



def reply_to_tweets():
    abc = ['a', 'b', 'c', 'd', 'e', 'f']
    oddeven = ['의 결과는… 홀!', '의 결과는… 짝!']
    #freeTweets = ['(은)는 엄청나게 실패했다! 어디서 부서지는 소리 나지 않았어?', '(은)는 실패했다. 안타깝게도…', '(은)는 기분 좋게 성공했다!', '(은)는 완벽하게 성공했다! 대단한 걸']
    rosipa = ['의 선택은…… 가위!', '의 선택은…… 바위!', '의 선택은…… 보!']
    hh = datetime.now().hour
    mm = datetime.now().minute
    ss = datetime.now().second
    now = ('%s:%s:%s' % ( hh, mm, ss) )

    print('retrieving and replying to tweets...')
    # DEV NOTE: Testing the lastest mention
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'd100' in mention.full_text.lower():
            print('found d100')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,101)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd50' in mention.full_text.lower():
            print('found d50')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,51)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd20' in mention.full_text.lower():
            print('found d20')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,21)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd10' in mention.full_text.lower():
            print('found d10')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,11)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif 'd6' in mention.full_text.lower():
            print('found d6')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '의 숫자는…\n…\n' + ' ' +  '<' + str(random.randrange(1,7)) + '> !!' +' '+ '\n' + str(now), mention.id)

        elif '운세' in mention.full_text.lower():
            print('found 운세')
            print('responding back...')
            luckyday =['광대\n자유의 바람이 부는걸요? 밖으로 나가 새로운 시도를 해보는 것도 좋을 것 같네요. 희망을 가지고 도전해보기로 해요!',
            '마법사\n당신의 숨겨진 잠재력을 마음껏 뽐내 볼 수 있을지도? 하지만 일이 술술 잘 풀릴 때야말로 자만하지 않도록 주의!',
            '여사제\n외로운 기분이 들지도 모릅니다. 아무도 모르게 속에 품고 있는 비밀이 있나요? 친구들과 상의해보는 것도 좋을 것 같네요.',
            '여제\n풍요로운 하루가 될 것 같네요! 물질적으로도 정신적으로도 만족스러울 것 같아요. 인간관계에 너그러운 마음을 가집시다.',
            '황제\n혹시 너무 목적이나 목표에 열중하지 않았나요? 원하는 바를 얻기 위한 고난과 역경이 당신을 기다리고 있네요. 스트레스를 조심하세요!',
            '교황\n사람을 통해 한 층 더 성장할 수 있을지도? 좋은 인연이 기다리고 있을지도, 또는 당신이 누군가의 좋은 인연이 될지도 모릅니다. 주변인을 아껴줍시다!',
            '연인\n애정운 최고조! 두근거리는 설레임이 찾아올지도 모르겠네요. 또는 누군가와 아주 깊은 감정적 교류를 나누게 될지도 몰라요.',
            '전차\n굉장히 도전적인 하루가 되겠네요. 승리의 여신이 당신을 향하고 있답니다. 당신이 꿈꾸던 것을 이룰지도 몰라요. 용기를 가지고 부딪혀 봅시다!',
            '힘\n다른 누구와도 아닌 당신 자신과의 싸움입니다. 포기하지 말고 자신의 신념과 지혜를 믿도록 하세요.',
            '은둔자\n혼자 있고 싶어질지도 몰라요. 홀로 틀여박혀 자신을 성찰하고 반성하게 될지도. 하지만 언제나 곁에 있는 친구의 존재를 잊지 말도록 해요.',
            '운명의 수레바퀴\n새로운 전환점이 당신을 기다리고 있네요. 뜻밖의 행운이 찾아올지도? 오롯이 변화를 받아들이는 생물만이 살아남을 수 있다는 것을 명심!',
            '정의\n결단을 내려야하는 날인 것 같네요. 여지껏 질질 끌고 있는 일이 있다면, 오늘이야말로 결판을 짓는 게 어떨까요? 행동없이 결과는 오지 않는 법이랍니다.',
            '매달린 자\n당신에게 시련이 찾아올지도 몰라요. 섣불리 움직일 수 없기 때문에 큰 인내심이 필요할 것 같네요. 고된 인내 끝에 달콤한 보상이 있으리!',
            '죽음\n당신 앞으로 무언가를 끝장내줄 사신이 찾아올지도? 너무 나쁘게 생각하지 말아요. 안 좋은 상황을 끝내고 새롭게 시작할 수도 있으니까요.',
            '절제\n선택을 하는 것보단 양쪽 모두를 생각하고 중립적인 자세를 취하는 게 어떨까요? 중요한 것은 균형입니다. 선을 넘지 말도록 해요.',
            '악마\n충동적인 하루가 될지도 몰라요. 많이 불안해질지도 모르지요. 최대한 이성을 지키고, 현명하게 처우합시다!',
            '탑\n당신의 잘못으로 끔찍한 결과가 나올지도 몰라요. 갑작스러운 비극은 당신을 포함한 주변인들까지 덮칠지도 모른답니다. 신중해져보도록 해요!',
            '별\n희망차고 황홀한 하루가 될지도 몰라요. 긍정적이고 꿈을 꿔보는 것도 좋지만... 과하면 좋지 않겠죠? 현실을 직시하는 것이 중요해요.',
            '달\n아주 혼란스러운 하루가 될지도 몰라요. 상황이 좋지 못해 갈등이 생기고 우울함을 느끼게 될지도. 오늘은 중요한 결정은 안 하는 걸 추천!',
            '태양\n아주 긍정적인 하루가 될 것 같네요! 목표를 달성하게 될지도 몰라요. 열정을 가지고 행동해보도록 해요.',
            '심판\n당신이 기다리고 있던 소식이 들려올지도 몰라요! 흐림 뒤 맑음, 지금까지의 노력을 보상받게 될 거랍니다.',
            '세계\n모든 것이 조화로울 것 같네요. 일은 큰 성취를 이룰 것이고, 인간관계에선 더 끈끈한 유대감이 생길지도 몰라요. 큰 도전을 해보는 건 어떨까요?']
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name +'의 카드는... '+random.choice(luckyday)+ '!\n' + str(now), mention.id)

        elif '홀짝' in mention.full_text.lower():
                print('found 홀짝')
                print('responding back...')
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + str(random.choice(oddeven))+' '+ '\n' + str(now), mention.id)

        elif '가위바위보' in mention.full_text.lower():
                print('found 가위바위보')
                print('responding back...')
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + str(random.choice(rosipa))+' '+ '\n' + str(now), mention.id)

        elif 'yn' in mention.full_text.lower():
                print('found YN')
                print('responding back...')
                yesno = ['yes!', 'no....', 'y', 'n']
                api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name + '은...  ' + str(random.choice(yesno))+'...! '+ '\n' + str(now), mention.id)


        elif '중국어' in mention.full_text.lower():
            print('found 중국어')
            print('responding back...')
            luckyday =[   '한문엔 "성조"라는 것이 존재합니다.  1성은 아→, 2성은 아↗, 3성은 아↘↗, 4성은 아 ↘. 마지막으로 "경성"이란 것이 있는데 이는 앞 성조에 따라 유동적으로 변합니다. 가볍고 짧게 발음해보세요.     ',
             ' 중국어는 기본적으로 [주어 + (부사)+ 술어 + 보어/목적어]으로 만들어집니다. 예를 들어 "我喜欢你(Wǒ xǐ huān nǐ)" 나는 너를 좋아해는, [나我(주어) + 좋다喜欢(동사) + 너你(목적어)]로 구성되어 있습니다. ',
             ' 병음을 알아야 글자를 읽을 수 있습니다. a(아), e(으어), o(오어), u(우) 등이 있고, zh(쯔), ch(츠), sh(쓰) 등이 있으며, -eng(엉), -ing(잉), ang(앙), -ong(옹) 등이 있습니다. 그 외 ü 이것은 u에서 i를 더한 "위" 발음이 됩니다. ',
             ' “日出江花红胜火rì chū jiāng huā hóng shèng huǒ，春来江水绿如蓝chūn lái jiāng shuǐ lǜ rú lán”.  "해 뜰 때 강가의 꽃이 불보다 더 붉고, 봄이 온 강물은 남초보다 푸르다."라는 뜻입니다. 읽어 봅시다! ',
             ' 한자의 편방 부수에는 의미가 있다는 걸 아시나요? 글자의 뜻을 몰라도 형태로 얼추 의미를 유추할 수 있습니다. 예를 들어, 氵는 물과 관련된 글자 앞에 붙고는 합니다. 游yóu -헤엄치다처럼요. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)


        elif '국어' in mention.full_text.lower():
            print('found 국어')
            print('responding back...')
            luckyday =['이때 화자의 마음은 사랑하는 이를 그리워하는 마음이라고 해석하면 됩니다.. 그 구절을 다시 확인해볼까요?',
            '어제 읽었던 다음 페이지를 먼저 누가 읽어보도록 할까. 음....'+mention.user.name+'가 일어나서 낭독해보도록 하죠.',
            '오늘의 수업은 본인이 직접 시나 소설을 적어보는 것으로 할까 해요. 간단한 단편도 좋답니다. 그럼 시작해볼까요?'						]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '수학' in mention.full_text.lower():
            print('found 수학')
            print('responding back...')
            luckyday =['어떤 수 A를 제곱하여 X가 되었을 때에... 예를 들어 A^2=X 일 때, A를 X의 제곱 근이라고 말한단다.',
            '(칠판에 문제를 적어내리면서) 저번에 배운 걸 응용한 문제에요. 이번 문제는'+mention.user.name +'가/이 나와서 풀어볼까요.',
            '소인수분해는 자연수를 소인수의 곱으로 나타낸 것을 의미한단다. 여기서 소인수는 자연수 중에 "소수"인 것을 뜻하는데, 이것은 숫자에 1과 그 수 자신만을 약수로 가지는 것이지.',
            '정수는 쉽게 말하자면 0과 음수, 양수를 포함하는 단어란다. 자연수라고 생각하면 되지. 하지만, 이 자연수에 포함되지 않은 숫자들을 부르는 것을 "정수가 아닌 유리수"라고 부른단다. 우리들이 흔히 알고 있는 분수로 표현하는 것, 생각하면 쉬울 거야.',
            '두 자연수의 최대공약수와 최소공배수의 곱은 그 두 자연수의 곱과 같단다. 자연수 A, B가 있고 최대공약수 G와 최소공배수 L이 있을 때에, AxB와 GxL의 값은 똑같게 나온단다.'						]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '사회지리' in mention.full_text.lower():
            print('found 사회지리')
            print('responding back...')
            luckyday =[ ' 다들 지구가 원형이란 건 알고 있지? 지구의 중심을 통과해 지구의 자전축과 수직을 이루는 선을 "적도"라고 불러. 적도는 위도의 기준이 되어, 정의상 위도는 0°인 셈이지. ',
             ' 지구의 기후를 평균 기온과 강수량을 참고해 몇 종류로 구분할 수 있지. 크게 열대 기후, 건조 기후, 온대 기후, 냉대 기후, 한대 기후 5가지로 나누어져 있어. 그리고 일본은 온대 기후에 속해 있어. 시험에 나오니 기억하도록 해! ',
             ' 현대인의 기원에 대해 유력한 가설은 2개가 있어. 하나는 아프리카에서 최초로 나타나 퍼졌다는 설이 있고, 또 하나는 다른 지구의 고대 인류가 각각 섞이고 진화했다는 다지구기원설이야. 뭐, 어느 쪽이 맞는지는 아무도 몰라. ',
             ' 인간과 원을 어떻게 구분할까? 첫째, 직립보행을 할 수 있는가. 이는 사람과의 표식이지. 그리고 둘째, 도구를 만들 수 있는가. 이는 사람 속의 표식이야. '	]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '과학' in mention.full_text.lower():
            print('found 산수')
            print('responding back...')
            luckyday =[  ' 행성에는 소행성대보다 안쪽에 있는 수성, 금성, 지구, 화성과 바깥쪽에 있는 목성, 토성, 천왕성, 해왕성이 있다. 이들은 각각 지구형 행성과 목성형 행성으로 부른다. ',
             ' 알칼리금속이나 알칼리토금속의 성분을 포함하는 물질을 겉불꽃에 넣으면 특유의 불꽃색이 나타나며, 이를 불꽃반응이라 부른다. 이 작용은 불꽃놀이에도 활용되어 있단다. 나중에 구해와서 다 같이 해보도록 할까. ',
             ' 지구계의 구성을 정리하자면 [지권, 수권, 기권, 생물권, 외권]으로 정리한단다. 지(地), 수(水), 기(氣), 생물은 여러분들도 짐작이 가능하겠죠? 그럼 마지막에 말하는 외권은 무엇을 말하는 것인지 발표해볼 사람 있나요? ',
             ' 지권 암석은 크게 "화성암"과 "퇴적암", "변성암"으로 나뉩니다. 화성암은 마그마나 용암이 식어 만들어졌고, 퇴적암은 무언가가 부서지고 녹여진 것이죠. 변성암은 지하에서 높은 열과 압력을 받아 성질이나 조직이 변한 것입니다. ',
             ' 파동이 진행하다가 장애물을 만나 방향이 바뀌어 되돌아 나오는 현상을 "반사"라고 한단다. 빛이 반사하는 것과 똑같이 파동도 "반사 법칙"이 성립하지. ... 반사 법칙은 기억하나? 반사 법칙에 대해서 설명해볼 사람?  '	]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '음악' in mention.full_text.lower():
            print('found 음악')
            print('responding back...')
            luckyday =[  ' 음악은 소리를 통해 인간의 감정과 사상을 표현하는 예술이에요. 언어가 통하지 않아도, 전 세계와 교감을 할 수 있는 소통의 매체이죠. 여러분들이 음악을 배우며, 활용하고, 삶의 희로애락을 경험하길 바라요. ',
             ' 생활 속에서 음악은 쉽게 접할 수 있답니다. 예를 들어, 결혼식, 행사 등에도 상황에 맞는 노래를 틀어 분위기를 더욱 즐겁게 만들어주는 경우가 있죠. 생활 외에도 무언가의 의식에도 사용되어 분위기를 만들어주기도 한답니다.  ',
             ' 크로스오버, 어떠한 장르에 다른 장르의 요소가 합해져서 만들어진 음악을 뜻합니다. 퓨전음악이라고도 하죠. 원래는 어떤 곡이 몇 종류의 차트에 동시에 등장하는 현상을 의미하지만, 퓨전 재즈 등의 음악 장르에서부터 널리 쓰이게 되었답니다. ',
             ' 작곡가 모차르트는 자신의 천재성을 바탕으로 우아산 가락과 맑은 화성, 구조적인 아름다움을 잘 갖춘 작품을 남겼죠. 오스트리아 출신이지만 독일, 프랑스, 영국, 이탈리아에 다녀 다양한 소재의 음악을 만들기로 했어요. "작은 별"도 그분의 작품이지요. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '도덕' in mention.full_text.lower():
            print('found 영어')
            print('responding back...')
            luckyday =[ ' 도덕적 상상력은 "도덕적 관점"으로 파악하여 바람직하게 해결하는 방법이며, 민감성은 "사람들의 입장"을 고려하여 올바른 결과를 얻기 위해 노력하는 성향입니다. 두 가지를 종합하면, 바람직한 방향과 해결책을 찾을 수 있지요. ',
             ' 사람의 "선천성"중에서도 가장 두드러지는 주제는 "성선설"과 "성악설"입니다. 각각 맹자와 순자가 주장하는 의견이지요. 물론, 그 뒤를 잇는 타불라 라사의 "백지론"도 같이 거론되고 있답니다. 여러분들은 무엇이라고 생각하시나요? ',
             ' 일한 만큼 정당한 대가를 받지 못하거나 빈곤 상태에서 벗어나지 못하는 것은 경제 및 사회 정의의 훼손과 관련된 도덕 문제로 거론되기도 합니다. 여러분들은 자신의 대가를 정당하게 받아 일하도록 하세요. 그게 자신의 가치를 지키는 일이랍니다. ',
             ' 지구 문제를 해결하기 위해서 세계 시민으로서 도덕적 책임을 다하려는 자세를 갖추어야 해요. 이는 상호 이해와 관용을 실천함으로써 공동체의 평화를 실현하기 위한 노력이기도 하답니다. 먼저 가까운 곳을 챙겨보도록 해요. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '보건체육' in mention.full_text.lower():
            print('found 보건체육')
            print('responding back...')
            luckyday =[  ' 뜨거운 날씨에 체육을 할 때에는 조심해야 한다. 더위만으로도 쉽게 일사병이 걸릴 수 있고, 그 뒤로 더 심해지면 열사병, 열피로, 열경련까지 갈 수 있으니까 말이지. 그러니, 다들 물 많이 먹고! 운동은 적당히!  ',
             ' 운동을 하다 보면 예상외의 상황이 발생하기도 한다. 타박상이나 찰과상 정도에서 멈추면 좋겠지만, 심하게는 골절까지 가는 경우가 있지. 그 때는 무리해서 움직이지 말고, 가만히 있을 것! 괜히 움직이면 출혈 위험까지 있으니, 반드시 가만히 있어야 해. ',
             ' 오늘의 수영의 4가지 영법을 배울 거다. 본인에게 맞는 수영법이 있으니까, 실전으로 천천히 터득해보도록. 평영, 자유형, 배영, 접영이 있다. 대부분의 수영이라고 하면 떠올리는 게 자유형과 평영이고, 접영과 배영은 초보자에겐 어려우니 천천히! ',
             ' 오늘은 자유 수업이다! 체육 창고를 열어두었으니, 너희가 놀고 싶은 대로 편하게 꺼내서 놀도록. 대신 물품의 반납은 제대로 해야 한다! '	]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '미술' in mention.full_text.lower():
            print('found 영어')
            print('responding back...')
            luckyday =[  ' 포르투갈어로 "일그러진 진주"라는 뜻이며, 르네상스 전성기가 지난 16세기 말부터 17세기까지 유럽 건축미술의 한 특징을 "바로크"라고 합니다. 자유분방함과 불균형만을 내세우지 않고, 최소한의 질서와 논리가 유지되는 것이 큰 장점이기도 하죠. ',
             ' 14세기에서부터 16세기까지 유럽 문명사에 나타난 문화운동, 르네상스. 학문 또는 예술의 재생·부활이라는 의미를 가지고 있으며, 그 범위는 미술 외에도 다양하게 두각이 드러났죠. 여러분이 알고 있는 예술가로는... 다빈치, 보티첼리등이 대표적이겠네요. ',
             ' 인상주의 작가로 많은 화가들이 거론되지만, 거두절미하고 불릴 수 있는 작가로는 "클로드 모네"로 뽑힙니다. 인상주의는 전후로 그와는 다른 관심과 양식을 추구했던 자들과는 다르게 "영원한 인상주의자"로 자처할 정도로 평생을 살았기 때문이지요.  ',
             ' 19세기의 근대미술들은 낭만주의, 사실주의, 인상주의로 나뉘어 구분한단다. 이 중에서 인상주의는 좀 더 나아가서 "신인상주의"와 "후기 인상주의"로까지 구분 지어지기도 하지. 시험에는 인상주의에 대해서 낼 것이니 꼼꼼하게 구분해서 외워두렴. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '가정' in mention.full_text.lower():
            print('found 영어')
            print('responding back...')
            luckyday =[  ' 권장 식사 패턴은 영양소 섭취를 만족시킬 수 있는 1일 식사 구성의 예랍니다. 식품군별 대표 식품의 1인 1회 분량을 기준으로 섭취해야 하는 횟수를 제시한 것이고, 그것을 참고하면 식단도 쉽게 계획할 수 있답니다. 모란원에서 나오는 식사도 그것을 기준으로 나오고 있죠. ',
             ' 주거 가치관은 개인이 중요하게 여기는 가치로서 주거를 선택하는 데 영향을 미칩니다. 시대에 따라 변화하고, 오늘날의 주거는 안식처나 사회적 지위, 재산적 가치뿐만이 아니라 정서적 안정, 자유로운 생활, 공동체 생활의 다양한 가치가 중요시되고 있죠. ',
             ' 진로는 인생을 살아가며 나아가는 길입니다. 이 중에도 이미 결정한 친구가 있을 거고, 없는 친구도 있을 거예요. 하지만, 진로란 직업 선택만 의미하는 것이 아니에요. 좀 더 나아가서 삶의 단계마다 주어지는 다양한 역할과 책임에 관련된 모든 일과 활동도 포함되지요. ',
             ' 생애 설계는 개인과 가족이 인생을 어떻게 살아갈 것인지에 대한 목표를 설정하고, 달성하기 위해 구체적인 계획을 세워 준비하는 것이에요. 여러분들도 3년 후엔 모란원을 졸업하니, 그 뒤의 "생애 설계"를 미리 고민해보아도 나쁘지 않겠네요. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '기술' in mention.full_text.lower():
            print('found 기술')
            print('responding back...')
            luckyday =[  ' 사람이나 물자를 다른 장소로 이동시키는 수간과 방법을 수송 기술이라며, 이것을 효율적으로 실현하는데 필요한 모든 활동을 체계화한 것을 수송 기술 시스템이라고 부른다! 쉽게 예로 들다면 버스, 지하철도 있고, 외국에 운반하는 비행기나 선박 등이 수송 기술이지! ',
             ' 사람들이 살아가며, 인구가 증가했죠. 그것으로 인하여 에너지 소비가 늘어났고, 처음에는 대부분 화석 연료에 의존하였습니다. 지금은 그것을 대처할 에너지들을 연구하고 있죠. 무엇이 있는지 오늘 알아보도록 할까요? ',
             ' 기술의 발전으로 인한 편리함은 누구나 이용되어야 하지만, 현실은 그것이 쉽지 않죠. 비용 문제로 인하여 혜택을 받지 못하는 소외계층이 생기면서, 최첨단 기술은 아니더라도 삶의 환경을 개선해 줄 수 있는 기술을 "적정 기술"이라고 한답니다.  ',
             ' 생명기술은 매년 발달되어가고 있지요. 10여 년 전 즈음에는 DNA 재조합 기술이 개발되었다고 해요. 이러한 기술의 발전은 사람들의 기대수명을 늘려준.답니다. 보건, 의료 분야에는 물론이고 농업·축산업·수산업의 식품 분야와 에너지 분야에서도 발전을 이룰 것이라고 가망을 두고 있죠. ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '영어' in mention.full_text.lower():
            print('found 영어')
            print('responding back...')
            luckyday =[ ' 관사는 부정관사(a, an)와 정관사(the)가 있습니다. an은 모음으로 시작되는 말 앞에, a는 자음으로 시작되는 말 앞에 쓰여요. 허나 철자가 모음으로 발음되는 말 앞에는 an을 쓴답니다. 따라 읽어 보아요! ',
             ' 수동태의 문장을 만들 때는 [be + 과거분사 +by]로 만들면 돼요. 능동태의 주어가 불분명하거나 생략 가능할 경우엔 by를 지우기도 합니다. 그럼 한 번'+mention.user.name +'이/가 문장을 만들어 볼까요? ',
             ' 접속사와 대명사의 구실을 겸하는 대명사를 "관계대명사"라 합니다. who, which, that, what 등이 있어요. 선행사가 사람이냐 사물이냐에 따라 사용하는 관계대명사를 결정합니다. 자! '+ mention.user.name+'이 말해볼까요? ',
             ' 형용사의 비교 변화엔 규칙 변화와 불규칙 변화가 있습니다. 원급에 -(e)r/-(e)st를 붙여 비교급, 최상급을 붙이는 형식이 바로 규칙 변화죠. 불규칙 변화에는 good- bette- best 등이 있습니다.  ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '밤줍기' in mention.full_text.lower():
            print('found 밤줍기')
            print('responding back...')
            luckyday =['1','1','1','1','2','2','2','3','3','4']
            api.update_status('@' + mention.user.screen_name + ' 주섬주섬...'+mention.user.name+'은... ['+random.choice(luckyday)+ ']개의 밤을 주웠다!\n' + str(now), mention.id)


        elif '모란석제작' in mention.full_text.lower():
            print('found 모란석제작')
            print('responding back...')
            rancolor = ['눈을 감고 집중하자... 제작에 성공했다!',
            '열심히 힘을 주었으나 아무것도 만들어지지 않았다.',
            '손 안에 작은 조각이 느껴진다. 제작에 성공했다!',
            '노력해보았으나... 오늘은 컨디션이 나쁜 걸까? 아무것도 만들어지지 않았다.']
            api.update_status('@' + mention.user.screen_name + ' '+mention.user.name +'의 결과...\n'+ random.choice(rancolor) +' \n' + str(now), mention.id)

        elif '모란석 제작' in mention.full_text.lower():
            print('found 모란석제작')
            print('responding back...')
            rancolor = ['눈을 감고 집중하자... 제작에 성공했다!',
            '열심히 힘을 주었으나 아무것도 만들어지지 않았다.',
            '손 안에 작은 조각이 느껴진다. 제작에 성공했다!',
            '노력해보았으나... 오늘은 컨디션이 나쁜 걸까? 아무것도 만들어지지 않았다.']
            api.update_status('@' + mention.user.screen_name + ' '+mention.user.name +'의 결과...\n'+ random.choice(rancolor) +' \n' + str(now), mention.id)

        elif '손질' in mention.full_text.lower():
            print('found 손질')
            print('responding back...')
            luckyday =['투당탕탕! 힘차게 재료를 손질하다가…… 앗─! 땅에 떨어트리고 말았다! (0점)',
            '투당탕탕! 힘차게 재료를 손질하다가…… 후후, 좀 잘게 잘랐지만 성공적이야! (8점)',
            '칼을 쥐는 건 조금 두렵지만…… 에잇! 날 두고 가, 얘들아! (3점)',
            '탕, 탕, 탕. 재료를 손질하는 소리가 리드미컬하게 들린다. 음, 잘 됐을지도. (10점)',
            '그러고 보니 야채는 물에 씻어야 하던가? 씻지 않아야 하던가? ……음. 에라, 모르겠다. 모두 물에 씻어버리자! (5점)']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '공건지기' in mention.full_text.lower():
            print('found 공건지기')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' 잘 찢어질 것 같은 뜰채를 받았다. 그래도 해봐야겠지! 내가 건진 슈퍼볼의 갯수는!\n……\n…………\n……………… 『' +str(random.randrange(0,16))+ '』개!\n' + str(now), mention.id)

        elif '사격' in mention.full_text.lower():
            print('found 사격')
            print('responding back...')
            luckyday =['탕! 탕!\n공기총이 나무패를 쓰러트리는 소리가 경쾌하다!\n 내가 쓰러트린 나무패는……\n'+ str(random.randrange(1,101))+'개!\n 이걸로 무슨 경품이랑 교환하지?', '탕! 탁! 탕! 탁!\n……맞긴 맞는데, 애꿎은 벽만 열심히 맞췄다. 옆에서 선배가 풋! 하고 크게 비웃는다.', '탕, 탕, 탕!\n하, 이 정도야 식은 죽 먹기지! 6번 연속 나무패 쓰러트리기에 성공했다!\n 이걸로 경품을 싹 쓸어올 수 있겠어!']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)


        elif '솜사탕만들기' in mention.full_text.lower():
                    print('found 사격')
                    print('responding back...')
                    luckyday =['드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n몽실몽실, 파스텔빛 실이 뭉치더니……. 무지개 솜사탕이 완성되었다!', '드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n…………………………\n어?! 넋 놓고 있는 사이, 2m 솜사탕이 완성되어버렸다! 언제 다 먹어?!','드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n……\n이상하다, 솜사탕이 원래 검은색도 있었나?! 이 솜사탕에게서, 익숙한 고기 냄새가 난다?',
                    '드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n……\n이상하다, 솜사탕이 원래 검은색도 있었나?! 이 솜사탕에게서, 익숙한 조개구이 냄새가 난다?',
                    '드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n……\n이상하다, 솜사탕이 원래 검은색도 있었나?! 이 솜사탕에게서, 익숙한 닭꼬치 냄새가 난다?',
                    '드륵드륵 돌아가는 기계에 나무젓가락을 넣어본다.\n……\n이상하다, 솜사탕이 원래 검은색도 있었나?! 이 솜사탕에게서, 익숙한 갈비 냄새가 난다?']
                    api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '사과사탕' in mention.full_text.lower():
                    print('found 사과사탕')
                    print('responding back...')
                    tasty=['메론', '바나나', '초코', '포도', '솜사탕', '고구마']
                    dis=['취두부','오이','토마토','완두콩','사이다']
                    luckyday =['사과사탕을 물었다!\n"어이! 지금 감히 날 물었냐!"\n으악, 사탕이 말했다! 깜짝 놀라서 사탕을 떨어트리고 말았다.', '사과사탕을 물었다! 평범한 사과맛이 나는 것 같은데, 이건……?\n"어이! 난 3대 독자에 속하는 고귀한 사과 씨족의 사과라고! 어딜 무는 거냐!"\n으악, 사탕이 말했다! 깜짝 놀라서 사탕을 떨어트리고 말았다.',
                    '사과사탕을 물었다! 어쩐지 달콤한 맛이 나는데, 이거 혹시'+ random.choice(tasty)+'맛?', '사과사탕을 물었다. 평범한 사과사탕인 거 같은데, 뭔가, 이상하다?\n"사과?(뭐지?)"\n……?!\n"사과, 사과!(뭐야, 뭐냐고!)"\n사, 사과?! 나 사과 밖에 말하지 못하게 된 거야?! (*1시간 지속/모든 말이 "사과"가 됩니다.)',
                    '사과사탕을 물었다! 어쩐지 이거, 이상한 맛, 이……?!\n으, '+ random.choice(dis)+'맛이다!']
                    api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '요리재료' in mention.full_text.lower():
            print('found 요리재료')
            print('responding back...')
            luckyday =[ ' 오리고기 ',
             ' 햄 ',
             ' 닭고기 ',
             ' 게맛살 ',
             ' 소고기 ',
             ' 돼지고기 ',
             ' 베이컨 ',
             ' 살라미 ',
             ' 참치 ',
             ' 멸치 ',
             ' 고등어 ',
             ' 연어 ',
             ' 낙지 ',
             ' 정어리 ',
             ' 문어 ',
             ' 바지락 ',
             ' 대합 ',
             ' 대게 ',
             ' 미역 ',
             ' 사과 ',
             ' 파프리카 ',
             ' 바나나 ',
             ' 딸기 ',
             ' 마늘 ',
             ' 레몬 ',
             ' 당근 ',
             ' 스위트콘 ',
             ' 청양고추 ',
             ' 파슬리 ',
             ' 토마토 ',
             ' 우엉 ',
             ' 포도 ',
             ' 가지 ',
             ' 통밀 ',
             ' 파슬리 ',
             ' 호박 ',
             ' 캐모마일 ',
             ' 완두콩 ',
             ' 낫토 ',
             ' 취두부 ',
             ' 흰 우유 ',
             ' 딸기우유 ',
             ' 초코우유 ',
             ' 초콜릿 ',
             ' 요거트 ',
             ' 빵 ',
             ' 치즈 ',
             ' 호두 ',
             ' 땅콩 ',
             ' 아몬드 ',
             ' 달걀 ',
             ' 떡 ',
             ' 라면스프 ',
             ' 메이플 시럽 ',
             ' 연유 ',
             ' 타르타르 소스 ',
             ' 마요네즈 ',
             ' 튀김가루 ',
             ' 일본식 된장 ',
             ' 특제 핫소스 ',
             ' 매운 고추 ',
             ' 꿀 ',
             ' 와사비 ',
             ' 소금 ',
             ' 설탕 ',
             ' 식용유 ',
             ' 후추 ',
             ' 간장 ',
             ' 각종 조리도구 ',
             ' 쌀밥 / 보리밥 ']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '를 획득했다.\n' + str(now), mention.id)

        elif '활쏘기' in mention.full_text.lower():
            print('found 활쏘기')
            print('responding back...')
            luckyday =['활을 시위에 걸고 쭉 당긴 후, 심호흡을 하고, 그대로…… 탁! 날아간 화살이 과녘을 멋지게 맞췄다!',
            '활을 시위에 걸…… 걸고? 어떻게 하는지 몰라 허둥대고 있으니 마사치카 선생님이 손수 도와주러 왔다.',
            '활을 시위에 걸고, 자세를 곧게 하고, 그대로 쏜다! …………허공을 가로지른 화살이 탁, 바닥에 떨어졌다.'	]
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '공굴리기' in mention.full_text.lower():
            print('found 공굴리기')
            print('responding back...')
            luckyday =['커다란 공에 올라타 중심을 잡고 앞으로 나아가야 하는 종목이다! 아니, 근데, 이거, 서커스, 아니야?! 나 지금 1초 만에 떨어졌다구?!',
            '커다란 공에 올라타서 열심히, 중심을…… 중심을…… 서, 성공했어! 이제 골까지 단숨에 가자!',
            '이 정도야 식은 죽 먹기지! 멋지게 올라타 멋지게 굴러서 멋지게 골인했다!']
            api.update_status('@' + mention.user.screen_name + ' ' +random.choice(luckyday)+ '\n' + str(now), mention.id)

        elif '원반던지기' in mention.full_text.lower():
            print('found 원반던지기')
            print('responding back...')
            rancolor = ['빨강','노랑','파랑','초록']
            api.update_status('@' + mention.user.screen_name + ' '+ random.choice(rancolor) +'원반을 집어 들고, ……던진다! 내 결과는?!\n['+ str(random.randrange(61,201))+'cm] \n' + str(now), mention.id)

        elif '빵냠' in mention.full_text.lower():
            print('found 빵냠')
            print('responding back...')
            rantaste1 = ['딸기', '초코', '레몬', '포도', '메론', '파인애플', '땅콩버터', '슈크림', '고등어']
            rantaste2 = ['완두콩', '와사비', '문어', '카레', '하와이안피자', '타바스코', '물', '샐러드', '낫토', '고구마']
            rancolor = ['빵을 냠! 물었다! …………오, ['+random.choice(rantaste1)+'] 맛이야!',
            '빵을 냠! 물었다! …………아. ['+random.choice(rantaste2)+'] 맛이야.']
            api.update_status('@' + mention.user.screen_name + ' '+ random.choice(rancolor) + '\n' + str(now), mention.id)

        elif '훌라후프' in mention.full_text.lower():
            print('found 훌라후프')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' 훌라후프 2개 동시 돌리기에 도전했다! 과연 마사치카 선생님이 평가하는 내 점수는?!\n…………\n……\n['+ str(random.randrange(1,101))+'] !' + '\n' + str(now), mention.id)

        elif '멀리뛰기' in mention.full_text.lower():
            print('found 멀리뛰기')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' 도움닫기 후 힘차게 발판을 박차고 점프! 옆에서 측정 로봇이 다가와 내 점수를 보여주었다.\n…………\n……\n['+str(random.randrange(1,101))+']점?!'+ '\n' + str(now), mention.id)

        elif '쪽지' in mention.full_text.lower():
            print('found 쪽지')
            print('responding back...')
            ranpaper=['리본을 한 사람',
            '겉옷을 걸친 사람',
            '노란 머리인 사람',
            '까만 머리인 사람',
            '초록 눈인 사람',
            '예의바른 사람',
            '어른스러운 사람',
            '얌전한 사람',
            '부드러운 사람',
            '사고뭉치',
            '신기한 사람',
            '씩씩한 사람',
            '따뜻한 사람',
            '차가운 사람',
            '힘이 센 사람',
            '점 있는 사람',
            '꾸민 사람',
            '덜렁대는 사람',
            '투덜대는 사람',
            '조용한 사람']
            api.update_status('@' + mention.user.screen_name + ' ' + mention.user.name +'의 쪽지는... ' +random.choice(ranpaper)+'...!\n'+ str(now), mention.id)


        elif '츠바키' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='tsubaki.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '키리야' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='kiriya.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '후와리' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='fuwari.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '센' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='sen.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '츠바사' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='tsubasa.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '타카요코' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='takayoko.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '야스하' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='yasuha.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '카이' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='kai.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '렌' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='ren.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        #체질

        elif '소노' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='sono.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '미오' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='mio.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '코코에' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='kokoe.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '카야' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='kaya.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '세이지' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='seige.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '카논' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='kanon.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '에이지로' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='agiro.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '산고' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='sango.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '안지' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='anji.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        #기술

        elif '와타루' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='wataru.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '하루토' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='haruto.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '묘카' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='myoka.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '치카' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='chika.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '세이토' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='seito.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '아리스' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='alice.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '사쿠야' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='sakuya.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        #특능

        elif '우츠츠' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='utsutsu.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '미야비' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='miyabi.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '유우' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='yuu.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '마키타로' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='makitaro.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)


        elif '에제' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='eje.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '하루야' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='haruya.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '시즈카' in mention.full_text.lower():
            print('responding back...')
            FLOWER_FILE='shizuka.txt'
            if('물주기') in mention.full_text.lower():
                bi = random.randrange(1,4)
                otoha_num = find_flower_exp(FLOWER_FILE) + bi
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('비료') in mention.full_text.lower():
                youngy = random.randrange(3,6)
                otoha_num = find_flower_exp(FLOWER_FILE) + youngy
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            elif('영양제') in mention.full_text.lower():
                wate = random.randrange(5,9)
                otoha_num = find_flower_exp(FLOWER_FILE) + wate
                save_flower_exp('000'+str(otoha_num), FLOWER_FILE)
            else:
                otoha_num = -1

            flower_app_show(otoha_num, mention.user.screen_name, mention.user.name, str(now), mention.id)

        elif '뽑기' in mention.full_text.lower():
            print('found 뽑기')
            print('responding back...')
            moe = [  ' 시집(20억년의 고독)  ',
             ' 뱃지(금으로 만들어진 꽃모양 뱃지) ',
             ' 붉은색과 흰색이 섞인 귀걸이 ',
             ' 마리아 수녀상 ',
             ' 연탄 ',
             ' 해바라기 조화 꽃송이 ',
             ' 작은 머리핀(반짝이는 재질) ',
             ' 차가운 눈 스프레이 ',
             ' 죽순 ',
             ' 쇼기(일본식 장기)말 ',
             ' 노란색 오마모리 ',
             ' 단단한 알사탕 ',
             ' 나무로 된 반달모양의 머리빗 ',
             ' 작은 허브나무 화분 ',
             ' 제비꽃 마크가 달린 화려한 옷들 ',
             ' 포도당 캔디 ',
             ' 생쥐용 츄르 ',
             ' 주사기 침선 ',
             ' 뜨거운 우정 이야기를 담은 소설책 ',
             ' 활짝 핀 모란 꽃 ',
             ' 왼손잡이를 위한 가위 ',
             ' 인어공주 인형 ',
             ' 해바라기 자수가 새겨진 손수건 ',
             ' 특제 시큼새콤 젤리 모음 ',
             ' 연하늘색 표지의 정리 노트',
             ' 전통 문양이 수놓아진 끈 ',
             ' 화끈한 매운맛 사탕 ',
             ' 작은 탁상 조명 ',
             ' 노란 백일홍이 새겨진 오마모리 ',
             ' 발음 연습 문장 모음집 ',
             ' 토마토 모종이 담긴 화분 ',
             ' 초록빛의 머리핀 ',
             ' 가습기 ',
             ' 커다란 나비 모찌인형 ',
             ' 모과꽃이 새겨진 옥패 ',
             ' 금간 흰색 도자기 인형 ',
             ' 고기 모양의 푹신한 인형 ',
             ' 분홍색 리본 ',
             ' 영어 교과서 ',
             ' 세계명화 직소퍼즐  ',
             ' 건강기원 오마모리 ',
             ' 주사기 ',
             ' 해바라기 물뿌리개 ',
             ' 식물도감 ',
             ' 벌레모형 ',
             ' 앗, 맵다! 매운 스낵 ',
             ' 붉은색 끈 팔찌 ',
             ' 안대 ',
             ' 휴대용 게임기 ',
             ' 최다 구성 게임팩 ',
             ' 동물 육성 시뮬레이션 게임(다x고치) ',
             ' 에그타르트 ',
             ' 손바닥만한 노란색 토끼 인형 ',
             ' 동화책 [빨간모자] ',
             ' 여름과일향 향수 ',
             ' 웃긴 표정의 쿠션 ',
             ' 행복한 왕자 그림 동화책 ',
             ' 원석 팔찌 ',
             ' 작은 꽃화분  ',
             ' 열자마자 범인이 적혀있는 추리소설 ',
             ' 그림책 ',
             ' 비밀 다이어리 ',
             ' 박하사탕 ',
             ' 생명과학 - 세균의 발견 책 ',
             ' 소독용 알코올 솜 ',
             ' 예쁜 액자 ',
             ' 글러브 ',
             ' 초콜릿 ',
             ' 인사하는 리얼 곰 사진 ',
             ' 하얀 조개 팬던트 목걸이 ',
             ' 펭귄이 그려진 담요 ',
             ' 종합 자습서 ',
             ' 동백꽃 ',
             ' 지우산 ',
             ' 고급 동물 간식 종합세트 ',
             ' 폴라로이드 사진기 ',
             ' 조각난 편지 ',
             ' 고급 수제 화과자 ',
             ' 화려한 무늬가 수놓아진 비단 리본 ',
             ' 모조 1엔짜리 동전 ',
             ' 책(해신의 전설) ',
             ' 조개껍떼기 ',
             ' 낙엽책갈피 ',
             ' 임상실험부 홍보지 ',
             ' 대머리수리 머리털 ',
             ' 흰고양이 인형 ',
             ' 저주인형 ',
             ' 검은색 양털 담요 ',
             ' 헤비메탈의 모든 것 ',
             ' 홍삼 사탕 ',
             ' 말차 가루 티백 ',
             ' 무드등 ',
             ' 영양제 ',
             ' 수학책 ',
             ' 모조 돈 ',
             ' 벽돌 ']
            api.update_status('@' + mention.user.screen_name +  "<"+mention.user.name +"의 손에서 나온 건\n. . . . .\n"+random.choice(moe)+"!>" + str(now), mention.id)


        elif '탕진' in mention.full_text.lower():
            print('found 탕진')
            print('responding back...')
            moe = [' 시집(20억년의 고독)  ',
             ' 뱃지(금으로 만들어진 꽃모양 뱃지) ',
             ' 붉은색과 흰색이 섞인 귀걸이 ',
             ' 마리아 수녀상 ',
             ' 연탄 ',
             ' 해바라기 조화 꽃송이 ',
             ' 작은 머리핀(반짝이는 재질) ',
             ' 차가운 눈 스프레이 ',
             ' 죽순 ',
             ' 쇼기(일본식 장기)말 ',
             ' 노란색 오마모리 ',
             ' 단단한 알사탕 ',
             ' 나무로 된 반달모양의 머리빗 ',
             ' 작은 허브나무 화분 ',
             ' 제비꽃 마크가 달린 화려한 옷들 ',
             ' 포도당 캔디 ',
             ' 생쥐용 츄르 ',
             ' 주사기 침선 ',
             ' 뜨거운 우정 이야기를 담은 소설책 ',
             ' 활짝 핀 모란 꽃 ',
             ' 왼손잡이를 위한 가위 ',
             ' 인어공주 인형 ',
             ' 해바라기 자수가 새겨진 손수건 ',
             ' 특제 시큼새콤 젤리 모음 ',
             ' 연하늘색 표지의 정리 노트',
             ' 전통 문양이 수놓아진 끈',
             ' 화끈한 매운맛 사탕',
             ' 작은 탁상 조명 ',
             ' 노란 백일홍이 새겨진 오마모리 ',
             ' 발음 연습 문장 모음집 ',
             ' 토마토 모종이 담긴 화분 ',
             ' 초록빛의 머리핀 ',
             ' 가습기 ',
             ' 커다란 나비 모찌인형 ',
             ' 모과꽃이 새겨진 옥패 ',
             ' 금간 흰색 도자기 인형 ',
             ' 고기 모양의 푹신한 인형 ',
             ' 분홍색 리본 ',
             ' 영어 교과서 ',
             ' 세계명화 직소퍼즐  ',
             ' 건강기원 오마모리 ',
             ' 주사기 ',
             ' 해바라기 물뿌리개 ',
             ' 식물도감 ',
             ' 벌레모형 ',
             ' 앗, 맵다! 매운 스낵 ',
             ' 붉은색 끈 팔찌 ',
             ' 안대 ',
             ' 휴대용 게임기 ',
             ' 최다 구성 게임팩 ',
             ' 동물 육성 시뮬레이션 게임(다x고치) ',
             ' 에그타르트 ',
             ' 손바닥만한 노란색 토끼 인형 ',
             ' 동화책 [빨간모자] ',
             ' 여름과일향 향수 ',
             ' 웃긴 표정의 쿠션 ',
             ' 행복한 왕자 그림 동화책',
             ' 원석 팔찌 ',
             ' 작은 꽃화분 ',
             ' 열자마자 범인이 적혀있는 추리소설 ',
             ' 그림책 ',
             ' 비밀 다이어리 ',
             ' 박하사탕 ',
             ' 생명과학 - 세균의 발견 책 ',
             ' 소독용 알코올 솜 ',
             ' 예쁜 액자 ',
             ' 글러브 ',
             ' 초콜릿 ',
             ' 인사하는 리얼 곰 사진 ',
             ' 하얀 조개 팬던트 목걸이 ',
             ' 펭귄이 그려진 담요 ',
             ' 종합 자습서 ',
             ' 동백꽃 ',
             ' 지우산 ',
             ' 고급 동물 간식 종합세트 ',
             ' 폴라로이드 사진기 ',
             ' 조각난 편지 ',
             ' 고급 수제 화과자 ',
             ' 화려한 무늬가 수놓아진 비단 리본 ',
             ' 모조 1엔짜리 동전 ',
             ' 책(해신의 전설) ',
             ' 조개껍떼기 ',
             ' 낙엽책갈피 ',
             ' 임상실험부 홍보지 ',
             ' 대머리수리 머리털 ',
             ' 흰고양이 인형 ',
             ' 저주인형 ',
             ' 검은색 양털 담요 ',
             ' 헤비메탈의 모든 것 ',
             ' 홍삼 사탕 ',
             ' 말차 가루 티백 ',
             ' 무드등 ',
             ' 영양제 ',
             ' 수학책 ',
             ' 모조 돈 ',
             ' 벽돌 ', '1회용 모란석(순간이동). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(발화). 해당 링크를 정산 게시판에 정산해주세요. ', '1회용 모란석(악기연주). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(요리). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(작곡). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(환각). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(천리안). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(비행). 해당 링크를 정산 게시판에 정산해주세요.', '재뽑기권 1회. 1회 더 탕진해보자!', '수근수근 쪽지. 해당 링크를 가지고 상점계 DM으로 찾아가면 [상점계 퍼블릭으로 트윗 게시 요청]을 할 수 있습니다.', '1회용 모란석(순간이동). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(발화). 해당 링크를 정산 게시판에 정산해주세요. ', '1회용 모란석(악기연주). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(요리). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(작곡). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(환각). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(천리안). 해당 링크를 정산 게시판에 정산해주세요.', '1회용 모란석(비행). 해당 링크를 정산 게시판에 정산해주세요.', '재뽑기권 1회. 1회 더 탕진해보자!', '수근수근 쪽지. 해당 링크를 가지고 상점계 DM으로 찾아가면 [상점계 퍼블릭으로 트윗 게시 요청]을 할 수 있습니다.',
            '수상한 부적. 인벤토리 획득을 위하여 정산 게시판에 정산해주세요.', '수상한 부적. 인벤토리 획득을 위하여 정산 게시판에 정산해주세요.', '파워스톤. 인벤토리 획득을 위하여 정산 게시판에 정산해주세요.',
            str(random.randrange(200,300))+'요우 획득. 정산 게시판에 정산해주세요.']
            api.update_status('@' + mention.user.screen_name +  "<"+mention.user.name +"의 손에서 나온 건\n. . . . .\n"+random.choice(moe)+"!>" + str(now), mention.id)



while True:
    reply_to_tweets()
    time.sleep(30)