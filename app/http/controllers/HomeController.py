''' A Module Description '''
from masonite.facades.Auth import Auth
from app.Question import Question
from app.Category import Category

class HomeController(object):
    ''' Home Dashboard Controller '''

    def __init__(self):
        pass
    
    def index(self, Request):
        page = Request.input('page', 1)

        questions = Question.paginate(10, int(page))
        categories = Category.all()
        
        search = Request.input('search')

        if search:
            questions = Question.where('title', 'like', '%{0}%'.format(search)).paginate(10, int(page))

        return view('index', {'questions': questions, 'categories': categories})
