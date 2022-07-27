import inject
# from app.infra.repository.mongo.mongo_operations import MongoOperations
# from app.infra.repository.redis.redis_operations import RedisOperations

def configure_inject() -> None:
  def config(binder: inject.Binder) -> None:
    # binder.bind(DatabaseOperations, RedisOperations),
    pass
  inject.configure(config)

def register_dependency_injection() -> None:
  configure_inject()
