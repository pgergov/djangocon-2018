from astroid.node_classes import Return
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class MyChecker(BaseChecker):
    __implements__ = (IAstroidChecker, )
    name = 'my-checker'
    msgs = {
        'R1234': ('No list comprehensions allowed :(',
                  'no-list-comprehensions',
                  'Sorry.'),
        'R1235': ('Lambdas too complicated',
                  'no-lambda',
                  'Too hard.'),
        'R1236': ('No need to return None at the end',
                  'no-redundant-return',
                  'You can do better..')
    }

    def visit_listcomp(self, node):
        self.add_message('no-list-comprehensions', node=node)

    def visit_lambda(self, node):
        self.add_message('no-lambda', node=node)

    def visit_functiondef(self, node):
        last = node.last_child()

        if isinstance(last, Return) and not last.bool_value():
            self.add_message('no-redundant-return', node=node)

    def close(self):
        print('You are GOAT!')
