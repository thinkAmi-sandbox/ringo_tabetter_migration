import traceback
from before import database as before_db, Apples, Tweets
from after import database as after_db, TweetsLastsearch, TweetsTweets

# 実行前に、新旧のデータベースに対しpwizを実行してmodelを自動生成しておく
# (下を一行にて実行する)
# python -m pwiz -e postgresql
# -u `user name`
# -P `password`
# -H `host name`
# `database name` > `before.py|after.py`


def main():
    '''新旧のテーブル移行処理'''
    try:
        with before_db.transaction():
            tweets = Apples.select()
            last = Tweets.select()

            with after_db.transaction():
                tweet_source = [convert_tweet(x) for x in tweets ]
                TweetsTweets.insert_many(tweet_source).execute()

                last_source = [{ 'prev_since': last[0].last_searched }]
                TweetsLastsearch.insert_many(last_source).execute()

                print('commit')

    except Exception:
        traceback.print_exc()
        print('error')


def convert_tweet(tweets):
    '''新旧のテーブル列をマッピング'''
    return {
        'name': tweets.name,
        'tweet': tweets.tweet,
        'tweet_id': tweets.tweet_id,
        'tweeted_at': tweets.tweeted_at
    }


if __name__ == '__main__':
    main()