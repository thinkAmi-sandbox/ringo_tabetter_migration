from peewee import *

database = PostgresqlDatabase(<your connection>)

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Accounts(BaseModel):
    created_at = DateTimeField()
    crypted_password = CharField(null=True)
    email = CharField(null=True)
    name = CharField(null=True)
    role = CharField(null=True)
    surname = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'accounts'

class Apples(BaseModel):
    created_at = DateTimeField()
    name = CharField(null=True)
    tweet = CharField(null=True)
    tweet_id = BigIntegerField(null=True)
    tweeted_at = DateTimeField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'apples'

class SchemaMigrations(BaseModel):
    version = CharField(unique=True)

    class Meta:
        db_table = 'schema_migrations'

class Tweets(BaseModel):
    created_at = DateTimeField()
    last_searched = BigIntegerField(db_column='last_searched_id', null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'tweets'

