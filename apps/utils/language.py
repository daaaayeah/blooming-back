from google.cloud import language_v1

def sample_analyze_sentiment(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "ko"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    """
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )

    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    print(u"Language of the text: {}".format(response.language))
    """
    return (response.document_sentiment.score, response.document_sentiment.magnitude)



def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--text_content", type=str, default="")
    args = parser.parse_args()

    sample_analyze_sentiment(args.text_content)


if __name__ == "__main__":
    main()
