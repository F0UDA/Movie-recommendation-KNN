from view import View
from presenter import Presenter



def main():
    """MVP architecture to separate logic from interface"""
    _view = View()
    _presenter = Presenter(_view)
    _view.set_presenter(_presenter)

    _presenter.run()

if __name__ == '__main__':
    main()