from google.cloud import language_v1

#######################################################################################    
#######################################################################################
# 구문 분석
# 주어진 텍스트를 일련의 구문과 토큰(일반적으로 단어)으로 분해하여 해당 토큰의 언어적 정보를 제공
def sample_analyze_syntax(text_content):
    """
    Analyzing Syntax in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'This is a short sentence.'

    # 사용가능한 유형 : PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # 선택사항. 지정하지 않으면 언어가 자동으로 감지됨
    # 지원되는 언어목록 : https://cloud.google.com/natural-language/docs/languages
    language = "ko"
    document = {"content": text_content, "type_": type_, "language": language}

    # 인코딩 타입
    # 사용 가능한 값 : NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    # 요청
    response = client.analyze_syntax(
        request={"document": document, "encoding_type": encoding_type}
    )
    
    
    # 반환된 토큰을 반복문으로 출력
    for token in response.tokens:
        # 토큰의 내용을 가져옴 
        # 일반적으로  단어나 구두점
        text = token.text
        print(f"Token text: {text.content}")
        print(f"Location of this token in overall document: {text.begin_offset}")
        # 토큰에 대한 품사정보, 참고링크
        # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
        part_of_speech = token.part_of_speech
        # 품사 태그를 가져옴 명사, 형용사 등
        print(
            "Part of Speech tag: {}".format(
                language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
            )
        )

        # 사용가능한 추가 품사 정보는 API 참조
        # 토큰의 기본형을 가져옴 위키피디아 기본형 설명
        # https://en.wikipedia.org/wiki/Lemma_(morphology)
        print(f"Lemma: {token.lemma}")
        # 종속성 트리구문 분석정보
        # 종속성 레이블 참조
        # http://www.aclweb.org/anthology/P13-2017
        dependency_edge = token.dependency_edge
        print(f"Head token index: {dependency_edge.head_token_index}")
        print(
            "Label: {}".format(
                language_v1.DependencyEdge.Label(dependency_edge.label).name
            )
        )
        print("===========================")

    # 분석에 사용된 언어
    # 언어가 지정되었으면 지정된 언어,
    # 미지정시 감지된 언어
    print(f"Language of the text: {response.language}")
    print("##########################################################################")
    print("##########################################################################")
    
#######################################################################################    
#######################################################################################

YOUTUBE = 1
SHOW_MESSAGE = 1 << 1
CAP_MESSAGE = 1 << 2
WEATHER = 1 << 3
NEWS = 1 << 4
UNEXPECT = 0

order = {"유튜브" : YOUTUBE, 
        "영상" :  SHOW_MESSAGE | CAP_MESSAGE, "메세지" : SHOW_MESSAGE | CAP_MESSAGE, "영상메세지" : SHOW_MESSAGE | CAP_MESSAGE,
        "메시지" : SHOW_MESSAGE | CAP_MESSAGE, "영상메시지": SHOW_MESSAGE | CAP_MESSAGE,
        "날씨" : WEATHER,
        "뉴스" : NEWS,

        "unexpect" : -1}

order_keyword = { "검색" : YOUTUBE, "찾아" : YOUTUBE, "찾아줘" : YOUTUBE, "찾아봐" : YOUTUBE,

        "보여" : SHOW_MESSAGE | NEWS, "보여줘" : SHOW_MESSAGE | NEWS, 
        "띄워" : SHOW_MESSAGE, "띄워줘" : SHOW_MESSAGE,
        "보내" : CAP_MESSAGE, "보내줘" : CAP_MESSAGE, 
        "찍어" : CAP_MESSAGE, "찍어줘" : CAP_MESSAGE, 
        "촬영" : CAP_MESSAGE,

        "에" : CAP_MESSAGE | YOUTUBE, "에게" : CAP_MESSAGE, "께" : CAP_MESSAGE, "한테" : CAP_MESSAGE,

        "도" : WEATHER, "어때" : WEATHER,

        "오늘" : NEWS | WEATHER, "알려줘" : NEWS | WEATHER,
}

family = {"아빠" : 0, "엄마" : 1, "아버지" : 0, "어머니" : 1, "누나" : 2}
"""https://www.youtube.com/results?search_query=싸피"""

def expect_youtube(response):
    # print("유튜브 보여주기")
    return "유튜브 검색 결과입니다."
    # search_keyword = ""

def expect_message_show(response):
    # print("메세지 보여주기")
    return "메세지를 보여드리겠습니다."

def expect_message_cap(response):
    target_post = ["에", "에게", "께", "한테"]
    
    target_expect = ""

    for token in response.tokens:
        if token.text.content in target_post:
            break
        target_expect = token.text.content
    if target_expect not in family:
        # print("누구에게 보내는지 모르겠어요")
        return "누구에게 보내는지 모르겠어요"

    # print(f"{target_expect}님께 보낼 메세지 녹화")
    return f"{target_expect}님께 보낼 메세지를 녹화하겠습니다."

def expect_weather(*response):
    # print("날씨 관련 요청")
    return "날씨 관련 요청을 받았습니다."

def expect_news(*response):
    # print("뉴스 관련 요청")
    return "뉴스 관련 요청을 받았습니다"

def cant_understand(*response):
    # print("이해하지 못 했어요")
    return "이해하지 못 했어요"



functoins = [expect_youtube, expect_message_show, expect_message_cap, expect_weather, expect_news, cant_understand]

#######################################################################################    
#######################################################################################

def my_analyze(text_content):
    # print(text_content)
    client = language_v1.LanguageServiceClient()

    # text_content = 'This is a short sentence.'

    # 사용가능한 유형 : PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # 선택사항. 지정하지 않으면 언어가 자동으로 감지됨
    # 지원되는 언어목록 : https://cloud.google.com/natural-language/docs/languages
    language = "ko"
    document = {"content": text_content, "type_": type_, "language": language}

    # 인코딩 타입
    # 사용 가능한 값 : NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    # 요청
    response = client.analyze_syntax(
        request={"document": document, "encoding_type": encoding_type}
    )

    # 구분된 결과에 따라 예측동작을 찾기
    expect_order = 0
    order_key = 0
    for token in response.tokens:
        # 문장 길이가 길경우 이해하지 못했어요
        if len(response.tokens) >= 10:
            break

        expect_order = expect_order | order.get(token.text.content, 0)
        order_key = order_key | order_keyword.get(token.text.content, 0)
        # print(token.text.content)
        # print(bin(expect_order))
        # print(bin(order_key))
        # print("==========")

    final_order = expect_order & order_key

    # print(bin(final_order))

    temp = -1
    for i in range(5):
        if temp == -1 and final_order & (1 << i):
            temp = i

        elif temp != -1 and final_order & (1 << i):
            temp = -1
            break


    return temp, functoins[temp](response)
            





    
if __name__ == '__main__':
    
    text_list = ["유튜브에 IOT 검색해줘",
	            "유튜브에 싸피 검색해줘",
                "유튜브에 오늘의 날씨 검색해줘", # 이건 날씨와 유튜브 2가지가 같이 예측되서 안된다고 나옴 

                "메세지 보여줘",
                "영상메세지 보여줘",

                "엄마한테 메세지 녹화해 줘",
                "어머니께 메세지 보내줘",
                "메세지 누나한테 녹화해 줘",
                "없는사람한테 메세지 보내줘",
                
                "문제 언제 풀어와?"]

    my_analyze("엄마한테 메시지 보내 줘")
    # for text in text_list:
    #     my_analyze(text)
    #     print("=======================")



    
    
