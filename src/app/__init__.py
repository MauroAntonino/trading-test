from app.extensions.injector import register_dependency_injection

def create_app():
  register_dependency_injection()
  return