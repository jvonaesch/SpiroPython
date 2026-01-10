from spiro.EvaluationRecord import EvaluationRecord


class Evaluator:

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, record: EvaluationRecord):
        vals = record[self]
        if vals is None:
            eval_args = []
            for arg in self.args:
                if isinstance(arg, Evaluator):
                    eval_args.append(arg(record))
                else:
                    eval_args.append(arg)
            record[self] = self.func(*eval_args)
