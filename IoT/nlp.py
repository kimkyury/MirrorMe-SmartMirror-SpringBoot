from google.cloud import language_v1


#######################################################################################    
#######################################################################################
# 항목 분석
# 주어진 텍스트에서 알려진 항목(유명 인사, 명소 등의 고유 명사)을 검사하고 항목의 정보를 반환
def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "ko"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(
        request={"document": document, "encoding_type": encoding_type}
    )

    # Loop through entitites returned from the API
    for entity in response.entities:
        print(f"Representative name for the entity: {entity.name}")

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(f"Entity type: {language_v1.Entity.Type(entity.type_).name}")

        # Get the salience score associated with the entity in the [0, 1.0] range
        print(f"Salience score: {entity.salience}")

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(f"{metadata_name}: {metadata_value}")

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(f"Mention text: {mention.text.content}")

            # Get the mention type, e.g. PROPER for proper noun
            print(
                "Mention type: {}".format(
                    language_v1.EntityMention.Type(mention.type_).name
                )
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(f"Language of the text: {response.language}")
    print("##########################################################################")
    print("##########################################################################")
    
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

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "ko"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(
        request={"document": document, "encoding_type": encoding_type}
    )
    
    print(len(response.tokens))
    # Loop through tokens returned from the API
    for token in response.tokens:
        # Get the text content of this token. Usually a word or punctuation.
        text = token.text
        print(f"Token text: {text.content}")
        print(f"Location of this token in overall document: {text.begin_offset}")
        # Get the part of speech information for this token.
        # Part of speech is defined in:
        # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
        part_of_speech = token.part_of_speech
        # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
        print(
            "Part of Speech tag: {}".format(
                language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
            )
        )
        # Get the voice, e.g. ACTIVE or PASSIVE
        print(
            "Voice: {}".format(
                language_v1.PartOfSpeech.Voice(part_of_speech.voice).name
            )
        )
        # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
        print(
            "Tense: {}".format(
                language_v1.PartOfSpeech.Tense(part_of_speech.tense).name
            )
        )
        
        print(
            "case: {}".format(
                language_v1.PartOfSpeech.Case(part_of_speech.case).name
            )
        )
        # See API reference for additional Part of Speech information available
        # Get the lemma of the token. Wikipedia lemma description
        # https://en.wikipedia.org/wiki/Lemma_(morphology)
        print(f"Lemma: {token.lemma}")
        # Get the dependency tree parse information for this token.
        # For more information on dependency labels:
        # http://www.aclweb.org/anthology/P13-2017
        dependency_edge = token.dependency_edge
        print(f"Head token index: {dependency_edge.head_token_index}")
        print(
            "Label: {}".format(
                language_v1.DependencyEdge.Label(dependency_edge.label).name
            )
        )
        print("===========================")

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    
    print(f"Language of the text: {response.language}")
    print("##########################################################################")
    print("##########################################################################")
    
#######################################################################################    
#######################################################################################
# 감정 분석
# 주어진 텍스트를 조사하고 텍스트 내의 주도적인 감정적 의견을 식별하여
# 작성자의 태도가 긍정적인지, 부정적인지 또는 중립적인지를 판단합니다
def sample_analyze_sentiment(content):
    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, bytes):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print(f"Score: {sentiment.score}")
    print(f"Magnitude: {sentiment.magnitude}")
    print("##########################################################################")
    print("##########################################################################")
        
#######################################################################################    
#######################################################################################

    
    
if __name__ == '__main__':
	# text = "아니 그거말고 다시"
	# text = "응"
	text = "유튜브에 ssafy 검색해줘"
# 	sample_analyze_entities(text)
	sample_analyze_syntax(text)
#	sample_analyze_sentiment(text)
    
    
