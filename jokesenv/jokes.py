# Virtual environments are isolated Python environments that contain all the packages and dependencies specific to a particular project. 
# Any packages installed in one virtual environment will not affect other virtual environments or the system Python installation.

try:
    import pyjokes #pyjokes is installed only in the jokesenv environment
    joke = pyjokes.get_joke('en','neutral')
    print(joke)

except: #if the virtual environment is not activate then pyjokes won't be available
    print('You need pyjokes installed to get a joke')

