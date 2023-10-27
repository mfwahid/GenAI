from lib import common as common
from classes import news
from classes import awsapi


def main():
    # Inputs
    s3bucketname = "bdnewsdocsnv"
    # apikey='4a3878ceccae4a3fbf95079564286bca'
    apikey = "079d77eb8be748ff83b0cb799afecd3c"
    country = "us"
    # category='business'
    # category='entertainment'
    category = "general"
    type = "top"
    # category='health'
    # category='science'
    # category='sports'
    # category='technology'
    path = country + "/" + category + "/" + type
    filename = common.get_new_filename(category + "-" + type + "news", "json")
    # inputs

    # objects
    obj_news = news.News(apikey, country, category)
    obj_aws_s3 = awsapi.aws_s3(s3bucketname, path, filename)
    obj_aws_bedrock = awsapi.aws_bedrock()
    # objects

    # printallarticles(country,category,apikey)

    content = obj_news.get_topnewsbycountrycategory()
    content_json = obj_news.getcontentJSON(content, type)
    data = obj_aws_s3.uploadJSONContenttoS3(content_json)
    response = obj_aws_bedrock.getTitanEmbedding(content_json)
    # print(data)
    print(
        "written to s3 bucket file : s3://" + s3bucketname + "/" + path + "/" + filename
    )
    # print(response)
    # data = aws.uploadJSONContenttoS3(country,category,'top',content,'bdnewsdocs','Article2.json')
    # print(content)


if __name__ == "__main__":
    main()
